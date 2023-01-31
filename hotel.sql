CREATE TABLE hotel(
    Nombre VARCHAR(12),
    Direccion VARCHAR(15),
   	Teléfono VARCHAR(9),
    WEB VARCHAR (20),
    categoria VARCHAR(10),
    nºdehabitaciones INT,
    ID_Hotel INT,
    PRIMARY KEY (ID_Hotel)
    
);

CREATE TABLE Habitación(
    ID_Habitación INT,
    Precio INT,
    nºdehabitaciones ENUM(1-510),
    Capacidad INT,º
    Extras VARCHAR(10)
);

CREATE TABLE Reserva(
    fecha de la Reserva DATE,
    nombre del hotel  VARCHAR(15)
    fecha de entrada DATE
    numero de coches INT
);

