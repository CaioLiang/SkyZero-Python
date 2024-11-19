-- Drops
DROP TABLE tb_usuario;
DROP TABLE tb_login;
DROP TABLE tb_registro;

DROP SEQUENCE tb_usuario_id_usuario_seq;
DROP SEQUENCE tb_registro_id_registro_seq;

-- Tabela para armazenar os usuários (empresas)
CREATE TABLE tb_usuario (
    id_usuario       INTEGER NOT NULL,
    nomeEmpresa VARCHAR2(255) NOT NULL,
    email VARCHAR2(255) UNIQUE NOT NULL,
    cnpj VARCHAR2(18) UNIQUE NOT NULL
);

ALTER TABLE tb_usuario ADD CONSTRAINT tb_usuario_id_usuario_pk PRIMARY KEY ( id_usuario );

-- Tabela para armazenar os logins (associados aos usuários)
CREATE TABLE tb_login (
    id_usuario    INTEGER NOT NULL,
    login VARCHAR2(18) UNIQUE NOT NULL,
    senha VARCHAR2(255) NOT NULL
);

ALTER TABLE tb_login ADD CONSTRAINT tb_login_id_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE tb_login
    ADD CONSTRAINT tb_login_id_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES tb_usuario ( id_usuario );

-- Tabela para armazenar os registros (cálculos e histórico)
CREATE TABLE tb_registro (
    id_registro       INTEGER NOT NULL,
    id_usuario        INTEGER NOT NULL,
    tipo_aviao VARCHAR2(50) NOT NULL,
    distancia NUMBER NOT NULL,
    emissaoCalculada NUMBER NOT NULL,
    data_registro DATE NOT NULL
);

ALTER TABLE tb_registro ADD CONSTRAINT tb_registro_id_registro_pk PRIMARY KEY ( id_registro );

ALTER TABLE tb_registro
    ADD CONSTRAINT tb_registro_id_usuario_fk FOREIGN KEY (id_usuario)
        REFERENCES tb_usuario (id_usuario);

-- Sequences

CREATE SEQUENCE tb_usuario_id_usuario_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_usuario_id_usuario_trg BEFORE
    INSERT ON tb_usuario
    FOR EACH ROW
    WHEN (new.id_usuario IS NULL)
BEGIN
    :new.id_usuario := tb_usuario_id_usuario_seq.nextval;
END;

CREATE SEQUENCE tb_registro_id_registro_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_registro_id_registro_trg BEFORE
    INSERT ON tb_registro
    FOR EACH ROW
    WHEN (new.id_registro IS NULL)
BEGIN
    :new.id_registro := tb_registro_id_registro_seq.nextval;
END;