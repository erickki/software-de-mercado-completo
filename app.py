from flask import Flask, redirect, url_for, render_template, request

from src.sistema_login import fazer_login
from src.sistema_login import fazer_esqueci_senha
from src.sistema_login import fazer_resetar_senha
from src.sistema_login import fazer_registro

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/esqueci_senha')
def esqueci_senha():
    return render_template('esqueci_senha.html')

@app.route('/resetar_senha')
def resetar_senha():
    return render_template('resetar_senha.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/sistema_inicio')
def sistema_inicio():
    return render_template('sistema_inicio.html')

@app.route('/sistema_funcionarios')
def sistema_funcionarios():
    return render_template('sistema_funcionarios.html')

if __name__ == '__main__':
    app.run(debug=True)