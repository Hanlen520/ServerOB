# coding:utf-8
from flask import Flask,render_template, request, url_for
from flask_bootstrap import Bootstrap
from ..public import log_printer

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('login.html', title_name = 'welcome')

@app.route('/service')
def service():
    return 'service'

@app.route('/about')
def about():
    return 'about'

@log_printer('Run server...')
def run_server():
    app.run(debug=True)

if __name__ == '__main__':
    run_server()
