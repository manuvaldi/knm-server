from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///networks.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Network(db.Model):

    __tablename__ = 'networks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    cidr = db.Column(db.String(100), nullable=False, unique=True)
    vlanid = db.Column(db.String(20), nullable=False, unique=True)
    options = db.Column(db.String(20), nullable=False)
    servers = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return '<Networks %r>' % self.name

class Server(db.Model):

    __tablename__ = 'servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False, unique=True)
    mac_address = db.Column(db.String(18), nullable=True)
    def __repr__(self):
        return '<Servers %r>' % self.name
