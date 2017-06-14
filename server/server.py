from flask import Flask
from flask_cors import CORS
import MySQLdb

app = Flask(__name__)
CORS(app)

con = MySQLdb.connect(user='root', db='avaliacao')

c = con.cursor()


@app.route("/login/<int:matricula>")
def login(matricula):
    c.execute("SELECT * FROM tb_aluno")
    query = (c.fetchall())
    for aluno in query:
        if str(matricula) in aluno:
            return "Matrícula encontrada"
        else:
            return "Matrícula não encontrada"



app.run(debug=True, use_reloader=True)