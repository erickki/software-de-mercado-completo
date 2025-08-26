import random
from plyer import notification

codigo_gerado_verificacao = random.randint(100000, 999999)
notification.notify(
    title="Código de Recuperação",
    message=f"Seu código é {codigo_gerado_verificacao}",
    timeout=10
)