from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

api = Flask("api_bd_erp")
api.config.from_pyfile('./Modulos/configs.py')

db = SQLAlchemy(api)
bcrypto = Bcrypt

from Modulos.usuarios import *
# from Modulos.clientes import *

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=5000, debug=True)
