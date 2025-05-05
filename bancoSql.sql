create table Usuarios(
    id serial primary key,
	nome varchar(30) not null,
	email varchar(255) not null,
	senha varchar(30) not null,
	is_active boolean not null,
	datacriacao date not null,
	is_admin boolean not null
)
CREATE TABLE alunoModel (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(240) NOT NULL,
    datacriacao DATE DEFAULT CURRENT_DATE,
    bairro VARCHAR(60) NOT NULL,
    rua VARCHAR(60) NOT NULL,
    numero INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
)
CREATE TABLE pagamentos (
    id SERIAL PRIMARY KEY,
    aluno_id INT NOT NULL,
    datapagamento DATE,
    vencimento DATE,
    valor FLOAT NOT NULL,
    formadepagamento VARCHAR(30) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES Alunos(id)
);


insert into usuarios(nome, email, senha, is_active, datacriacao, is_admin) values('kaua','kaua123','123','True','2025-04-22','True')