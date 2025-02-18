create user "kelompok4" identified by 'kelompok4';
Grant all privileges on *.* to "kelompok4";

create database warehouse;
use warehouse;

CREATE TABLE users (
    UserID VARCHAR(35) PRIMARY KEY,
    Password VARCHAR(50),
    Email VARCHAR(100),
    Nama VARCHAR(50),
    Gender VARCHAR(50),
    Usia Smallint,
    Pekerjaan VARCHAR(35),
    Hobi VARCHAR(100),
    Kota VARCHAR(50),
    RT smallint,
    RW smallint,
    Zipcode int,
    Latitude float,
    Longitude float,
    Nomor_Hp VARCHAR(20),
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stock (
    ID VARCHAR(15) PRIMARY KEY,
    Nama_produk VARCHAR(50) NOT NULL,
    kategori VARCHAR(50) NOT NULL,
    Unit Smallint NOT NULL,
    Harga_Satuan int NOT NULL
);

SET SQL_SAFE_UPDATES = 0;

insert into users (userid, password) values 
	('admin', '123');

insert into stock (id, nama_produk, kategori, unit, harga_satuan) values 
	('TEL-001', 'TV LED 42"', 'Televisi', 15, 2500000),
    ('LAP-001', 'Laptop Asus Tuf Gaming F15', "Laptop", 8, 17540000),
    ('LAP-002', 'Laptop Omen By HP 16', "Laptop", 3, 16780000),
    ('SMA-001', 'Smartphone Iphone 15', "Smartphone", 10, 13429000),
    ('KUL-001', 'Kulkas LG GN-B215SQMT', "Kulkas", 7, 3000000),
    ('MES-001', 'Mesin Cuci Panasonic NA-W76BBZ', "Mesin Cuci", 4, 2200000);
    
