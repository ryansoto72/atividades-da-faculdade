create database BD_sisAcademico;
#drop database BD_sisAcademico; Apaga o banco de dados
use BD_sisAcademico;
create table Aluno(
 rgm int not null,
 nome varchar(100) not null,
 rg varchar(20) not null,
 cpf varchar(11) not null unique,
 constraint pk_Aluno primary key (rgm)
 );
create table Curso(
 codico int not null,
 descricao varchar(100) not null,
 constraint pk_Curso primary key (codico)
 );

create table Telefone(
 codico int not null,
 numero varchar(20) not null unique,
 descricao varchar(100),
 ddd varchar(100) not null,
 constraint pk_Telefone primary key (codico)
);

create table Endereco(
 codico int not null,
 cidade varchar(50) not null,
 rua varchar(50) not null,
 numero_rua int not null,
 constraint pk_Endereco primary key (codico)
);

create table Diciplina(
 codico int not null,
 descricao varchar(100),
 constraint pk_Diciplina primary key (codico)
);

create table Aluno_curso(
codico int not null,
data_inicio date,
data_fim date,
constraint pk_Aluno_curso primary key (codico)
);

create table Aluno_DIciplina(
codico int not null,
data_inicio date,
data_fim date,
constraint pk_Aluno_diciplina primary key (codico)
);