import sqlite3
import random
from plyer import notification

entrada_nome = 'Erick'
entrada_email = 'aerick@roxho.com.br'

banco_dados = 'data/banco_dados_roxho.db'
conn = sqlite3.connect(banco_dados)
cursor = conn.cursor()
cursor.execute(
    "SELECT nome, email FROM usuarios_sistema WHERE email = ?",(entrada_email,)
)
resultado_email = cursor.fetchone()
print(resultado_email)
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
        else:
            print(f'Nome errado')
except:
    print(f'Email errado')