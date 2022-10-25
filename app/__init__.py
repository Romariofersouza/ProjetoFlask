from flask import Flask, render_template
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

def pagina_nao_encontrada(e):
    mensagem = 'pagina em desenvolvimento ou não encontrada!'
    return render_template('erro.html', mensagem=mensagem), 404

app = Flask(__name__)
app.register_error_handler(404, pagina_nao_encontrada)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Para usar este aplicativo, é necessário fazer login!'


db = SQLAlchemy(app)
Migrate = Migrate(app, db)

from app. controllers import rotas
from app.models import modelos


