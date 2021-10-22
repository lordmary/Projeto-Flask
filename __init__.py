from flask import Flask #importando uma instância da classe flask
from flask_sqlalchemy import SQLAlchemy #vai traduzir python pra SQL
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__) #para o interpretador do Python saber se é arquivo principal, se for ele vai receber um valor "main"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' #uri do banco de dados. "/// pro local host"
db = SQLAlchemy(app) #recebe a instancia do flask. Chamei db por padrão (data base)
migrate = Migrate(app, db) #recebe app e banco de dados 

manager = Manager(app) #vai cuidar dos comandos pra inicializar a aplicação
manager.add_command('db', MigrateCommand )

from app.controllers import default
