CREATE DATABASE db_concessionaria;

USE db_concessionaria;

CREATE TABLE IF NOT EXISTS clientes(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255) NOT NULL,
    email VARCHAR (100) UNIQUE,
    phone VARCHAR (20) NOT NULL,
);
#Alterar
ALTER TABLE clientes ADD COLUMN birthday;
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
ALTER TABLE clientes DROP COLUMN phone DROP NOT NULL;
#ALTER DATABASE db_concessionaria NAME novo_nome
#Para excluir o banco de dados ou qualquer coisa
DROP TABLE clientes;
DROP DATABASE db_concessionaria;