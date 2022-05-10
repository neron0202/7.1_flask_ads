from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app_var = Flask(__name__)
app_var.config.from_object(Config)
db = SQLAlchemy(app_var)
migrate = Migrate(app_var, db)

from app_pac.api import bp
app_var.register_blueprint(bp, url_prefix='/api')

from app_pac import routes, models