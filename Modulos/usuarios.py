from flask import request, session
from json import dumps

from api_back_end import api, db
from Modulos.models import USUARIOS, PERFIL, PERFIS


@api.route('/')
def desk():
    return '<div><h1>A API deve ser acessada apenas via software</h1></div>'


@api.route('/auth', methods=['POST', ])
def auth():
    print(f'Tentando logar com usuário {request.args.get("usuario")}')
    user_infos = dict()
    perfil_infos = dict()
    permissoes_infos = dict()
    
    user = db.session.execute(db.select(USUARIOS).filter_by(usuario=request.args.get('usuario'))).scalar()
    passw = request.args.get('senha') == user.senha

    if user and passw:
        perfil = db.session.execute(db.select(PERFIL).filter_by(id_perfil=user.id_perfil)).scalar()
        perfis = db.session.execute(db.select(PERFIS).filter_by(id_perfil=user.id_perfil)).scalar()

        user_infos['status'] = 'Conectado'
        user_infos['id_usuario'] = user.id_usuario
        user_infos['nome'] = user.nome
        user_infos['usuario'] = user.usuario
        user_infos['senha'] = user.senha
        user_infos['id_perfil'] = user.id_perfil
        user_infos['email'] = user.email

        perfil_infos['id_perfil'] = perfil.id_perfil
        perfil_infos['perfil'] = perfil.perfil

        permissoes_infos['id_perfil'] = perfis.id_perfil
        permissoes_infos['cadastro_de_clientes'] = perfis.cadastro_de_clientes
        permissoes_infos['cadastro_de_produtos'] = perfis.cadastro_de_produtos
        permissoes_infos['cadastro_de_servicos'] = perfis.cadastro_de_servicos
        permissoes_infos['cadastro_de_usuarios'] = perfis.cadastro_de_usuarios
        permissoes_infos['cadastro_de_estoque'] = perfis.cadastro_de_estoque

        permissoes_infos['vendas'] = perfis.vendas

        permissoes_infos['clientes_por_regiao'] = perfis.clientes_por_regiao
        permissoes_infos['compras_por_periodo'] = perfis.compras_por_periodo
        permissoes_infos['ranking_de_clientes'] = perfis.ranking_de_clientes
        permissoes_infos['paretto'] = perfis.paretto

    else:
        user_infos['status'] = 'Desconectado'
        user_infos['nome'] = 'Usuário ou senha inexistentes'

    infos = dict(user_infos=user_infos, perfil_infos=perfil_infos, permissoes_infos=permissoes_infos)
    json_obj = dumps(infos)
    # print(json_obj)
    return json_obj


@api.route('/logout')
def logout():
    session.pop(request.args.get('login', None))
    return 'Usuário deslogado'
