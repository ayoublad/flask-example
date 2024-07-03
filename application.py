from flask import Flask # type: ignore
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Je suis en stage chez Capgemini. [MAJ] Cela fait plus de deux semaines.'