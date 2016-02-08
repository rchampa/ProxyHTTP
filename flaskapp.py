__author__ = 'Ricardo'

print("welcome to the jungle")
from flask import Flask

app = Flask(__name__, static_url_path = "")
app.config.from_pyfile('flaskapp.cfg')

import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
#app.logger.setLevel(logging.ERROR)  # set the desired logging level here
app.logger.addHandler(file_handler)



from constants import MYSQL_URI
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Mock(db.Model):
    __tablename__ = "mocks"
    id_mock = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    method = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text,nullable=False)
    activado = db.Column(db.Boolean, nullable=False)
    creado_en = db.Column(db.DateTime)
    actualizado_en = db.Column(db.DateTime)
    __table_args__ = (db.UniqueConstraint(ip, port, url, name='_ip:port_url_uc'),{})

    def __init__(self, ip, port,method, url, body, creado_en):
        self.ip = ip
        self.port = port
        self.method = method
        self.url = url
        self.body = body
        self.activado = True
        self.creado_en = creado_en



db.create_all()

import restful
api = restful.init_rest(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response