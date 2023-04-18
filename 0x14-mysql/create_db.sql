-- creates db "tyrell_corp" and table "nexus6" and adds one entry
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
    id INT,
    name VARCHAR(256) NOT NULL
);
INSERT INTO nexus6 (id, name) VALUES (1, "John");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';