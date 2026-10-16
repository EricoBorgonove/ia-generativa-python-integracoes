
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "atendimentos.db"


def conectar():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row

    return conexao
