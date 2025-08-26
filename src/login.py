import sqlite3

def validar_login(entrada_email, entrada_senha):
    banco_dados = 'data/banco_dados_roxho.db'
    conn = sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT senha FROM usuarios_sistema WHERE email = ?", (entrada_email,)
        )
        resultado_senha = cursor.fetchone()
        if entrada_senha == resultado_senha[0]:
            return 'pode logar'
        else:
            return 'senha errada'
    except:
        return 'sem cadastro'
    finally:
        conn.close()