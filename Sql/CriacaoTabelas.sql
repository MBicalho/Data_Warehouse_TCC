-- Cria��o da Dimens�o Aluno
CREATE TABLE CEFET_PRODUCAO.DBO.DimALUNO (
    ID_ALUNO INT IDENTITY(1,1) PRIMARY KEY,
    NOME_ALUNO NVARCHAR(255) NOT NULL,
    MATRICULA_ALUNO NVARCHAR(50) NOT NULL,
    ANO_INICIO INT NOT NULL
);

-- Cria��o da Dimens�o Mat�ria
CREATE TABLE CEFET_PRODUCAO.DBO.DimMATERIA (
    ID_MATERIA INT IDENTITY(1,1) PRIMARY KEY,
    NOME_MATERIA NVARCHAR(255) NOT NULL,
    TIPO_MATERIA NVARCHAR(50) NOT NULL,
	HORA_AULA INT NOT NULL
);

-- Cria��o da Dimens�o Tempo
CREATE TABLE CEFET_PRODUCAO.DBO.DimTEMPO (
    ID_TEMPO INT IDENTITY(1,1) PRIMARY KEY,
    DATA NVARCHAR(6) NOT NULL,
    ANO INT NOT NULL,
    SEMESTRE INT NOT NULL,
);

-- Cria��o da Tabela de Fatos Hist�rico Estudantil
CREATE TABLE FatoHISTORICO_ESTUDANTIL (
    ID_FATO INT IDENTITY(1,1) PRIMARY KEY,
    ID_ALUNO INT FOREIGN KEY REFERENCES DimAluno(ID_Aluno),
    ID_MATERIA INT FOREIGN KEY REFERENCES DimMateria(ID_Materia),
    ID_TEMPO INT FOREIGN KEY REFERENCES DimTempo(ID_Tempo),
    HORAS_REALIZADAS INT NOT NULL,
    --HORAS_PENDENTES INT NOT NULL,
    NOTA_MATERIA FLOAT,
    STATUS_MATERIA NVARCHAR(50) NOT NULL
);

CREATE TABLE DimStatus (
    ID_STATUS INT IDENTITY(0,1) PRIMARY KEY,
    STATUS NVARCHAR(50) NOT NULL
);

CREATE TABLE DimREQUISITOS (
    ID_REQUISITO INT IDENTITY(1,1) PRIMARY KEY,
    ID_MATERIA INT FOREIGN KEY REFERENCES DimMateria(ID_Materia),
	PRE_REQUISITO INT,
	CO_REQUISITO INT
);

DROP TABLE FatoHISTORICO_ESTUDANTIL
DROP TABLE DBO.DimTEMPO
DROP TABLE DimMATERIA
DROP TABLE DBO.DimALUNO
DROP TABLE DimStatus
DROP TABLE DimREQUISITOS

INSERT INTO CEFET_PRODUCAO.DBO.DimStatus (STATUS) VALUES ('Reprovado'),
('Aprovado')

INSERT INTO CEFET_PRODUCAO.DBO.DimALUNO (NOME_ALUNO, MATRICULA_ALUNO, ANO_INICIO) VALUES ('Matheus Bicalho de Freitas', '201717060129', '2017')
INSERT INTO CEFET_PRODUCAO.DBO.DimMATERIA(NOME_MATERIA, TIPO_MATERIA) VALUES ('Calculo 1', '1')
INSERT INTO CEFET_PRODUCAO.DBO.DimTEMPO(DATA, ANO, SEMESTRE) VALUES ('2023.2', 2023, 2)
INSERT INTO CEFET_PRODUCAO.DBO.FatoHISTORICO_ESTUDANTIL(ID_ALUNO, ID_MATERIA, ID_TEMPO, HORAS_REALIZADAS, HORAS_PENDENTES, NOTA_MATERIA, STATUS_MATERIA) VALUES (1, 1, 1, 3060, 360, 64, 1)


SELECT * FROM
CEFET_PRODUCAO.DBO.DimTEMPO (NOLOCK)

SELECT * FROM
CEFET_PRODUCAO.DBO.DimMateria (NOLOCK)

SELECT * FROM
CEFET_PRODUCAO.DBO.DIMALUNO (NOLOCK)

SELECT * FROM
CEFET_PRODUCAO.DBO.DIMSTATUS (NOLOCK)



SELECT C.* FROM
CEFET_PRODUCAO.DBO.DimALUNO A
JOIN CEFET_PRODUCAO.DBO.FatoHISTORICO_ESTUDANTIL B ON A.ID_ALUNO = B.ID_ALUNO
JOIN CEFET_PRODUCAO.DBO.DimMATERIA C ON B.ID_MATERIA = C.ID_MATERIA
WHERE A.ID_ALUNO = 1

INSERT INTO CEFET_PRODUCAO.DBO.FatoHISTORICO_ESTUDANTIL(ID_ALUNO, 
ID_MATERIA, 
ID_TEMPO, 
HORAS_REALIZADAS, 
NOTA_MATERIA, 
STATUS_MATERIA)
VALUES
(1, 1, 17, 90, 46, 0),
(1, 2, 17, 90, 64, 1),
(1, 3, 17, 30, 76, 1),
(1, 4, 17, 30, 61, 1),
(1, 5, 17, 30, 61, 1),
(1, 6, 17, 30, 90, 1),
(1, 7, 17, 30, 82, 1),
(1, 8, 17, 30, 80, 1),
(1, 1, 18, 90, 64, 1),
(1, 9, 18, 30, 12, 3),
(1, 10, 18, 30, 12, 3)

SELECT D.NOME_ALUNO, B.DATA, C.NOME_MATERIA, A.NOTA_MATERIA, A.STATUS_MATERIA, E.STATUS, C.HORA_AULA FROM
CEFET_PRODUCAO.DBO.FatoHISTORICO_ESTUDANTIL (NOLOCK) A
JOIN CEFET_PRODUCAO.DBO.DimTEMPO (NOLOCK) B ON A.ID_TEMPO = B.ID_TEMPO
JOIN CEFET_PRODUCAO.DBO.DimMateria (NOLOCK) C ON C.ID_MATERIA = A.ID_MATERIA
JOIN CEFET_PRODUCAO.DBO.DimAluno (NOLOCK) D ON D.ID_ALUNO = A.ID_ALUNO
JOIN CEFET_PRODUCAO.DBO.DimStatus (NOLOCK) E ON E.ID_STATUS = A.STATUS_MATERIA
WHERE 1=1--A.NOTA_MATERIA > 60
AND D.NOME_ALUNO = 'Bruna Carvalho'


SELECT A.ID_MATERIA, B.NOME_MATERIA MATERIA, C.NOME_MATERIA PRE_REQUISITO, D.NOME_MATERIA CO_REQUISITO FROM
DIMREQUISITOS A
JOIN DIMMATERIA B ON A.ID_MATERIA = B.ID_MATERIA
JOIN DIMMATERIA C ON A.PRE_REQUISITO = C.ID_MATERIA
JOIN DIMMATERIA D ON A.CO_REQUISITO = D.ID_MATERIA
WHERE B.TIPO_MATERIA = 3

SELECT * FROM
DIMREQUISITOS (NOLOCK)

SELECT * FROM
DIMTEMPO

SELECT * FROM
DIMALUNO

SELECT * FROM
DIMMATERIA

SELECT * FROM
FATOHISTORICO_ESTUDANTIL

SELECT *
FROM DIMSTATUS

SELECT DISTINCT A.*, B.DATA FROM
DIMALUNO (NOLOCK) A
JOIN DIMTEMPO (NOLOCK) B ON A.ANO_INICIO = ANO
JOIN DIM
WHERE B.DATA LIKE '%.1'

CREATE TABLE CEFET_PRODUCAO.DBO.GRADE_2024_1 (
    ID_MATERIA INT PRIMARY KEY,
    TIPO NVARCHAR(50) NOT NULL,
    CONCORRENTE INT
);