from flask import request, session, jsonify

from api_back_end import api
from Modulos.crud import read, create, delete, update


def checa_login(usuario):
    # print(f'sessão: {usuario not in session}, usuário: {session[usuario]}')
    if not session.get(usuario, False):
        return 'Necessário a autenticação'


@api.route('/')
def desk():
    return '<div><h1>A API deve ser acessada apenas via software</h1></div>'


# Login

@api.route('/auth')
def auth():
    # print(f'Tentando logar com usuário {request.args.get("usuario")}')

    user = read(tabela='usuarios', filtros={'usuario': request.json.get('usuario')})
    passw = request.json.get('senha') == user.senha

    if user and passw:
        # Armazena a sessao do usuário
        session[user.usuario.lower()] = user.usuario.lower()
        # print(session)

        # Realiza a busca das demais informações pertinentes ao usuário
        perfil = read(tabela='perfil', filtros={'id_perfil': user.id_perfil})
        permissoes = read(tabela='permissoes', filtros={'id_perfil': user.id_perfil})

        infos = {
            'user_infos': user.__deepcopy__(),
            'perfil_infos': perfil.__deepcopy__(),
            'permissoes_infos': permissoes.__deepcopy__()
        }
        return jsonify(infos)
    else:
        mal_sucedido = {'user_infos': {'usuario': False}}
        return jsonify(mal_sucedido)


@api.route('/logout')
def logout():
    # print(session)
    session.pop(request.args.get('login', None).lower())
    # print(session)
    return 'Usuário deslogado'


# CRUD

@api.route('/criar', methods=['POST', ])
def create_info():
    usuario = request.args.get('login').lower()
    checa_login(usuario=usuario)

    tabela = request.json.get('tabela')
    user_infos = request.json.get('infos')

    verifica_existente = read(tabela, user_infos)
    if verifica_existente:
        return jsonify({'usuario': 'Usuário existente'})

    new_user = create(tabela=tabela, infos=user_infos)
    return jsonify(new_user.__deepcopy__())


@api.route('/consulta')
def read_info():
    usuario = request.args.get('login').lower()
    checa_login(usuario=usuario)

    tabela = request.json.get('tabela')
    filtros = request.json.get('filtros')
    query = read(tabela=tabela, filtros=filtros)

    return jsonify(query.__deepcopy__())


@api.route('/deletar', methods=['DELETE', ])
def delete_info():
    tabela = request.json.get('tabela')
    filtros = request.json.get('filtros')

    verifica_informacao = read(tabela=tabela, filtros=filtros)
    if not verifica_informacao:
        return jsonify({'status': 'Informação inexistente'})
    query = delete(obj=verifica_informacao)

    return jsonify({'status': query})


@api.route('/atualiza', methods=['PUT', ])
def update_info():
    tabela = request.json.get('tabela')
    id_atual = request.json.get('id_atual')
    atualizacao = request.json.get('atualizacao')

    info_que_sera_atualizada = read(tabela=tabela, filtros=id_atual)
    if not info_que_sera_atualizada:
        return jsonify({'status': 'Informação inexistente'})

    for attr, value in atualizacao.items():
        setattr(info_que_sera_atualizada, attr, value)

    query = update()
    print(query)

    return jsonify({'status': query})
