from flask import Flask, redirect, render_template
from controle import insert_data_in_db, coleta_data_of_db, trata_headers

app = Flask('claclick')

@app.route('/')
def index():

	data = trata_headers()
	insert_data_in_db(data)
	print 'LOG: ' + str(coleta_data_of_db())
	return redirect('https://www.facebook.com/ClaClick-272681776174594')


@app.route('/consulta')
def consulta():
	registros = coleta_data_of_db()
	return render_template(
		'consulta.html',
		registros=registros
		)

if __name__=='__main__':
	app.run(debug=True)

