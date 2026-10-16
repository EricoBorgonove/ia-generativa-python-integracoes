
import json

from services.database_service import (
    listar_atendimentos,
    contar_atendimentos,
    resumo_atendimentos
)

print("\n=== CONTAGEM ===")

print(
    "Atendimentos pendentes:",
    contar_atendimentos("pendente")
)

print("\n=== ÚLTIMOS ATENDIMENTOS ===")

for atendimento in listar_atendimentos(limite=5):
    print(
        atendimento["cliente"],
        "-",
        atendimento["status"]
    )

print("\n=== RESUMO PARA A IA ===")

resumo = resumo_atendimentos()

print(
    json.dumps(
        resumo,
        indent=4,
        ensure_ascii=False
    )
)
