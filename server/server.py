from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from JsonUtils import convert_input_to, json_repr
from Aluno import Aluno
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/avaliacao' # mysql://usuario:senha@localhost/nomedobanco
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
CORS(app)

class tb_aluno(db.Model):
    __table__ = db.Model.metadata.tables['tb_aluno']

    def __repr__(self):
        return self.matricula

@app.route("/aluno/consultar/matricula/<int:matricula>", methods=['GET'])
def buscarAlunoPorMatricula(matricula):
	print("GET")

	return ""

@app.route("/aluno/login", methods=['POST'])
@convert_input_to(Aluno)
def login(aluno):
	# Converter JSON para Objeto.
	print(aluno.matricula)
	# Consultar os dados do Aluno no Banco de Dados.
	query = map(str, tb_aluno.query.all()) # Transformando todos os itens da lista (consulta) em string
	if str(aluno.matricula) in query:
		print("Logado!")
		# Enviar os dados na resposta
		return make_response(json_repr(aluno))
	else:
		# Retornar erro
		print("Erro de autenticação!")
		return "Erro"

app.run(debug=True, use_reloader=True)