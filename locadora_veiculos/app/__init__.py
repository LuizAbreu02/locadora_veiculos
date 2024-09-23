from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Cria a função para montar a aplicação e a retornar 

def create_app():
    app = Flask(__name__, static_folder='static')  

# Configuração banco de dados SQLite

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o método db para app

    db.init_app(app)

# Início: importamos e registramos o Blueprint
    from routes import bp
    app.register_blueprint(bp)
# Fim: importamos e registramos o Blueprint

    return app