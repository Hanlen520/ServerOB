# coding:utf-8
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, login_required
from ..public import log_printer


# in __init__.py
from . import app, login_manager
from user_control.user import User, LoginForm


@login_manager.user_loader
def user_loader(_id):
    user = User.query.filter_by(id=_id).first()
    return user


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # POST
        _name = form.username.data
        _password = form.password.data

        # query from table
        user_object = User.query.filter_by(username=_name).first()

        # compare
        if user_object and user_object.password == _password:
            login_user(user_object)
            return redirect(url_for('index'))
        else:
            return 'Bad login'

    # first request
    if request.method == 'GET':
        return render_template(
            'login.html',
            form=LoginForm()
        )


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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template(
        'login.html',
        form=LoginForm()
    )


@log_printer('Run server...')
def run_server():
    app.run(debug=True)


if __name__ == '__main__':
    run_server()
