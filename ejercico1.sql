CREATE DATABASE

CREATE TABLE país(
    ID_País INT AUTO_INCREMENT,
    Nombre_País VARCHAR(11),
    NºHabitantes INT NOT NULL,
    PRIMARY KEY(ID_País),
);

CREATE TABLE clientes(
    ID_cliente VARCHAR(12) AUTO_INCREMENT NOT NULL,
    Apellido1 VARCHAR(12)NOT NULL,
    Apellido2 VARCHAR(12)NOT NULL,
    Dirección VARCHAR(11)NOT NULL,
    Carnet VARCHAR(2) DEFAULT "A" ENUM('B1','B2'),
    fecha de nacimiento DATE,
    ID_País INT,
    Telefono VARCHAR(9)NOT NULL,
    FOREIGN KEY (ID_País)  REFERENCES pais(ID_País),
);


INSERT INTO País ( ID_País , Nombre_País , NºHabitantes ) VALUES("3", "España" , "47.345.347");