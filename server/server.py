from flask import Flask, request, jsonify, make_response
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from JsonUtils import convert_input_to, json_repr
from Erro import Erro
import json

# Aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ifpbinfo@10.1.134.157/nutrif' # mysql://usuario:senha@localhost/nomedobanco

# Conexão com o Banco de Dados
db = SQLAlchemy(app)
#db.Model.metadata.reflect(db.engine)
CORS(app)

class Aluno(db.Model):
    __tablename__ = 'tb_aluno'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    matricula = db.Column('nm_matricula', db.String(13))
    senha = db.Column('nm_senha', db.String(77))
    isacesso = db.Column('is_acesso', db.Boolean)
    nome = db.Column('nm_nome', db.String(77))
    email = db.Column('nm_email', db.String(77))
    isativo = db.Column('is_ativo', db.Boolean)

    def __init__(self, matricula, senha):
        self.matricula = matricula
        self.senha = senha

@app.route("/", methods=['GET'])
def index():
    print("GET")
    return "Ola"

@app.route("/aluno/matricula/<int:matricula>", methods=['GET'])
def buscarAlunoPorMatricula(matricula):

    # Consultar os dados do Aluno no Banco de Dados.
    aluno = Aluno.query.filter_by(matricula=matricula).first()


    if aluno != None:
        del(aluno.__dict__['_sa_instance_state'])

        # Enviar os dados na resposta
        return (json.dumps(aluno.__dict__), status.HTTP_200_OK)
    else:
        erro = Erro("Aluno nao encontrado")
        return (erro.mensagem, status.HTTP_404_NOT_FOUND)

@app.route("/aluno/login", methods=['POST'])
@convert_input_to(Aluno)
def login(aluno):
    # Converter JSON para Objeto.
    matricula = aluno.matricula
    senha = aluno.senha
    # Consultar os dados do Aluno no Banco de Dados.
    aluno = Aluno.query.filter_by(matricula=matricula, senha=senha).first()

    if aluno != None:
        del(aluno.__dict__['_sa_instance_state'])

        # Enviar os dados na resposta
        return (json.dumps(aluno.__dict__), status.HTTP_200_OK)
    else:
        erro = Erro("Aluno nao encontrado")
        return (erro.mensagem, status.HTTP_404_NOT_FOUND)

app.run(debug=True, use_reloader=True)
