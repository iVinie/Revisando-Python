CREATE DATABASE restaurante;

CREATE TABLE IF NOT EXISTS clientes(id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    endereco VARCHAR(255),
    data_cadastro DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS fornecedores(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    data_contratacao DATE NOT NULL DEFAULT CURRENT_DATE,
    observacao VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS lanches(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    preco FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos(
    id SERIAL PRIMARY KEY,
    mesa INT NOT NULL,
    data_e_hora VARCHAR(100),
    situacao BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS estoque(
    ID SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    quantidade FLOAT NOT NULL
);



-- Inserindo clientes
INSERT INTO clientes (nome, telefone, endereco) VALUES
('João Silva', '81999998888', 'Rua das Flores, 123'),
('Maria Oliveira', '81988887777', 'Av. Brasil, 456'),
('Carlos Santos', '81977776666', 'Rua do Sol, 789');

-- Inserindo fornecedores
INSERT INTO fornecedores (nome, telefone, email, observacao) VALUES
('Fornecedor Alimentos LTDA', '81911112222', 'contato@alimentos.com', 'Entrega semanal de carnes'),
('Bebidas & Cia', '81922223333', 'vendas@bebidascia.com', 'Fornecedor de refrigerantes e cervejas'),
('Pães do Recife', '81933334444', 'padaria@paesrecife.com', 'Entrega diária de pães');

-- Inserindo lanches
INSERT INTO lanches (nome, descricao, preco) VALUES
('X-Burger', 'Pão, carne, queijo e salada', 15.50),
('X-Frango', 'Pão, frango desfiado, queijo e salada', 17.00),
('Pizza Brotinho', 'Massa fina com queijo e tomate', 12.00);

-- Inserindo pedidos
INSERT INTO pedidos (mesa, data_e_hora, situacao) VALUES
(5, '2025-09-12 12:30', TRUE),
(3, '2025-09-12 13:15', FALSE),
(7, '2025-09-12 14:00', TRUE);

-- Inserindo estoque
INSERT INTO estoque (nome, categoria, quantidade) VALUES
('Carne bovina', 'Carnes', 20.5),
('Queijo mussarela', 'Laticínios', 15.0),
('Refrigerante Cola', 'Bebidas', 30.0);


-- Ver todos os clientes
SELECT * FROM clientes;

-- Ver todos os fornecedores
SELECT * FROM fornecedores;

-- Ver todos os lanches
SELECT * FROM lanches;

-- Ver todos os pedidos
SELECT * FROM pedidos;

-- Ver todo o estoque
SELECT * FROM estoque;


-- Retorna uma parte da tabela
SELECT id, nome, telefone FROM clientes;

-- Modificar o formato dos resultados, como o nome das colunas:
SELECT 
    id AS código,
    nome AS Lanche
FROM lanches;

--Outro comando importante do SQL e que é usado juntamente com o SELECT é o WHERE, que permite filtrarmos os resultados de acordo com uma condição:
SELECT * FROM lanches WHERE preco > 15;

--Também podemos usar o WHERE em conjunto com vários operadores para tornar os filtros mais elaborados:
-- Operador E (AND)
SELECT * FROM estoque WHERE categoria = 'Carnes' AND quantidade < 21;

-- Operador OU (OR)
SELECT * FROM estoque WHERE categoria = 'Carnes' OR quantidade < 21;

-- Operador IN para obter uma coluna pertencente a um conjunto
SELECT * FROM estoque WHERE categoria IN ('Carnes', 'Bebidas');

INSERT INTO clientes (nome, telefone, endereco) VALUES
  ('Nadeen Nassy', '(894) 3770999', '344 Comanche Circle'),
  ('Rufe Woolforde', '(876) 3190195', '1199 Garrison Junction'),
  ('Erl Bumphrey', '(828) 4611193', '279 Carey Way'),
  ('Libbey Allbut', '(780) 9682663', '0 Tennyson Pass'),
  ('Vick Saterthwait', '(858) 2707342', '8098 Carpenter Crossing'),
  ('Valma Leathlay', '(988) 1855788', '52 Pankratz Point'),
  ('Cathrin Balcers', '(854) 2908154', '58 Kipling Alley'),
  ('Fidelity Hurleston', '(169) 2896946', '99412 Nova Place'),
  ('Lane Beggio', '(102) 4251437', '625 Mcguire Place'),
  ('Abigale Ofield', '(414) 2709709', '4526 Ronald Regan Point'),
  ('Melisse Stappard', '(828) 1752818', '4 Sunnyside Lane'),
  ('Vito Breach', '(516) 2554781', '86120 Towne Court'),
  ('Jessalin Duckett', '(333) 6498842', '02 Artisan Center'),
  ('Bo Collie', '(163) 2032492', '0 Straubel Terrace'),
  ('Raphaela Krates', '(916) 8872820', '7798 3rd Street'),
  ('Lucian Draxford', '(827) 4937186', '739 Toban Way'),
  ('Philippa Sidon', '(475) 4933015', '64985 Clarendon Way'),
  ('Cordie Voce', '(937) 6629079', '767 Prairieview Road'),
  ('Easter Petrescu', '(135) 9137473', '32 Dayton Crossing');


-- Ordena pelo nome em ordem alfabética decrescente
SELECT * FROM clientes ORDER BY name DESC;

-- Ordena por telefone baseado nos primeiros dígitos em ordem crescente
SELECT * FROM clientes ORDER BY phone ASC;

-- Outro comando usado em conjunto com o SELECT é o de limitar os resultados:
SELECT * FROM clientes LIMIT 4;

-- E que usamos com frequência em conjunto com o comando de pular resultados OFFSET para criar um mecanismo de paginação:
SELECT * FROM clientes LIMIT 4 OFFSET 4;

-- Também podemos usar comandos para contagem de registros, média aritmética, soma, etc:
SELECT COUNT(id) AS Usuários FROM clientes;

SELECT SUM(quantidade) AS Total FROM estoque;

SELECT AVG(quantidade) AS Média FROM estoque;

-- Por fim, existem vários operadores mais avançados para serem utilizados em conjunto com o WHERE, podemos destacar o LIKE como sendo um dos mais interessantes:
-- Obs.: para o comando LIKE o caractere ‘%’ significa qualquer número de caracteres e o caractere ‘_’ representa um único caractere qualquer.

-- Obtém todos os clientes com nome começando com 'V'
SELECT * FROM clientes WHERE nome LIKE 'V%';

-- Obtém todos os clientes onde a segunda letra do nome é 'a'
SELECT * FROM clientes WHERE nome LIKE '_a%';

-- Obtém todos os clientes onde a última letra do nome é 'd'
SELECT * FROM clientes WHERE nome LIKE '%d';

-- Obtém todos os clientes que possuem 'an' em alguma parte do nome
SELECT * FROM clientes WHERE nome LIKE '%an%';

-- No PostgreSQL também temos o comando ILIKE, que funciona como o LIKE, porém é case-insensitive, ou seja, não diferencia maiúsculas e minúsculas:

-- Obtém os clientes com a letra 'B' em qualquer parte do nome
SELECT * FROM clientes WHERE nome LIKE '%B%';

-- Obtém os clientes com as letras 'B' ou 'b' em qualquer parte do nome
SELECT * FROM clientes WHERE nome ILIKE '%B%