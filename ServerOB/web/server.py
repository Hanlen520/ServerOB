# coding:utf-8
from flask import Flask,render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from ..public import log_printer

app = Flask(__name__)
Bootstrap(app)

# 用户验证
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# http://blog.csdn.net/smalltankpy/article/details/53616053

@app.route('/')
def home():
    return render_template('login.html')

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
