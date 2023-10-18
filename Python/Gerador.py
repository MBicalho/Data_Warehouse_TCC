import random
import pandas as pd

import function_models as fm

import pyodbc
import datetime

import sqlalchemy

df_return = pd.DataFrame()

def connectDatabase():
    server = 'SEUHOSTNAME'
    database = 'SEUDATABASE'
    username = 'SEUUSERNAME'
    password = 'SEUPASSWORD'
    driver= '{ODBC Driver 17 for SQL Server}'

    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    conn = pyodbc.connect(connection_string)

    return conn
     


def insereFato(cursor):

    lista = [30, 60, 90]
    status_reprovado = [0]
    status_aprovado = [1]
    for i in range(1,69):
        for aluno_id in range(1, 20): # para cada aluno
            #for materia_id in range(1, 69): # para cada matéria
                #for tempo_id in range(1, 30): # para cada semestre
                    materia_id = random.randint(1,69)
                    tempo_id = random.randint(1,30)
                    horas_realizadas = random.choice(lista) # gera horas de estudo aleatórias
                    nota_materia = random.randint(0, 100) # gera nota aleatória
                    if nota_materia >= 60:
                        status_materia = 1
                    elif nota_materia < 60:
                        status_materia = 0
                    
                    sql = '''INSERT INTO CEFET_PRODUCAO.DBO.FatoHISTORICO_ESTUDANTIL (ID_ALUNO, ID_MATERIA, ID_TEMPO, HORAS_REALIZADAS, NOTA_MATERIA, STATUS_MATERIA) VALUES (?, ?, ?, ?, ?, ?)'''

                    cursor.execute(sql,aluno_id,materia_id,tempo_id,horas_realizadas,nota_materia, status_materia)
                    cursor.commit()


from faker import Faker
fake = Faker('pt_BR') # para nomes em português do Brasil


def insereAluno(N, cursor):
    lista = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    for i in range(1, N+1): # substitua N pelo número de alunos que você quer gerar
        nome = fake.name()
        ano_inicio = random.choice(lista)
        matricula = '{}00'.format(ano_inicio) + str(i)
        

        #print(f"INSERT INTO CEFET_PRODUCAO.DBO.DimALUNO (NOME_ALUNO, MATRICULA_ALUNO, ANO_INICIO) VALUES ('{nome}', '{matricula}', {ano_inicio});")

        sql = '''INSERT INTO CEFET_PRODUCAO.DBO.DimALUNO (NOME_ALUNO, MATRICULA_ALUNO, ANO_INICIO) VALUES (?, ?, ?)'''
        cursor.execute(sql,nome,matricula,ano_inicio)
        cursor.commit()

if __name__ == "__main__":

    #consultaAlunos()
    
    conn = connectDatabase()
    cursor = conn.cursor()
    insereHorario(cursor)
    # insereAluno(20, cursor)
    # insereFato(cursor)

    # fm.ConsultaAluno()

    #executar primeiro o insere aluno, depois preencher a fato

    # Então, recuperamos todos os alunos.
    

    conn.close()

