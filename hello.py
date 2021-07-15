from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/github-actions')
def hello_github_actions():
    return '<p>Hello, Github Actions!</p>'


@app.route('/digital-ocean')
def hello_digital_ocean():
    return '<p>Hello, Digital Ocean!</p>'


@app.route('/linux')
def hello_linux():
    return '<p>Hello, Linux!</p>'
