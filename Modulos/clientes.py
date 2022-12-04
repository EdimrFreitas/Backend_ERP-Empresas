from flask import request, session

from api_back_end import api, db
from Modulos.models import Crm


@api.route('/consulta', methods=['POST', ])
def consulta():
    if request.args.get('login') not in session or not session[request.args.get('login')]:
        return 'Autenticação inválida'
    tipo = request.json.get('tipo')
    filtros = request.json.get('filtros')

    return f'{tipo}, {filtros}'
