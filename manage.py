from flask_script import Manager
from app import flask_app

manager = Manager(flask_app)

if __name__ == "__main__":
    manager.run(default_command='shell')
