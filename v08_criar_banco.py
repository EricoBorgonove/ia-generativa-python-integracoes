
from database.connection import conectar
from database.init_db import inicializar_banco

inicializar_banco()

atendimentos = [
    (
        "Ana Souza", "Suporte",
        "Problema de acesso ao sistema",
        "pendente", "2026-10-10"
    ),
    (
        "Carlos Lima", "Financeiro",
        "Solicitação de segunda via",
        "concluido", "2026-10-11"
    ),
    (
        "Mariana Costa", "Suporte",
        "Erro no cadastro",
        "em andamento", "2026-10-12"
    ),
    (
        "Pedro Oliveira", "Acadêmico",
        "Solicitação de declaração",
        "pendente", "2026-10-13"
    ),
    (
        "Juliana Santos", "Financeiro",
        "Dúvida sobre pagamento",
        "concluido", "2026-10-13"
    ),
    (
        "Roberto Alves", "Suporte",
        "Recuperação de senha",
        "pendente", "2026-10-14"
    ),
    (
        "Fernanda Rocha", "Acadêmico",
        "Ajuste de matrícula",
        "em andamento", "2026-10-14"
    ),
    (
        "Lucas Ferreira", "Suporte",
        "Falha no login",
        "concluido", "2026-10-15"
    )
]

with conectar() as conexao:
    total = conexao.execute(
        "SELECT COUNT(*) FROM atendimentos"
    ).fetchone()[0]

    if total == 0:
        conexao.executemany("""
            INSERT INTO atendimentos (
                cliente,
                categoria,
                descricao,
                status,
                data_abertura
            )
            VALUES (?, ?, ?, ?, ?)
        """, atendimentos)

        conexao.commit()
        print("8 atendimentos cadastrados.")
    else:
        print("O banco já possui registros.")

print("Banco de dados preparado!")
