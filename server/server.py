from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from JsonUtils import convert_input_to, json_repr
import MySQLdb
from Aluno import Aluno
import json

app = Flask(__name__)
CORS(app)

@app.route("/aluno/consultar/matricula/<int:matricula>", methods=['GET'])
def buscarAlunoPorMatricula(matricula):
	print("GET")

	return ""

@app.route("/aluno/login", methods=['POST'])
@convert_input_to(Aluno)
def login(aluno):

	
    # Converter JSON para Objeto.
    content = request.get_json(silent=True)
    print(aluno.matricula)
    # Consultar os dados do Aluno no Banco de Dados.
    

    # Enviar os dados na resposta
    return make_response(json_repr(aluno))

app.run(debug=True, use_reloader=True)