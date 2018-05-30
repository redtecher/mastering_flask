from flask import Flask
from flask_script import Manager,Server
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
manager = Manager(app)
db = SQLAlchemy(app)
manager.add_command("runserver",Server())



class User(db.Model):
    id =db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
 
    def __init__(self, username):
        self.username=username
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
    



@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)


@app.route('/')
def home():
    return '<h1>Hello World</h1>'

if __name__=='__main__':
    manager.run()
