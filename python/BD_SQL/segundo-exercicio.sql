CREATE DATABASE db_filmes_series;

CREATE TABLE IF NOT EXISTS Filmes(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    genre VARCHAR(255) NOT NULL,
    duration FLOAT NOT NULL,
    rating FLOAT NOT NULL,
    box_office FLOAT NOT NULL,
    cost FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS Series(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    creator VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    genre VARCHAR(255) NOT NULL,
    seasons INT NOT NULL,
    episodes INT NOT NULL,
    rating FLOAT NOT NULL,
    channel VARCHAR(255) NOT NULL,
    situation VARCHAR(255) NOT NULL
);

INSERT INTO Filmes (title, director, year, genre, duration, rating, box_office, cost) VALUES
('Mad Max: Fury Road', 'George Miller', 2015, 'Ação', 120, 8.1, 375200000.00, 150000000.00),
('Star Wars', 'George Lucas', 1977, 'Sci-fi', 121, 8.6, 775398007.00, 11000000.00),
('Super Mario Bros', 'Aaron Horvath, Michael Jelenic', 2023, 'Animação', 92, 7.3, 1300000000.00, 100000000.00),
('Pride and Prejudice', 'Joe Wright', 2005, 'Romance', 129, 7.8, 121147947.00, 28000000.00),
('Back to the Future', 'Robert Zemeckis', 1985, 'Sci-Fi', 116, 8.5, 381109762.00, 19000000.00),
('The Godfather', 'Francis Ford Coppola', 1972, 'Crime', 175, 9.2, 246120974.00, 6000000.00),
('The Lord of the Rings: The Return of the King', 'Peter Jackson', 2003, 'Fantasia', 201, 9.0, 1146030912.00, 94000000.00),
('Treasure Plane', 'Ron Clements, John Musker', 2002, 'Animação', 95, 7.2, 109578115.00, 140000000.00),
('Jurassic Park', 'Steven Spielberg', 1993, 'Aventura', 127, 8.1, 1043580597.00, 63000000.00),
('About Time', 'Richard Curtis', 2013, 'Romance', 123, 7.8, 87100000.00, 12000000.00),
('Transformers', 'Michael Bay', 2007, 'Ação', 144, 7.0, 709709780.00, 150000000.00);

INSERT INTO Series (title, creator, year, genre, seasons, episodes, rating, channel, situation) VALUES
('Breaking Bad', 'Vince Gilligan', 2008, 'Drama', 5, 62, 9.5, 'AMC', 'Finalizada'),
('Game of Thrones', 'David Benioff, D.B. Weiss', 2011, 'Fantasia', 8, 73, 9.3, 'HBO', 'Finalizada'),
('Stranger Things', 'The Duffer Brothers', 2016, 'Sci-fi', 4, 34, 8.7, 'Netflix', 'Em andamento'),
('Friends', 'David Crane, Marta Kauffman', 1994, 'Comédia', 10, 236, 8.9, 'NBC', 'Finalizada'),
('The Office', 'Greg Daniels', 2005, 'Comédia', 9, 201, 8.8, 'NBC', 'Finalizada'),
('Vikings', 'Michael Hirst', 2013, 'Drama Histórico', 6, 89, 8.5, 'History Channel', 'Finalizada'),
('Lost', 'J.J. Abrams, Damon Lindelof', 2004, 'Mistério', 6, 121, 8.4, 'ABC', 'Finalizada'),
('Once Upon a Time', 'Edward Kitsis, Adam Horowitz', 2011, 'Fantasia', 7, 155, 7.7, 'ABC', 'Finalizada'),
('The Mentalist', 'Bruno Heller', 2008, 'Crime', 7, 151, 8.1, 'CBS', 'Finalizada'),
('Star Trek', 'Gene Roddenberry', 1966, 'Sci-Fi', 3, 79, 8.4, 'NBC', 'Finalizada'),
('Cobra Kai', 'Josh Heald, Jon Hurwitz, Hayden Schlossberg', 2018, 'Ação', 5, 50, 8.6, 'Netflix', 'Em andamento');


-- Todos os filmes em ordem alfabética:
SELECT * FROM Filmes ORDER BY title ASC;

-- Todos os filmes com bilheteria acima de US$ 500 milhões:
SELECT * FROM Filmes WHERE box_office > 500000000.00;

-- Os IDs, nomes, anos de lançamento, gêneros, número de temporadas e episódios, avaliações e situações das séries, ordenadas da mais recente para a mais antiga:
SELECT id, title, year, genre, seasons, episodes, rating, situation FROM Series ORDER BY year DESC;

-- Todas as séries já finalizadas ordenadas da melhor avaliação para a pior:
SELECT * FROM Series WHERE situation = 'Finalizada' ORDER BY rating DESC;

-- Todos os filmes lançados antes dos anos 2000.
SELECT * FROM Filmes WHERE year < 2000;

-- Os títulos, anos de lançamento, gênero e avaliação dos filmes ordenados por sua avaliação pela crítica:
SELECT title, year, genre, rating FROM Series ORDER BY rating DESC;

-- A média de avaliação entre os filmes de até 2 horas e a média de avaliação dos filmes de mais de 2 horas (em colunas separadas).
SELECT 
    AVG(CASE WHEN duration <= 120 THEN rating END) AS avg_rating_short,
    AVG(CASE WHEN duration > 120 THEN rating END) AS avg_rating_long
FROM Filmes;

--  Nomes, anos e avaliações dos filmes ordenados pelo lucro (bilheteria - custo), incluindo o próprio lucro
SELECT 
    title, 
    year, 
    rating, 
    (box_office - cost) AS lucro
FROM Filmes
ORDER BY lucro DESC;