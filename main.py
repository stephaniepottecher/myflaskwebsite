from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/titi')
def titi():
    return "J'aime le code"

app.run(debug=True)