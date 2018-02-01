# coding:utf-8
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user, login_user, login_required, UserMixin
from ..public import log_printer

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# 用户验证
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_message = u"Need login first"
login_manager.init_app(app)


# user class
class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(180), unique=True)

    def __init__(self, _id, _username, _email):
        self.user_id = _id
        self.username = _username
        self.password = _email

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def user_loader(_id):
    user = User.query.filter_by(user_id=_id).first()
    return user


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # first request
    if request.method == 'GET':
        return render_template('login.html')

    # POST
    _name = request.values.get('username')
    _password = request.values.get('password')

    # query from table
    user_object = User.query.filter_by(username=_name).first()

    # compare
    if user_object and user_object.password == _password:
        return redirect(url_for('/index'))
    else:
        return 'Bad login'


@app.route('/service')
@login_required
def service():
    return 'service'


@app.route('/about')
@login_required
def about():
    return 'about'


@app.route('/index')
@app.route('/')
@login_required
def index():
    return 'index'


@log_printer('Run server...')
def run_server():
    app.run(debug=True)


if __name__ == '__main__':
    run_server()
