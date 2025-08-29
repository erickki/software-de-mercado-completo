import sqlite3
import random
from plyer import notification

def validar_esqueceu_senha(entrada_nome, entrada_email):
    banco_dados = 'data/banco_dados_roxho.db'
    conn = sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    if not entrada_nome or not entrada_email:
        return 'falta informacao'
    else:
        cursor.execute(
            "SELECT nome, email FROM usuarios_sistema WHERE email = ?",(entrada_email,)
        )
        resultado_email = cursor.fetchone()
        try:
            if resultado_email[1] == entrada_email:
                if resultado_email[0] == entrada_nome:
                    codigo_gerado_verificacao = random.randint(100000, 999999)
                    cursor.execute(
                        "UPDATE usuarios_sistema SET codigo_recuperacao = ? WHERE email = ?",(codigo_gerado_verificacao, entrada_email)
                    )
                    conn.commit()
                    conn.close()
                    notification.notify(
                        title="Código de Recuperação",
                        message=f"Seu código é {codigo_gerado_verificacao}",
                        timeout=10
                    )
                    return 'codigo gerado'
                else:
                    return 'nome incorreto'
        except:
            return 'email nao registrado'