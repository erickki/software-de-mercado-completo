import sqlite3

def validar_registro(entrada_nome, entrada_email, entrada_senha, entrada_senha2):
    banco_dados = 'data/banco_dados_roxho.db'
    conn = sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    if not entrada_nome or not entrada_email or not entrada_senha or not entrada_senha2:
        return 'falta informacao'
    else:
        cursor.execute(
            "SELECT email FROM usuarios_sistema WHERE email = ?", (entrada_email,)
        )
        resultado_email = cursor.fetchone()
        if resultado_email:
            return 'ja registrado'
        else:
            if entrada_senha == entrada_senha2:
                cursor.execute(
                    "INSERT INTO usuarios_sistema (nome, email, senha) VALUES (?, ?, ?)",
                    (entrada_nome, entrada_email, entrada_senha)
                )
                conn.commit()
                conn.close()
                return 'registrado'
            else:
                return 'senhas diferentes'