SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO PERFIL (ID_PERFIL, PERFIL)
VALUES
(1, "VENDEDOR"),
(2, "GESTOR"),
(3, "COMPRADOR"),
(4, "TOTAL");

INSERT INTO PERFIS
(ID_PERFIL, CADASTRO_DE_CLIENTES, Cadastro_de_produtos, Cadastro_de_SERVICOS, Cadastro_de_USUARIOS, Cadastro_de_estoque, VENDAS,	# 7 informações
CLIENTES_POR_REGIAO, COMPRAS_POR_PERIODO, RANKING_DE_CLIENTES, PARETTO)																# 4 informações
VALUES
(1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0),
(2, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1),
(3, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0),
(4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

select * from perfil;
select * from perfis;