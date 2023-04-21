from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig
from routes.gabinete.gabinete import appGabinete

app = Flask(__name__)

app.register_blueprint(appGabinete)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")