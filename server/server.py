from flask import Flask, request, jsonify, make_response
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from JsonUtils import convert_input_to, json_repr
from Erro import Erro
import json

# Aplicação Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ifpbinfo@localhost/avaliacao' # mysql://usuario:senha@localhost/nomedobanco

# Conexão com o Banco de Dados
db = SQLAlchemy(app)
#db.Model.metadata.reflect(db.engine)
CORS(app)

#MApeamento da Tabela Aluno
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

#Mapeamento da Tabela Questao
class Questao(db.Model):
    __tablename__ = 'tb_questao'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    pergunta = db.Column('pergunta', db.String)

    def __init__(self, pergunta):
        self.pergunta = pergunta

#Mapeamento da Tabela tb_resposta
class Resposta(db.Model):
    __tablename__ = 'tb_resposta'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    idQuestao = db.Column('id_questao', db.Integer, db.ForeignKey('tb_questao.id'))
    idAluno = db.Column('id_aluno', db.Integer, db.ForeignKey('tb_aluno.id'))
    nota = db.Column('nota', db.String)

    def __init__(self, idQuestao, idAluno, nota):
        self.idQuestao = idQuestao
        self.idAluno = idAluno
        self.nota = nota


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


@app.route("/aluno/perguntas", methods=["GET"])
def buscarPerguntas():
    perguntas = Questao.query.all()
    perguntasJson = {}

    for pergunta in perguntas:
        del(pergunta.__dict__['_sa_instance_state'])
        pergunta = pergunta.__dict__

        perguntasJson["p" + str(pergunta["id"])] = pergunta["pergunta"]

    perguntasJson = json.dumps(perguntasJson)
    return perguntasJson



@app.route("/aluno/resposta", methods=["POST"])
def enviarRespostas():
    posts = request.json

    respostas = posts['respostas']
    idAluno = posts['id']


    for resposta in respostas:

        idQuestao = resposta.replace('p', '')
        nota = respostas[resposta]
        resposta = Resposta(idQuestao,idAluno,nota)
        db.session.add(resposta)
        db.session.commit()

    return "OK",200


app.run(debug=True, use_reloader=True)
