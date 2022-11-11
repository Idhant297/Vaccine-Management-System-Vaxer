# create database
CREATE DATABASE IF NOT EXISTS vaxer;
# open the database
USE vaxer;
# for patient to login
CREATE TABLE IF NOT EXISTS login (email VARCHAR(50) PRIMARY KEY, pass VARCHAR(25) NOT NULL);
# a list of vaccine options
CREATE TABLE IF NOT EXISTS vaccines (vacc_id INT PRIMARY KEY, name VARCHAR(25) UNIQUE NOT NULL, status ENUM('Y', 'N'));
# a list of vaccination centers
CREATE TABLE IF NOT EXISTS centers (center_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, address VARCHAR(500) NOT NULL, district VARCHAR(50) NOT NULL, state VARCHAR(20) NOT NULL, pincode INT NOT NULL, UNIQUE(address, district, state));
# for patient to register for the vaccination
CREATE TABLE IF NOT EXISTS registration (uidai BIGINT PRIMARY KEY CHECK(uidai BETWEEN 999999999999999 AND 10000000000000000), first_name VARCHAR(25) NOT NULL, last_name VARCHAR(25) NOT NULL, age INT NOT NULL, gender ENUM('M','F'), vaccine INT REFERENCES vaccines ON DELETE RESTRICT ON UPDATE CASCADE, center INT REFERENCES centers ON DELETE RESTRICT ON UPDATE CASCADE, slot ENUM('1', '2', '3', '4'), email VARCHAR(50) UNIQUE REFERENCES login ON DELETE CASCADE ON UPDATE CASCADE);
# for records examination
CREATE TABLE IF NOT EXISTS records (uidai BIGINT, first_name VARCHAR(25), last_name VARCHAR(25), age INT, gender VARCHAR(1), vaccine_name VARCHAR(25), center_id INT, center_name VARCHAR(50), center_state VARCHAR(20), center_district VARCHAR(25), center_pincode INT);
