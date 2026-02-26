CREATE DATABASE imdb_db;
USE imdb_db;

CREATE TABLE imdb_top250 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_rank INT,
    title VARCHAR(255),
    year INT,
    rating FLOAT,
    votes INT,
    genres VARCHAR(255),
    duration VARCHAR(50),
    duration_minutes INT,
    certificate VARCHAR(50),
    directors VARCHAR(255),
    poster_url TEXT,
    movie_url TEXT,
    scrape_time DATETIME
);
CREATE TABLE rank1_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    movie_url TEXT,
    scrape_time DATETIME
);

show tables;
DESCRIBE imdb_top250;
DESCRIBE rank1_history;

SELECT COUNT(*) FROM imdb_top250;

INSERT INTO rank1_history (title, movie_url, scrape_time)
SELECT title, movie_url, scrape_time
FROM imdb_top250
WHERE movie_rank = 1
ORDER BY scrape_time DESC
LIMIT 1;

SELECT * FROM rank1_history;

SELECT title, scrape_time
FROM rank1_history
ORDER BY scrape_time DESC;

SELECT title, scrape_time
FROM imdb_top250
WHERE movie_rank = 1
ORDER BY scrape_time DESC
LIMIT 2;
DESCRIBE imdb_top250;