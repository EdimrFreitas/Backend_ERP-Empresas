from api_back_end import db

from Modulos.models import USUARIOS, PERFIL, PERMISSOES

models_tabelas = dict(
        usuarios=USUARIOS,
        perfil=PERFIL,
        permissoes=PERMISSOES,
    )


def create(tabela: str, infos: dict):
    new_info = models_tabelas[tabela](**infos)
    db.session.add(new_info)
    db.session.commit()
    return read(tabela=tabela, filtros=infos)


def read(tabela: str, filtros: dict):
    query = db.session.execute(db.select(models_tabelas[tabela.lower()]).filter_by(**filtros)).scalar()
    return query


def update():
    try:
        db.session.commit()
    except:
        return 'Falha na atualização'
    return 'Atualizado com sucesso'


def delete(obj: object):
    try:
        db.session.delete(obj)
    except:
        return 'Falha na deleção'
    db.session.commit()
    return 'Deletado com sucesso'

