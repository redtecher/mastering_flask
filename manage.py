from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

from main import app,db,User

manager = Manager(app)
manager.add_command("runserver",Server())

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)


@app.route('/')
def home():
    return '<h1>Hello World</h1>'

if __name__=='__main__':
    manager.run()