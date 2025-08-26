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
            if resultado_email[1]:
                if entrada_nome == resultado_email[0] and entrada_email == resultado_email[1]:
                    codigo_gerado_verificacao = random.randint(100000, 999999)
                    cursor.execute(
                        "UPDATE usuarios_sistema SET codigo_recuperacao = ? WHRE email = ?",(codigo_gerado_verificacao, entrada_email)
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
                    return 'erro desconhecido'
        except:
            return 'nao registrado'