-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-09-30 20:35:30 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g

DROP TABLE aplicacaoinsumo CASCADE CONSTRAINTS;

DROP TABLE fazenda CASCADE CONSTRAINTS;

DROP TABLE insumo CASCADE CONSTRAINTS;

DROP TABLE medicao CASCADE CONSTRAINTS;

DROP TABLE plantio CASCADE CONSTRAINTS;

DROP TABLE sensor CASCADE CONSTRAINTS;

DROP TABLE valores CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE aplicacaoinsumo (
    id_aplicacao       INTEGER NOT NULL,
    data_aplicacao     TIMESTAMP NOT NULL,
    medicao_id_valores INTEGER NOT NULL,
    insumo_id_insumo   INTEGER NOT NULL
);

ALTER TABLE aplicacaoinsumo ADD CONSTRAINT aplicação_pk PRIMARY KEY ( id_aplicacao );

CREATE TABLE fazenda (
    id_fazenda     INTEGER NOT NULL,
    nome_fazenda   VARCHAR2(255) NOT NULL,
    estado_fazenda VARCHAR2(2) NOT NULL,
    cidade_fazenda VARCHAR2(255) NOT NULL
);

ALTER TABLE fazenda ADD CONSTRAINT fazenda_pk PRIMARY KEY ( id_fazenda );

CREATE TABLE insumo (
    id_insumo   INTEGER NOT NULL,
    nome_insumo VARCHAR2(255) NOT NULL
);

CREATE UNIQUE INDEX insumo__idx ON
    insumo (
        id_insumo
    ASC );

ALTER TABLE insumo ADD CONSTRAINT insumo_pk PRIMARY KEY ( id_insumo );

CREATE TABLE medicao (
    id_valores         INTEGER NOT NULL,
    valor_medido       NUMBER NOT NULL,
    data_medicao       TIMESTAMP NOT NULL,
    plantio_id_plantio INTEGER NOT NULL,
    sensor_id_sensor   INTEGER NOT NULL
);

CREATE UNIQUE INDEX medicao__idxv1 ON
    medicao (
        id_valores
    ASC );

ALTER TABLE medicao ADD CONSTRAINT medicao_pk PRIMARY KEY ( id_valores );

CREATE TABLE plantio (
    id_plantio         INTEGER NOT NULL,
    cultura_plantio    VARCHAR2(255) NOT NULL,
    area_total         NUMBER NOT NULL,
    latitude_plantio   VARCHAR2(255) NOT NULL,
    longitude_plantio  VARCHAR2(255) NOT NULL,
    fazenda_id_fazenda INTEGER NOT NULL
);

ALTER TABLE plantio ADD CONSTRAINT plantio_pk PRIMARY KEY ( id_plantio );

CREATE TABLE sensor (
    id_sensor   INTEGER NOT NULL,
    nome_sensor VARCHAR2(255) NOT NULL
);

CREATE UNIQUE INDEX sensor__idx ON
    sensor (
        id_sensor
    ASC );

ALTER TABLE sensor ADD CONSTRAINT sensor_pk PRIMARY KEY ( id_sensor );

CREATE TABLE valores (
    id_valores             INTEGER NOT NULL,
    qtde_insumo_total      NUMBER NOT NULL,
    qtde_horas_gasta       NUMBER NOT NULL,
    qtde_insumo_metro      NUMBER NOT NULL,
    valor_custo_aplicacao  NUMBER NOT NULL,
    data_valores           TIMESTAMP NOT NULL,
    aplicacao_id_aplicacao INTEGER NOT NULL
);

CREATE UNIQUE INDEX valores__idx ON
    valores (
        aplicacao_id_aplicacao
    ASC );

ALTER TABLE valores ADD CONSTRAINT valores_pk PRIMARY KEY ( id_valores );

ALTER TABLE aplicacaoinsumo
    ADD CONSTRAINT aplicacao_insumo_fk FOREIGN KEY ( insumo_id_insumo )
        REFERENCES insumo ( id_insumo );

ALTER TABLE aplicacaoinsumo
    ADD CONSTRAINT aplicacao_medicao_fk FOREIGN KEY ( medicao_id_valores )
        REFERENCES medicao ( id_valores );

ALTER TABLE medicao
    ADD CONSTRAINT medicao_plantio_fk FOREIGN KEY ( plantio_id_plantio )
        REFERENCES plantio ( id_plantio );

ALTER TABLE medicao
    ADD CONSTRAINT medicao_sensor_fk FOREIGN KEY ( sensor_id_sensor )
        REFERENCES sensor ( id_sensor );

ALTER TABLE plantio
    ADD CONSTRAINT plantio_fazenda_fk FOREIGN KEY ( fazenda_id_fazenda )
        REFERENCES fazenda ( id_fazenda );

ALTER TABLE valores
    ADD CONSTRAINT valores_aplicacao_fk FOREIGN KEY ( aplicacao_id_aplicacao )
        REFERENCES aplicacaoinsumo ( id_aplicacao );