from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def questao1():
    nome = "Guilherme"
    return render_template('questao1.html', nome=nome)

@app.route('/idade')
def questao2():
    nome = "Guilherme"
    idade = 17
    return render_template('questao2.html', nome=nome, idade=idade)

@app.route('/dados')
def questao3():
    dados = {"nome": "Ana", "email": "ana@email.com"}
    return render_template('questao3.html', dados=dados)

@app.route('/alunos')
def questao4():
    alunos = [
        {"nome": "Ana", "nota": 8.5},
        {"nome": "Bruno", "nota": 7.0},
        {"nome": "Carlos", "nota": 9.2},
        {"nome": "Daniela", "nota": 6.8},
        {"nome": "Eduardo", "nota": 8.0}
]
    return render_template('questao4.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)
