import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / 'database'
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / 'database.db'

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Criar tabela de usuários
cur.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# Criar tabela de notas
cur.execute('''
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    checkbox INTEGER NOT NULL,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
''')

conn.commit()
conn.close()
print("Banco de dados inicializado com sucesso!")
