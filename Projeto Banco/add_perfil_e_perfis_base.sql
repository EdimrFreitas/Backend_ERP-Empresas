SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO perfil (id_perfil, perfil)
VALUES
(1, 'Total'),
(2, 'Gestor'),
(3, 'Vendedor'),
(4, 'Comprador');

INSERT INTO permissoes
(ID_PERFIL, CADASTRO_DE_CLIENTES, Cadastro_de_produtos, Cadastro_de_SERVICOS, Cadastro_de_USUARIOS, Cadastro_de_estoque, VENDAS,	# 7 informações
CLIENTES_POR_REGIAO, COMPRAS_POR_PERIODO, RANKING_DE_CLIENTES, PARETTO)																# 4 informações
VALUES
(1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0),
(2, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1),
(3, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0),
(4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

select * from perfil;
select * from perfis;