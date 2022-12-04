from requests import Session


class ConectorBD:
    def __init__(self, ip='127.0.0.1', usuario=None, senha=None):
        self.__sessao = Session()
        self.__ip = ip
        self.__logar(usuario, senha)

    @property
    def __servidor(self):
        return 'http://' + self.__ip + ':5000'

    @__servidor.getter
    def get_servidor(self):
        return self.__servidor

    def __logar(self, usuario, senha):
        url = self.get_servidor + '/auth'

        payload = dict(usuario=usuario, senha=senha)

        s = self.__sessao.post(url=url, params=payload)

        if s.cookies:
            self.__sessao.params['login'] = usuario
        else:
            raise 'Erro de usuário ou senha'

    def consulta(self, tipo: str, filtros: list):
        url = self.get_servidor + '/consulta'

        payload = dict(tipo=tipo, filtros=filtros)

        return self.__sessao.get(url=url, json=payload).content

    def logout(self):
        url = self.get_servidor + '/logout'

        return self.__sessao.get(url=url).text


if __name__ == '__main__':
    usuario = 'Edimar'
    senha = '12345'
    login = ConectorBD(ip='127.0.0.1', usuario=usuario, senha=senha)

    # info = login.consulta(tipo='usuarios', filtros=['infos1', 'infos2'])
    # print(info)

    # logoff = login.logout()
    # print(logoff)
