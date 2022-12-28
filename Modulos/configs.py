SECRET_KEY = 'ERP-Empresas'

SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD='mysql+mysqlconnector',
    usuario='root',
    senha='048Edimar258',
    servidor='127.0.0.1',
    database='dimas_sis'
)

