from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from .. import db


# user class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(180), unique=True)

    def __init__(self, _id, _username, _email):
        self.id = _id
        self.username = _username
        self.password = _email

    def __repr__(self):
        return '<User %r>' % self.username


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])