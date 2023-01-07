SECRET_KEY = 'ERP-Empresas'

SGBD = 'mysql+mysqlconnector'
usuario = 'api-erp-empresas'
senha = 'ERP-Empresas!0512'
servidor = '127.0.0.1'
database = 'dimas_sis'
SQLALCHEMY_DATABASE_URI = f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'
