
from ollama import Client

from config import OLLAMA_MODEL, OLLAMA_HOST

cliente = Client(
    host=OLLAMA_HOST,
    timeout=120.0
)

pergunta = input("Digite sua pergunta: ")

resposta = cliente.chat(
    model=OLLAMA_MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "Você é um assistente educacional. "
                "Responda em português brasileiro."
            )
        },
        {
            "role": "user",
            "content": pergunta
        }
    ]
)

print("\nResposta da IA:")
print(resposta.message.content)
