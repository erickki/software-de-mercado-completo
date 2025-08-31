from flask import Flask, redirect, url_for, render_template, request

from src.sistema_login import fazer_login
from src.sistema_login import fazer_esqueci_senha
from src.sistema_login import fazer_resetar_senha
from src.sistema_login import fazer_registro
from src.sistema_validar_dados import validar_dado_nome

app = Flask(__name__)

registro_login_salvo = ''

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/erro_no_login', methods=['POST'])
def erro_no_login():
    global registro_login_salvo
    entrada_email = request.form.get('entrada_email_validar')
    entrada_senha = request.form.get('entrada_senha_validar')
    registro_login_salvo = entrada_email
    verificacao_login = fazer_login(entrada_email, entrada_senha)
    if verificacao_login == 'pode logar':
        registro_login_salvo = entrada_email
        return redirect(url_for('inicio')) 
    elif verificacao_login == 'senha incorreta':
        return render_template('login.html', erro='Senha incorreta.')
    elif verificacao_login == 'email não localizado':
        return render_template('login.html', erro='Usuário não cadastrado.')
    else:
        return render_template('login.html', erro='Erro desconhecido.')

@app.route('/esqueci_senha')
def esqueci_senha():
    return render_template('esqueci_senha.html')

@app.route('/erro_esqueci_senha', methods=['POST'])
def erro_esqueci_senha():
    entrada_nome = request.form.get('entrada_nome_validar')
    entrada_email = request.form.get('entrada_email_validar')
    verificacao_esqueci_senha = fazer_esqueci_senha(entrada_nome, entrada_email)
    if verificacao_esqueci_senha == 'codigo gerado':
        return redirect(url_for('resetar_senha'))
    elif verificacao_esqueci_senha == 'nome incorreto':
        return render_template('esqueci_senha.html', erro='Nome incorreto.')
    elif verificacao_esqueci_senha == 'email não localizado':
        return render_template('esqueci_senha.html', erro='Usuário não cadastrado.')
    else:
        return render_template('esqueci_senha.html', erro='Erro desconhecido.')

@app.route('/resetar_senha')
def resetar_senha():
    return render_template('resetar_senha.html')

@app.route('/erro_resetar_senha', methods=['POST'])
def erro_resetar_senha():
    entrada_email = request.form.get('entrada_email_validar')
    entrada_senha = request.form.get('entrada_senha_validar')
    entrada_senha2 = request.form.get('entrada_senha2_validar')
    entrada_codigo = request.form.get('entrada_codigo_validar')
    if not entrada_email or not entrada_senha or not entrada_senha2 or not entrada_codigo:
        return render_template('resetar_senha.html', erro='Preencha todos os campos.')
    elif entrada_senha != entrada_senha2:
        return render_template('resetar_senha.html', erro='As senhas precisam ser iguais.')
    else:
        verificacao_resetar_senha = fazer_resetar_senha(entrada_email, entrada_senha, entrada_codigo)
        if verificacao_resetar_senha == 'senha alterada':
            return redirect(url_for('login'))
        elif verificacao_resetar_senha == 'codigo incorreto':
            return render_template('resetar_senha.html', erro='Código incorreto.')
        elif verificacao_resetar_senha == 'email não localizado':
            return render_template('resetar_senha.html', erro='Usuário não cadastrado.')
        else:
            return render_template('resetar_senha.html', erro='Erro desconhecido.')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/erro_registro', methods=['POST'])
def erro_registro():
    entrada_nome = request.form.get('entrada_nome_validar')
    entrada_email = request.form.get('entrada_email_validar')
    entrada_senha = request.form.get('entrada_senha_validar')
    entrada_senha2 = request.form.get('entrada_senha2_validar')
    if not entrada_nome or not entrada_email or not entrada_senha or not entrada_senha2:
        return render_template('registro.html', erro='Preencha todos os campos.')
    elif entrada_senha != entrada_senha2:
        return render_template('registro.html', erro='As senhas precisam ser iguais.')
    else:
        verificacao_registro = fazer_registro(entrada_nome, entrada_email, entrada_senha)
        if verificacao_registro == 'registrado':
            return redirect(url_for('login'))
        elif verificacao_registro == 'email já cadastrado':
            return render_template('registro.html', erro='Email já cadastrado.')
        else:
            return render_template('registro.html', erro='Erro desconhecido.')

@app.route('/inicio')
def inicio():
    global registro_login_salvo
    nome_salvo = validar_dado_nome(registro_login_salvo)
    return render_template('inicio.html', nome=nome_salvo)

@app.route('/cadastros_funcionarios')
def cadastros_funcionarios():
    return render_template('cadastros_funcionarios.html')

if __name__ == '__main__':
    app.run(debug=True)