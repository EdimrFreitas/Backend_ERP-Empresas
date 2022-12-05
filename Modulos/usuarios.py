from flask import request, session

from api_back_end import api, db
from Modulos.models import Crm


@api.route('/')
def desk():
    return '<div><h1>API deve ser acessada apenas via software</h1></div>'


@api.route('/auth', methods=['POST', ])
def auth():
    print('entrou')
    user = db.session.execute(db.select(Crm).filter_by(username=request.args.get('usuario'))).scalar()
    senha = request.args.get('senha') == user.password
    if user and senha:
        session[user.username] = user.username
        return f'User logado: {session[user.username]}'
    else:
        return 'Usuário ou senha inválidos'


@api.route('/logout')
def logout():
    session.pop(request.args.get('login', None))
    return 'Usuário deslogado'
