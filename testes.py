import sqlite3

banco_dados = 'data/banco_dados_roxho.db'

conn = sqlite3.connect(banco_dados)
cursor = conn.cursor()

entrada_email = 'admin@roxho.com.br'
entrada_senha = 'admin'

try:
    cursor.execute(
        "SELECT senha FROM usuarios_sistema WHERE email = ?", (entrada_email,)
    )
    resultado_senha = cursor.fetchone()
    print(resultado_senha)
    if entrada_senha == resultado_senha[0]:
        print(f'pode logar')
    else:
        print(f'senha errada')
except:
    print(f'sem cadastro')