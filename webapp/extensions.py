from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
bcrypt = Bcrypt()
bootstrap = Bootstrap()
db = SQLAlchemy()
loginmanager = LoginManager()