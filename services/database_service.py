
from database.connection import conectar
from database.init_db import inicializar_banco


STATUS_VALIDOS = {
    "pendente",
    "em andamento",
    "concluido"
}


def listar_atendimentos(limite=20):
    """Retorna os atendimentos mais recentes."""

    if not isinstance(limite, int) or not 1 <= limite <= 100:
        raise ValueError("O limite deve estar entre 1 e 100.")

    inicializar_banco()

    with conectar() as conexao:
        registros = conexao.execute("""
            SELECT id, cliente, categoria,
                   descricao, status, data_abertura
            FROM atendimentos
            ORDER BY data_abertura DESC, id DESC
            LIMIT ?
        """, (limite,)).fetchall()

        return [dict(item) for item in registros]


def contar_atendimentos(status=None):
    """Conta atendimentos, com filtro opcional."""

    inicializar_banco()

    if status is not None and status not in STATUS_VALIDOS:
        raise ValueError("Status inválido.")

    with conectar() as conexao:

        if status is None:
            resultado = conexao.execute("""
                SELECT COUNT(*) AS total
                FROM atendimentos
            """).fetchone()
        else:
            resultado = conexao.execute("""
                SELECT COUNT(*) AS total
                FROM atendimentos
                WHERE status = ?
            """, (status,)).fetchone()

        return resultado["total"]


def atendimentos_por_categoria():
    """Agrupa os atendimentos por categoria."""

    inicializar_banco()

    with conectar() as conexao:
        registros = conexao.execute("""
            SELECT categoria, COUNT(*) AS total
            FROM atendimentos
            GROUP BY categoria
            ORDER BY total DESC
        """).fetchall()

        return [dict(item) for item in registros]


def atendimentos_por_status():
    """Agrupa os atendimentos por status."""

    inicializar_banco()

    with conectar() as conexao:
        registros = conexao.execute("""
            SELECT status, COUNT(*) AS total
            FROM atendimentos
            GROUP BY status
            ORDER BY total DESC
        """).fetchall()

        return [dict(item) for item in registros]


def resumo_atendimentos():
    """Retorna um resumo estruturado do banco."""

    return {
        "fonte": "SQLite",
        "total": contar_atendimentos(),
        "pendentes": contar_atendimentos("pendente"),
        "em_andamento": contar_atendimentos(
            "em andamento"
        ),
        "concluidos": contar_atendimentos("concluido"),
        "por_categoria": atendimentos_por_categoria(),
        "por_status": atendimentos_por_status()
    }
