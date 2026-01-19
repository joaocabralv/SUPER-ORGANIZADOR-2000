## SUPER ORGANIZADOR 2000

Um app para organizar o seu dia.<br>
Ainda está incompleto e ficará assim por um bom tempo, se não para sempre.<br>
Esse é o meu primeiro web app, criei com o intuito de aprender mais e testar o que já sei.<br>
<br>
export SECRET_KEY="sua_chave_aqui"<br>
<br>
Próximas atualizações:<br>
- Acessar notas salvas<br>
- Editar nome de perfil, email ou senha<br>
- Homepage interessante<br>

## Como rodar o projeto

```bash
git clone https://github.com/joaocabralv/super-organizador-2000
cd superorganizador2000
python -m venv venv
source venv/bin/activate
pip install flask werkzeug
export SECRET_KEY="dev"
python app.py
