from flask import Flask, render_template, request, url_for, session, redirect
from model import Notas, Usuarios
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Rota para a homepage.
@app.get('/')
def homepage():
    return render_template('homepage.html')

# Rota para a funcionalidade principal do web app.
@app.route('/principal', methods=['GET', 'POST'])
def principal():
    if not session.get('usuario'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        limpo = Notas.limpar(request.form)
        if not limpo:
            return '', 400

        textoLimpo = limpo.get('texto')
        checkboxLimpa = limpo.get('checkbox')

        # Retornar o id do usuário
        usuario_id = session.get('usuario')
        
        Notas.adicionar(textoLimpo, checkboxLimpa, usuario_id)
        return '', 204

    return render_template('base.html')

# Rota para o sobre page.
@app.get('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para o login page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        limpo = Usuarios.limparLogin(request.form)

        usuario = limpo.get('usuario')
        email = limpo.get('email')
        senha = limpo.get('senha')

        usuario_id = Usuarios.conferirLogin(email, usuario, senha)

        if usuario_id:
            session['usuario'] = usuario_id
            return {
                'ok': True,
                'redirect': url_for('principal')
            }, 200

        else:
            return {
                'ok': False,
                'error': 'Usuário ou senha inválidos'
            }, 401

    return render_template('login.html')

# Rota para o registro page.
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        limpo = Usuarios.limparRegistro(request.form)
        if limpo is None:
            return 'As senhas não coincidem!', 400

        usuario = limpo.get('usuario')
        email = limpo.get('email')
        senha = limpo.get('senha')

        emailConferido = Usuarios.conferirEmail(email)
        usuarioConferido = Usuarios.conferirusuario(usuario)

        if emailConferido is not None:
            return {
                'ok': False,
                'error': 'Este email já está vinculado a uma conta!'
            }, 401
            
        elif usuarioConferido is not None:
            return {
                'ok': False,
                'error': 'Este nome de usuário já está vinculado a uma conta!'
            }, 401

        else:
            Usuarios.registrar(email, senha, usuario)
            return {
                'ok': True,
                'redirect': url_for('principal')
            }, 200
            
    return render_template('registro.html')
