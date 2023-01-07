CREATE SCHEMA IF NOT EXISTS dimas_sis;

USE dimas_sis;

CREATE TABLE IF NOT EXISTS usuarios(
is_usuario INTEGER NOT NULL AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
usuario VARCHAR(16) NOT NULL UNIQUE,
senha VARCHAR(100) NOT NULL,
id_perfil INTEGER NOT NULL,
email VARCHAR(100) NOT NULL,

PRIMARY KEY (is_usuario)
);

CREATE TABLE IF NOT EXISTS perfil(
id_perfil INTEGER NOT NULL AUTO_INCREMENT,
perfil VARCHAR(20) UNIQUE,

PRIMARY KEY (id_perfil)
);

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
);

SHOW TABLES;