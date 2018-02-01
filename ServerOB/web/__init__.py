# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import config

# 初始化app
app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)


# 用户验证
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
