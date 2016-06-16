from flask import Flask, redirect
from controle import insert_data_in_db, coleta_data_of_db, trata_headers

app = Flask('claclick')



@app.route('/')
def index():

	data = trata_headers()
	insert_data_in_db(data)
	print 'LOG: ' + str(coleta_data_of_db())
	
	#return redirect('https://www.facebook.com/ClaClick-272681776174594')
	return redirect('/n')
	#return str(coleta_data_of_db())

#	return 'feito'

@app.route('/n')
def retorne():
	return 'foi feito <a href="/">voltar</a>'

@app.route('/consulta')
def consulta():
	return str(coleta_data_of_db())

if __name__=='__main__':
	app.run(debug=True)

