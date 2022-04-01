
use browsergames;
 
CREATE TABLE game(
nome varchar(45) NOT NULL,
URL varchar(255) NOT NULL,
URLVideo varchar(255) DEFAULT NULL,
descricao varchar(255) NOT NULL,
categoria_nomeCategoria varchar(45) NOT NULL,
PRIMARY KEY (nome)
);