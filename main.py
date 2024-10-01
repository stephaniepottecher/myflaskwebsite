from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/titi')
def titi():
    return "J'aime le code"

@app.route('/menu')
def toto():
    return "Accueil, Page 1 Page 2"

app.run(debug=True)