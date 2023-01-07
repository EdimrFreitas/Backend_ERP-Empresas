SECRET_KEY = 'ERP-Empresas'

SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = '048Edimar258'
servidor = '127.0.0.1'
database = 'dimas_ss'
SQLALCHEMY_DATABASE_URI = f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'
