from flask import Flask, redirect

app = Flask('claclick')


@app.route('/')
def index():
    return redirect('https://www.facebook.com/ClaClick-272681776174594')