import sqlite3

banco_dados = 'data/banco_dados_roxho.db'

def validar_dado_nome(registro_login_salvo):
    conn = sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nome FROM usuarios_sistema_roxho WHERE email = ?",(registro_login_salvo,)
    )
    resultado_nome = cursor.fetchone()
    return resultado_nome[0]