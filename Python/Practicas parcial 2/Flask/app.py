from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig
from routes.cemento.cemento import appCemento
from routes.cheetos.cheetos import appCheetos
from routes.dulces.dulces import appDulces, appDulces2

app = Flask(__name__)
app.register_blueprint(appCemento)
app.register_blueprint(appCheetos)
app.register_blueprint(appDulces)
app.register_blueprint(appDulces2)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")
