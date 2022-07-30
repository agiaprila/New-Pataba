from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bappeda.db'
app.config['SECRET_KEY'] = 'my-super-secret-key'

login_manager.login_view = 'login_page'
login_manager.login_message = 'Harap Login Dulu'
login_manager.login_message_category = 'warning'

from publication import routes
from publication.setda import routes_setda
from publication.dprd import routes_dprd