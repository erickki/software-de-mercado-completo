from flask import Flask, redirect, url_for, render_template, request

from src.login import validar_login
from src.registro import validar_registro

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fazer_login', methods=['POST'])
def fazer_login():
    entrada_email = request.form.get('entrada_email_validar')
    entrada_senha = request.form.get('entrada_senha_validar')
    verificacao_login = validar_login(entrada_email, entrada_senha)

    if verificacao_login == 'pode logar':
        return redirect(url_for('registro'))
    elif verificacao_login == 'sem cadastro':
        return render_template('login.html', erro='Usuário não cadastrado.')
    elif verificacao_login == 'senha errada':
        return render_template('login.html', erro='Senha incorreta.')
    else:
        return render_template('login.html', erro='Erro desconhecido.')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/fazer_registro', methods=['POST'])
def fazer_registro():
    entrada_nome = request.form.get('entrada_nome_validar')
    entrada_email = request.form.get('entrada_email_validar')
    entrada_senha = request.form.get('entrada_senha_validar')
    entrada_senha2 = request.form.get('entrada_senha2_validar')
    verificacao_registro = validar_registro(entrada_nome, entrada_email, entrada_senha, entrada_senha2)

    if verificacao_registro == 'registrado':
        return redirect(url_for('login'))
    elif verificacao_registro == 'falta informacao':
        return render_template('registro.html', erro='Preencha todos os campos.')
    elif verificacao_registro == 'ja registrado':
        return render_template('registro.html', erro='Email já registrado.')
    elif verificacao_registro == 'senhas diferentes':
        return render_template('registro.html', erro='As senhas precisam ser iguais.')
    else:
        return render_template('login.html', erro='Erro desconhecido.')

@app.route('/esqueceu_senha')
def esqueceu_senha():
    return render_template('esqueceu_senha.html')

if __name__ == '__main__':
    app.run(debug=True)