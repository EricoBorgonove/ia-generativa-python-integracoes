
from database.connection import conectar

# Consulta 1: listar todos os atendimentos
print("\n=== TODOS OS ATENDIMENTOS ===")

with conectar() as conexao:
    registros = conexao.execute("""
        SELECT id, cliente, categoria,
               status, data_abertura
        FROM atendimentos
        ORDER BY data_abertura DESC
    """).fetchall()

    for registro in registros:
        print(dict(registro))


# Consulta 2: contar atendimentos pendentes
print("\n=== ATENDIMENTOS PENDENTES ===")

with conectar() as conexao:
    total = conexao.execute("""
        SELECT COUNT(*) AS total
        FROM atendimentos
        WHERE status = ?
    """, ("pendente",)).fetchone()

    print("Quantidade:", total["total"])


# Consulta 3: agrupar por categoria
print("\n=== ATENDIMENTOS POR CATEGORIA ===")

with conectar() as conexao:
    resultado = conexao.execute("""
        SELECT categoria, COUNT(*) AS total
        FROM atendimentos
        GROUP BY categoria
        ORDER BY total DESC
    """).fetchall()

    for item in resultado:
        print(item["categoria"], ":", item["total"])


# Consulta 4: agrupar por status
print("\n=== ATENDIMENTOS POR STATUS ===")

with conectar() as conexao:
    resultado = conexao.execute("""
        SELECT status, COUNT(*) AS total
        FROM atendimentos
        GROUP BY status
        ORDER BY total DESC
    """).fetchall()

    for item in resultado:
        print(item["status"], ":", item["total"])
