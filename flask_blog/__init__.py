from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# generated from secrets module from secrets.token_hex method
app.config['SECRET_KEY'] = '903a926a0006ed0c810907d0daa38cd7'  # to avoid from harmful malwares
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# sqlachemy is an ORM object relation mapper with which we can create databse using python and cn workwith any db's
db =   SQLAlchemy(app=app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flask_blog import routes


