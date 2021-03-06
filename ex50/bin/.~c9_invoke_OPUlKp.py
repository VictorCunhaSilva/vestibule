from sqlalchemy import create_engine
from flask import Flask
import json
from flask_jsonpify import jsonify
from flask_mysqldb import MySQL

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'
mysql = MySQL(app)

@app.route("/") # decorator para rotear a view
def hello_world(): # view
    return "Hello World! Bem vindo ao Vestibule"
    
@app.route('/usuarios')
def users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM c9.usuario')
    rv = cur.fetchall()
    return jsonify(str(rv))
    
@app.route('/usuarios/<email>/<senha>')
def login(email=None, senha=None):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM c9.usuario where email= \'"+email+"\'"+" and senha=\'"+senha+"\'")
    rv = cur.fetchall()
    print (rv)
    return jsonify("200")

@app.route('/cadastrausuario/<email>/<nome>/<senha>')
def cadastrausuario(email=None, nome=None, senha=None):
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO c9.usuario(email,nome,senha) VALUES (%s,%s,%s)''', (email,nome,senha))
    mysql.connection.commit()
    return jsonify("200")
    
@app.route('/videos')
def videos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM c9.video')
    rv = cur.fetchall()
    return jsonify(str(rv))

@app.route('/cadastravideo/<nome>/<descricao>')
def cadastravideo(nome=None, descricao=None):
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO c9.video(nome,descricao) VALUES (%s,%s)''', (nome,descricao))
    mysql.connection.commit()
    return jsonify("200")

@app.route('/cadastracomentario/<nomevideo>/<nome>/<descricao>')
def cadastracomentario(nomevideo=None, nome=None, descricao=None):
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO c9.comentario(nomevideo,nome,comentario) VALUES (%s,%s,%s)''', (nomevideo,nome,descricao))
    mysql.connection.commit()
    return jsonify("200")

@app.route('/comentarios')
def comentarios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM c9.comentario')
    rv = cur.fetchall()
    return jsonify(rv)#return jsonify(str(rv))
    #
@app.route('/comentarios/<nomevideo>')
def comentariosvideo(nomevideo=None):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM c9.comentario where nomevideo = \'"+ nomevideo+"\'")
    rv = cur.fetchall()
    return jsonify(rv)#return jsonify(str(rv))

#app.run(host="") # inicia o servidor
app.run(host='0.0.0.0', port='8080', debug = True)