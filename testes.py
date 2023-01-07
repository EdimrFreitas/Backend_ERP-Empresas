from netifaces import interfaces, ifaddresses, AF_INET
ip_list = []
for interface in interfaces():
    try:
        for link in ifaddresses(interface)[AF_INET]:
            ip_list.append(link['addr'])
    except KeyError:
        pass

print(ip_list)










# from requests import Session
#
#
# class ConectorBD:
#     def __init__(self, ip='127.0.0.1', usuario: str = None, senha: str = None):
#         """
#         Ao iniciar o 'ConectorBD' será realizado o login no servidor e
#         serão armazenados informações importantes para as proximas requisições
#         :param ip: ip ou ddns do servidor, padrão 127.0.0.1
#         :param usuario: usuario para login
#         :param senha: senha para login
#         :return: sessao logada
#         """
#         self.__sessao = Session()
#         self.__ip = ip
#         self.__logar(usuario, senha)
#
#     @property
#     def __url_servidor(self):
#         return 'http://' + self.__ip + ':5000'
#
#     @__url_servidor.getter
#     def get_url_servidor(self):
#         return self.__url_servidor
#
#     def __logar(self, usuario: str, senha: str):
#         """
#         Realiza o login e armazena o usuário na sessão
#         :param usuario: usuario para login
#         :param senha: senha para login
#         """
#         url = self.get_url_servidor + '/auth'
#         payload = dict(usuario=usuario, senha=senha)
#
#         s = self.__sessao.get(url=url, json=payload)
#         json = s.json()
#         # print(json)
#
#         if json['user_infos']:
#             self.__sessao.params['login'] = usuario
#             # print(self.__sessao.params['login'])
#         else:
#             return 'Erro de usuário ou senha'
#
#     def consulta(self, tabela: str, filtros: dict):
#         """
#         Realiza consultas de informação, equivalente ao READ
#         :param tabela: tabela em que a informação será pesquisada
#         :param filtros: filtros a serem aplicados na tabela, exemplo: {'usuario': 'user1'}
#         :return: Json com as informações solicitadas
#         """
#         url = self.get_url_servidor + '/consulta'
#         payload = dict(tabela=tabela, filtros=filtros)
#
#         s = self.__sessao.get(url=url, json=payload)
#         return s.json()
#
#     def criar(self, tabela: str, infos: dict):
#         """
#         Cria informações não existentes no banco, como novo usuário, equivalente ao CREATE
#         :param tabela: tabela em que a informação será adicionada
#         :param infos: informações a serem adicionadas na tabela, deverá conter todas as informações da tabela
#         :return: Json com o status da solicitação
#         """
#         url = self.get_url_servidor + '/criar'
#         payload = dict(tabela=tabela, infos=infos)
#
#         s = self.__sessao.post(url=url, json=payload)
#         return s.json()
#
#     def delete(self, tabela: str, filtros: dict):
#         """
#         Deleta informações de uma determinada tabela
#         :param tabela: tabela da qual a informação será removida
#         :param filtros: filtros a serem aplicados na consulta da linha da tabela a ser removida, exemplo: {'usuario': 'user1'}
#         :return: Json com o status da solicitação
#         """
#         url = self.get_url_servidor + '/deletar'
#         payload = dict(tabela=tabela, filtros=filtros)
#
#         s = self.__sessao.delete(url=url, json=payload)
#         return s.json()
#
#     def update(self, tabela: str, id_atual: dict, atualizacao: dict):
#         """
#         Atualiza informação existente
#         :param tabela: tabela da qual a informação será atualizada
#         :param id_atual: id da informação a ser atualizada
#         :param atualizacao: informação a ser alterada, exemplo: {'usuario': 'user1'}
#         :return: Json com o status da solicitação
#         """
#         url = self.get_url_servidor + '/atualiza'
#         payload = dict(tabela=tabela, id_atual=id_atual, atualizacao=atualizacao)
#
#         s = self.__sessao.put(url=url, json=payload)
#         return s.json()
#
#     def logout(self):
#         """
#         realiza o logout desta sessao, caso não seja utilizada,
#         a sessao se fechará automáticamente depois de algumas horas
#         :return: retorna o status do logout
#         """
#         url = self.get_url_servidor + '/logout'
#         s = self.__sessao.get(url=url)
#         return s.text
#
#     def __str__(self):
#         return self.__sessao.params['login']
#
#     def __eq__(self, other):
#         return other == self.__sessao.params['login']
#
#
# if __name__ == '__main__':
#     def testes(tipo_teste: str, teste: bool):
#         if teste:
#             print(f'Teste de {tipo_teste}', 'ok...', sep='\t-->\t')
#         else:
#             print(f'Falha no teste de {tipo_teste}...')
#
#     usuario = 'Edimar'
#     senha = '123456'
#     login = ConectorBD(ip='127.0.0.1', usuario=usuario, senha=senha)
#     testes('login', login == 'Edimar')
#
#     novo_user_infos = dict(
#         nome='Teste de novo usuário',
#         usuario='teste',
#         senha='048258',
#         id_perfil='3',
#         email='teste@teste.com.br'
#     )
#     novo_user = login.criar(tabela='usuarios', infos=novo_user_infos)
#     testes('criação de usuário', novo_user['usuario'] == 'teste' or novo_user['usuario'] == 'Usuário existente')
#
#     info = login.consulta(tabela='usuarios', filtros={'usuario': 'teste'})
#     testes('consulta', info['usuario'] == 'teste')
#
#     atualizado = login.update(
#         tabela='usuarios', id_atual={'id_usuario': info['id_usuario']}, atualizacao={'senha': '258456'}
#     )
#     testes('atualização', atualizado['status'] == 'Atualizado com sucesso')
#
#     del_user = login.delete(tabela='usuarios', filtros={'usuario': 'teste'})
#     testes('deletar', del_user['status'] == 'Deletado com sucesso')
#
#     logoff = login.logout()
#     testes('logoff', logoff == 'Usuário deslogado')
