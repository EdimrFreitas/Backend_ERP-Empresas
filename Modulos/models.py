import sqlalchemy as sa

from api_back_end import db


class USUARIOS(db.Model):
    id_usuario = sa.Column(sa.Integer, nullable=False, primary_key=True)
    nome = sa.Column(sa.String(50), nullable=False)
    usuario = sa.Column(sa.String(16), nullable=False, unique=True)
    senha = sa.Column(sa.String(100), nullable=False)
    id_perfil = sa.Column(sa.Integer, nullable=False)
    email = sa.Column(sa.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

    def __deepcopy__(self, memodict={}):
        memodict['id_usuario'] = self.id_usuario
        memodict['nome'] = self.nome
        memodict['usuario'] = self.usuario
        memodict['senha'] = self.senha
        memodict['id_perfil'] = self.id_perfil
        memodict['email'] = self.email
        
        return memodict


class PERFIL(db.Model):
    id_perfil = sa.Column(sa.Integer, nullable=False, primary_key=True)
    perfil = sa.Column(sa.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.perfil

    def __deepcopy__(self, memodict={}):
        memodict['id_perfil'] = self.id_perfil
        memodict['perfil'] = self.perfil
        
        return memodict


class PERMISSOES(db.Model):
    id_perfil = sa.Column(sa.Integer, nullable=False, primary_key=True)
    cadastro_de_clientes = sa.Column(sa.Boolean, nullable=False)
    cadastro_de_produtos = sa.Column(sa.Boolean, nullable=False)
    cadastro_de_servicos = sa.Column(sa.Boolean, nullable=False)
    cadastro_de_usuarios = sa.Column(sa.Boolean, nullable=False)
    cadastro_de_estoque = sa.Column(sa.Boolean, nullable=False)
    vendas = sa.Column(sa.Boolean, nullable=False)
    clientes_por_regiao = sa.Column(sa.Boolean, nullable=False)
    compras_por_periodo = sa.Column(sa.Boolean, nullable=False)
    ranking_de_clientes = sa.Column(sa.Boolean, nullable=False)
    paretto = sa.Column(sa.Boolean, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.id_perfil
    
    def __deepcopy__(self, memodict={}):
        memodict['id_perfil'] = self.id_perfil
        memodict['cadastro_de_clientes'] = self.cadastro_de_clientes
        memodict['cadastro_de_produtos'] = self.cadastro_de_produtos
        memodict['cadastro_de_servicos'] = self.cadastro_de_servicos
        memodict['cadastro_de_usuarios'] = self.cadastro_de_usuarios
        memodict['cadastro_de_estoque'] = self.cadastro_de_estoque

        memodict['vendas'] = self.vendas

        memodict['clientes_por_regiao'] = self.clientes_por_regiao
        memodict['compras_por_periodo'] = self.compras_por_periodo
        memodict['ranking_de_clientes'] = self.ranking_de_clientes
        memodict['paretto'] = self.paretto
        
        return memodict
