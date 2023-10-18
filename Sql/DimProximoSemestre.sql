CREATE TABLE DimPROXIMOSEMESTRE (
	ID_HORARIO INT IDENTITY(1,1) PRIMARY KEY,
    ID_MATERIA INT,
    TIPO_MATERIA NVARCHAR(100),
    HORARIO NVARCHAR(100),
	ANO NVARCHAR(6)
);
DROP TABLE DimPROXIMOSEMESTRE
-- Semestre 1
INSERT INTO DimProximoSemestre VALUES (1, 1, 1, '2024.1'); -- CÁLCULO I
INSERT INTO DimProximoSemestre VALUES (2, 1, 2, '2024.1'); -- GEOMETRIA ANALÍTICA E ÁLGEBRA VETORIAL
INSERT INTO DimProximoSemestre VALUES (3, 1, 3, '2024.1'); -- INGLÊS INSTRUMENTAL
INSERT INTO DimProximoSemestre VALUES (4, 1, 4, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (5, 1, 5, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (6, 1, 6, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (7, 1, 7, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (8, 1, 8, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (9, 2, 9, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (10, 2, 1, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (11, 2, 2, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (12, 2, 3, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (13, 2, 4, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (14, 2, 5, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (15, 2, 6, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES I
INSERT INTO DimProximoSemestre VALUES (16, 2, 7, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (17, 3, 10, '2024.1'); -- PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (18, 3, 11, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (19, 3, 12, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (20, 3, 13, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (21, 3, 1, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (22, 3, 2, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (23, 3, 3, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (24, 3, 4, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (25, 4, 8, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (26, 4, 9, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (27, 4, 10, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (28, 4, 11, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (29, 4, 12, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (30, 4, 13, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (31, 4, 1, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (32, 4, 2, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (33, 4, 3, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (34, 5, 5, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (35, 5, 6, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (36, 5, 7, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (37, 5, 8, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (38, 5, 9, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (39, 5, 10, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (40, 5, 11, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (41, 6, 4, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (42, 6, 5, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (43, 6, 6, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (44, 6, 7, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (45, 6, 8, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (46, 6, 9, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (47, 6, 10, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (48, 6, 11, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (49, 7, 12, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (50, 7, 13, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (51, 7, 1, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (52, 7, 2, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (53, 7, 3, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (54, 7, 4, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (55, 7, 5, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (56, 8, 12, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (57, 8, 13, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (58, 8, 1, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (59, 8, 2, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (60, 8, 3, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (61, 8, 4, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (62, 9, 1, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (63, 9, 2, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (64, 9, 3, '2024.1'); -- LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES II
INSERT INTO DimProximoSemestre VALUES (65, 10, 1, '2024.1'); -- TRABALHO DE CONCLUSÃO DE CURSO II
INSERT INTO DimProximoSemestre VALUES (66, 10, 2, '2024.1'); -- CONTEXTO SOCIAL E PROFISSIONAL DA ENGENHARIA DE COMPUTAÇÃO
INSERT INTO DimProximoSemestre VALUES (67, 10, 3, '2024.1'); -- CONTEXTO SOCIAL E PROFISSIONAL DA ENGENHARIA DE COMPUTAÇÃO
INSERT INTO DimProximoSemestre VALUES (68, 10, 4, '2024.1'); -- CONTEXTO SOCIAL E PROFISSIONAL DA ENGENHARIA DE COMPUTAÇÃO
INSERT INTO DimProximoSemestre VALUES (69, 10, 5, '2024.1'); -- CONTEXTO SOCIAL E PROFISSIONAL DA ENGENHARIA DE COMPUTAÇÃO