ALTER table PERFIS ADD constraint CE_PERFIS_PERFIL
foreign key (ID_PERFIL) 
references PERFIL (ID_PERFIL)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE USUARIOS ADD CONSTRAINT CE_USUARIOS_PERFIL
FOREIGN KEY (ID_PERFIL)
REFERENCES PERFIL (ID_PERFIL)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
