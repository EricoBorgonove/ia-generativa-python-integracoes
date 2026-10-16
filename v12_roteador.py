
from core.source_router import identificar_fonte

perguntas = [
    "Qual é a temperatura em Manaus?",
    "Vai chover amanhã?",
    "Quantos atendimentos estão pendentes?",
    "Qual categoria possui mais atendimentos?",
    "Explique o que é uma API REST",
    "Compare os atendimentos com o clima"
]

for pergunta in perguntas:
    fonte = identificar_fonte(pergunta)

    print("\nPergunta:", pergunta)
    print("Fonte identificada:", fonte)
