import sqlite3
# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("autosalon.sqlite")

con.executescript('''
    CREATE TABLE Brand (
	idBrand              INTEGER NOT NULL  PRIMARY KEY  ,
	brandName            VARCHAR(100) NOT NULL
 );

CREATE TABLE Buyer (
	idBuyer              INTEGER NOT NULL  PRIMARY KEY  ,
	buyerFio             VARCHAR(70) NOT NULL    ,
	buyerPassportSeries  VARCHAR(4) NOT NULL    ,
	buyerPassportNumber  VARCHAR(6) NOT NULL
 );

CREATE TABLE Manager (
	idManager            INTEGER NOT NULL  PRIMARY KEY  ,
	managerFio           VARCHAR(100) NOT NULL    ,
	baseRate             INTEGER NOT NULL    ,
	countOfDeals         INTEGER NOT NULL    ,
	countOfTestDrives    INTEGER NOT NULL    ,
	countOfInspection    INTEGER NOT NULL
 );

CREATE TABLE Manufactor (
	idManufactor         INTEGER NOT NULL  PRIMARY KEY  ,
	manufactorCountry    VARCHAR(100) NOT NULL
 );

CREATE TABLE RequestType (
	idType               INTEGER NOT NULL  PRIMARY KEY  ,
	requestName          VARCHAR(50) NOT NULL
 );

CREATE TABLE TechnicalData (
	idBodyType           INTEGER NOT NULL  PRIMARY KEY  ,
	numberOfDoors        INTEGER NOT NULL    ,
	numbersOfSeats       INTEGER NOT NULL    ,
	engineType           VARCHAR(50) NOT NULL    ,
	engineLocation       VARCHAR(50) NOT NULL    ,
	price                INTEGER NOT NULL
 );

CREATE TABLE Product (
	idProduct            INTEGER NOT NULL  PRIMARY KEY  ,
	idManufactor         INTEGER NOT NULL    ,
	avaliability         TINYINT NOT NULL    ,
	modelName            VARCHAR(100) NOT NULL    ,
	idBrand              INTEGER NOT NULL    ,
	idBodyType           INTEGER NOT NULL    ,
	FOREIGN KEY ( idBrand ) REFERENCES Brand( idBrand )  ,
	FOREIGN KEY ( idManufactor ) REFERENCES Manufactor( idManufactor )  ,
	FOREIGN KEY ( idBodyType ) REFERENCES TechnicalData( idBodyType )
 );

CREATE TABLE Request (
	idRequest            INTEGER NOT NULL  PRIMARY KEY  ,
	idManager            INTEGER NOT NULL    ,
	date                 DATE NOT NULL    ,
	idProduct            INTEGER NOT NULL    ,
	idType               INTEGER NOT NULL    ,
	idBuyer              INTEGER NOT NULL    ,
	FOREIGN KEY ( idBuyer ) REFERENCES Buyer( idBuyer )  ,
	FOREIGN KEY ( idType ) REFERENCES RequestType( idType )  ,
	FOREIGN KEY ( idProduct ) REFERENCES Product( idProduct )  ,
	FOREIGN KEY ( idManager ) REFERENCES Manager( idManager )
 );''')
# сохраняем информацию в базе данных
con.commit()