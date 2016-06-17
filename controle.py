from flask import request, Response
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/monitor2_db')

db = client.monitor2_db
registro = db.registro

def insert_data_in_db(data):
    registro_id = registro.insert(data)

def trata_headers():
    res = Response(request).response.environ
    date,time = str(datetime.now()).split(' ')

    print '-----'
    print res['SERVER_NAME']
    print res['REMOTE_ADDR']
    print res['HTTP_USER_AGENT'].split(';')[1]
    print '-----'

    response_dic = {
        'request_method': res['REQUEST_METHOD'],
        'path_info': res['PATH_INFO'],
        'protocol': res['SERVER_PROTOCOL'],
        'user_agent': res['HTTP_USER_AGENT'],
        'server_name': res['SERVER_NAME'],
        'server_port': res['SERVER_PORT'],
        'http_accept': res['HTTP_ACCEPT'],
        'remote_addr': res['REMOTE_ADDR'],
        'language': res['HTTP_ACCEPT_LANGUAGE'].split(',')[0],
        'so': res['HTTP_USER_AGENT'].split(';')[1],
        'date': date,
        'time': time,
    }
    return response_dic

def coleta_data_of_db():
    date,time = str(datetime.now()).split(' ')
    return registro.find().sort([("date",-1),("time",-1)])
    