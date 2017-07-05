from flask_sqlalchemy import SQLAlchemy

class Aluno:
	def __init__(self, matricula, senha):
		self.matricula = matricula
		self.senha = senha