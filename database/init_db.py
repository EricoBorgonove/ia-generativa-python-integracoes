
from database.connection import conectar


def inicializar_banco():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS atendimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                categoria TEXT NOT NULL,
                descricao TEXT NOT NULL,
                status TEXT NOT NULL
                    CHECK (
                        status IN (
                            'pendente',
                            'em andamento',
                            'concluido'
                        )
                    ),
                data_abertura TEXT NOT NULL
            )
        """)

        conexao.commit()
