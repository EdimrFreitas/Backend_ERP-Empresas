from getpass import getpass
from os import name

from flask_bcrypt import generate_password_hash
import mysql.connector
from mysql.connector import errorcode

import Modulos.configs
from Configurador.configs_linux import Linux

print("iniciando as configurações...", end='\n\n\n')

if name == 'posix':
    Linux()

print('Conectando...')
conn = None
print('Digite o usuário do banco de dados:', end=' ')
usuario_inicial = input()
senha_inicial = None
if name == 'nt':
    senha_inicial = input('Digite a senha: ')
elif name == 'posix':
    senha_inicial = getpass(f"Digite a senha do usuário '{usuario_inicial}'@'localhost': ")

try:
    conn = mysql.connector.connect(
        host='localhost',
        user=usuario_inicial,
        password=senha_inicial
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

print(f"Logado com usuário {usuario_inicial}@localhost...")
cursor = conn.cursor()

usuario_final = Modulos.configs.usuario
senha_final = Modulos.configs.senha
base_de_dados = Modulos.configs.database

# Cria o banco de dados e o usuário que será usado daqui para frente
print(f'Deletando a base de dados {base_de_dados} caso ela já exista...')
cursor.execute(F'DROP DATABASE IF EXISTS `{base_de_dados}`;')

print(f'Criando o banco de dados {base_de_dados}...')
cursor.execute(f'CREATE DATABASE IF NOT EXISTS `{base_de_dados}`')

cursor.execute(f'USE `{base_de_dados}`;')

print(f"Criando o {usuario_final}@'localhost' no banco {base_de_dados}...")
cursor.execute(f"CREATE USER IF NOT EXISTS '{usuario_final}'@'localhost';")
print(f"Usuário {usuario_final}...")
cursor.execute(f"GRANT ALL PRIVILEGES ON {base_de_dados}.* TO '{usuario_final}'@'localhost';")
cursor.execute(f"FLUSH PRIVILEGES;")

conn.commit()
cursor.close()
conn.close()

print(f"Deslogando do usuário {usuario_inicial}@'localhost'...")

conn = None

try:
    conn = mysql.connector.connect(
        host=Modulos.configs.servidor,
        user=usuario_final,
        password=senha_final
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

print(f"Logado como usuário {usuario_final}@'localhost'...")

cursor.execute(f'USE {base_de_dados}')

# Cria as tabelas
TABELAS = dict()
TABELAS['usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `id_usuario` INTEGER NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `usuario` varchar(16) NOT NULL UNIQUE,
      `senha` varchar(100) NOT NULL,
      `id_perfil` INTEGER NOT NULL,
      `email` varchar(100) NOT NULL,
      
      PRIMARY KEY (`id_usuario`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABELAS['perfil'] = ('''
      CREATE TABLE `perfil` (
      `id_perfil` INTEGER NOT NULL AUTO_INCREMENT,
      `perfil` VARCHAR(20) NOT NULL UNIQUE,
      
      PRIMARY KEY (`id_perfil`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABELAS['permissoes'] = (
    '''
    CREATE TABLE IF NOT EXISTS permissoes(
    id_perfil INTEGER NOT NULL auto_increment,
    cadastro_de_clientes BOOL NOT NULL,
    cadastro_de_produtos BOOL NOT NULL,
    cadastro_de_servicos BOOL NOT NULL,
    cadastro_de_usuarios BOOL NOT NULL,
    cadastro_de_estoque BOOL NOT NULL,
    vendas BOOL NOT NULL,
    clientes_por_regiao BOOL NOT NULL,
    compras_por_periodo BOOL NOT NULL,
    ranking_de_clientes BOOL NOT NULL,
    paretto BOOL NOT NULL,
    
    PRIMARY KEY (id_perfil)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''
)

for tabela_nome in TABELAS:
    tabela_sql = TABELAS[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')


# Insere perfis padrões
perfi_sql = 'INSERT INTO perfil (perfil) VALUES (%s)'
perfis = [
    ("Total", ), ("Gestor", ), ("Vendedor", ), ("Comprador", )
]
cursor.executemany(perfi_sql, perfis)

cursor.execute('select * from perfil')
print(' -------------  Perfis:  -------------')
for perfil in cursor.fetchall():
    print(perfil[1])


# Cria os níveis de permissões de cada PERFIL

permissoes_sql = """INSERT INTO permissoes 
(id_perfil, cadastro_de_clientes, cadastro_de_produtos, cadastro_de_servicos, cadastro_de_usuarios, cadastro_de_estoque,
vendas, clientes_por_regiao, compras_por_periodo, ranking_de_clientes, paretto)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
permissoes = [
    (1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0),
    (2, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1),
    (3, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0),
    (4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
]
cursor.executemany(permissoes_sql, permissoes)

cursor.execute('select * from permissoes')
print(' -------------  Permissoes:  -------------')
for permissao in cursor.fetchall():
    print(permissao)

# inserindo usuarios de teste
usuario_sql = 'INSERT INTO usuarios (nome, usuario, senha, id_perfil, email) VALUES (%s, %s, %s, %s, %s)'
usuarios = [
    ('Teste de permissao total', 'total', generate_password_hash('total').decode('utf-8'), 1, 'total@email.com'),
    ('Teste de permissao gestor', 'gestor', generate_password_hash('gestor').decode('utf-8'), 2, 'gestor@email.com'),
    ('Teste de permissao vendedor', 'vendedor', generate_password_hash('vendedor').decode('utf-8'), 3, 'vendedor@email.com'),
    ('Teste de permissao comprador', 'comprador', generate_password_hash('comprador').decode('utf-8'), 4, 'comprador@email.com'),
    ('Edimar Freitas de Sá', 'Edimar', '123456', 4, 'edimarfreitas95@gmail.com'),
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from usuarios')
print(' -------------  Usuarios:  -------------')
for usuario in cursor.fetchall():
    print(usuario[1])

# Cria as chaves estrangeiras entre as tabelas
print("Criando as chaves estrangeiras...")

cursor.execute(
f"""
ALTER TABLE permissoes ADD CONSTRAINT CE_PERMISSOES_PERFIL
FOREIGN KEY (id_perfil) 
REFERENCES perfil (id_perfil)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""
)

cursor.execute(
f"""
ALTER TABLE usuarios ADD CONSTRAINT CE_USUARIOS_PERFIL
FOREIGN KEY (id_perfil) 
REFERENCES perfil (id_perfil)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""
)

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()

print("Tudo certo e configurado, divirta-se.")
