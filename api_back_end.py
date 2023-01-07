import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

api = Flask("api_bd_erp")
api.config.from_pyfile(os.path.abspath('./Modulos/configs.py'))

db = SQLAlchemy(api)
bcrypto = Bcrypt

from Modulos.base import *

if __name__ == '__main__':
    ip_list = list()
    if os.name == 'posix':
        from netifaces import interfaces, ifaddresses, AF_INET
        ip_list = []
        for interface in interfaces():
            for link in ifaddresses(interface)[AF_INET]:
                ip_list.append(link['addr'])
    elif os.name == 'nt':
        ip_list.append('127.0.0.1')
    print(ip_list)
    api.run(host=ip_list[0], port=5000, debug=True)
