import sqlite3
import os
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.getenv('DATABASE_PATH', BASE_DIR / 'database' / 'database.db'))

def getConnection():
    return sqlite3.connect(DB_PATH)

class Notas:
    # Limpar input para evitar injeções e formalizar os dados.
    @staticmethod
    def limpar(dic):
        texto = ''
        checkbox = 0

        for k, v in dic.items():
            if k.startswith('text-note'):
                texto = str(v).strip()
            if k.startswith('checkbox'):
                checkbox = 1
        
        if not texto:
            return None

        return {
            'texto': texto,
            'checkbox': checkbox
        }

    # Adicionar nova nota ao banco de dados.
    @staticmethod
    def adicionar(texto, checkbox, usuario_id):
        with getConnection() as conn:

            cur = conn.cursor()

            cur.execute('''
                INSERT INTO notas (texto, checkbox, usuario_id) VALUES (?, ?, ?)
            ''',
            (texto, checkbox, usuario_id,)
            )

class Usuarios:
    # Limpar o input do registro para evitar injeções e formalizar os dados.
    @staticmethod
    def limparRegistro(dic):
        usuario = dic.get('user-login')
        email = dic.get('user-email-login')
        senha = dic.get('senha-login')
        confirmarSenha = dic.get('confirmar-senha-login')

        usuarioLimpo = str(usuario).strip().lower()
        emailLimpo = str(email).strip().lower()
        senhaLimpa = str(senha).strip()
        confirmarSenhaLimpa = str(confirmarSenha).strip()

        if senhaLimpa != confirmarSenhaLimpa:
            return None

        return {
            'usuario': usuarioLimpo,
            'email': emailLimpo,
            'senha': senhaLimpa
        }

    # Limpar o input do login para evitar injeções e formalizar os dados.
    @staticmethod
    def limparLogin(dic):
        usuario = dic.get('user-login')
        email = dic.get('user-email-login')
        senha = dic.get('senha-login')

        usuarioLimpo = str(usuario).strip().lower()
        emailLimpo = str(email).strip().lower()
        senhaLimpa = str(senha).strip()

        return {
            'usuario': usuarioLimpo,
            'email': emailLimpo,
            'senha': senhaLimpa
        }

    # Conferir se o usuario já está cadastrado no login.
    @staticmethod
    def conferirLogin(email, usuario, senha):
        with getConnection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, senha
                FROM usuarios
                WHERE email = ? OR usuario = ?
                ''',
                (email, usuario)
            )

            row = cur.fetchone()

            if row and check_password_hash(row[1], senha):
                return row[0]

            return None

    # Conferir se o usuario já está cadastrado para não haver repetição.
    @staticmethod
    def conferirusuario(usuario):
        with getConnection() as conn:

            cur = conn.cursor()

            cur.execute('''
                SELECT usuario FROM usuarios WHERE usuario = ?
            ''',
            (usuario,)
            )

            existe = cur.fetchone()

            return existe

    # Conferir se o email já está cadastrado para não haver repetição.
    @staticmethod
    def conferirEmail(email):
        with getConnection() as conn:

            cur = conn.cursor()

            cur.execute('''
                SELECT email FROM usuarios WHERE email = ?
            ''',
            (email,)
            )

            existe = cur.fetchone()

            return existe

    # Registrar o email e a senha para login.
    @staticmethod
    def registrar(email, senha, usuario):
        senha_hash = generate_password_hash(senha)
        
        with getConnection() as conn:

            cur = conn.cursor()

            cur.execute('''
                INSERT INTO usuarios (email, senha, usuario)
                VALUES (?, ?, ?)
            ''',
            (email, senha_hash, usuario,)
            )
