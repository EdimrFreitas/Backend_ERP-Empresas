from api_back_end import db


class USUARIOS(db.Model):
    id_usuario = db.Column(db.Integer, nullable=False, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(16), nullable=False, unique=True)
    senha = db.Column(db.String(32), nullable=False)
    id_perfil = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.username


class PERFIL(db.Model):
    id_perfil = db.Column(db.Integer, nullable=False, primary_key=True)
    perfil = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.perfil


class PERFIS(db.Model):
    id_perfil = db.Column(db.Integer, nullable=False, primary_key=True)
    cadastro_de_clientes = db.Column(db.Boolean, nullable=False)
    cadastro_de_produtos = db.Column(db.Boolean, nullable=False)
    cadastro_de_servicos = db.Column(db.Boolean, nullable=False)
    cadastro_de_usuarios = db.Column(db.Boolean, nullable=False)
    cadastro_de_estoque = db.Column(db.Boolean, nullable=False)
    vendas = db.Column(db.Boolean, nullable=False)
    clientes_por_regiao = db.Column(db.Boolean, nullable=False)
    compras_por_periodo = db.Column(db.Boolean, nullable=False)
    ranking_de_clientes = db.Column(db.Boolean, nullable=False)
    paretto = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.id_perfil
