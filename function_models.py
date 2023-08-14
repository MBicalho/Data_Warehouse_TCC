import time
import codecs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlalchemy as sa
from urllib.parse import quote
import paramiko as pk
import os
import shutil
import json
import ftplib as ftp
import pandas as pd
import datetime


timestr = time.strftime("%Y%m%d-%H%M%S")

def InfoDataAtualDetalhada():
    info = {
        'dia': timestr[6:8],
        'mes': timestr[4:6],
        'ano': timestr[0:4],
        'hora': timestr[9:11],
        'minuto': timestr[11:13],
        'segundo': timestr[13:],
        'data_completa': timestr[6:8] + '/' + timestr[4:6] + '/' + timestr[0:4],
        'hora_completa': timestr[9:11] + ':' + timestr[11:13] + ':' + timestr[13:],
        'data_hora': timestr[6:8] + '/' + timestr[4:6] + '/' + timestr[0:4] + ' ' + timestr[9:11] + ':' + timestr[11:13] + ':' + timestr[13:],
        'referencia': timestr[4:6] + '/' + timestr[0:4],
        'data_hora_arquivo_log': timestr[6:8] + '-' + timestr[4:6] + '-' + timestr[0:4] + '_' + timestr[9:11] + timestr[11:13] + timestr[13:],
        'data_padrao_bd': timestr[0:4] + '-' + timestr[4:6] + '-' + timestr[6:8]
    }

    return info

def ConnectionBD(database='', drive=''):
    """
    Banco = Ex: CTN_PRODUCAO.\n
    """
    server_name = 'LAPTOP-34OQSR9F\SQLEXPRESS'
    database = 'CEFET_PRODUCAO'
    username = 'admin'
    ps = 'admin'


    if not drive:
        drive = 'ODBC Driver 17 for SQL Server'

    connection_string = (
        f'Driver=' + drive + ';'
        f'Server=' + server_name + ';'
        f"Database=" + database + ';'
        f'UID=' + username + ';'
        f'PWD=' + ps + ';'
        #f"Trusted_Connection=no;"
        f"Trusted_Connection=yes;"
    )

    connection_url = sa.engine.URL.create(
        "mssql+pyodbc", 
        query={"odbc_connect": connection_string}
    )

    try:
        sqlcon = sa.create_engine(connection_url,fast_executemany=True)
        return(sqlcon)
    except Exception as ex:
        print(ex)
        return False, ex


def DescReferencia(month):
    """
    01 = 01 - JANEIRO;\n
    02 = 02 - FEVEREIRO;\n
    03 = 03 - MARÇO;\n
    04 = 04 - ABRIL;\n
    05 = 05 - MAIO;\n
    06 = 06 - JUNHO;\n
    07 = 07 - JULHO;\n
    08 = 08 - AGOSTO;\n
    09 = 09 - SETEMBRO;\n
    10 = 10 - OUTUBRO;\n
    11 = 11 - NOVEMBRO;\n
    12 = 12 - DEZEMBRO;\n
    """
    _month = int(month)
    if _month == 1:
        return(str(_month).zfill(2) + ' - JANEIRO')
    if _month == 2:
        return(str(_month).zfill(2) + ' - FEVEREIRO')
    if _month == 3:
        return(str(_month).zfill(2) + ' - MARÇO')
    if _month == 4:
        return(str(_month).zfill(2) + ' - ABRIL')
    if _month == 5:
        return(str(_month).zfill(2) + ' - MAIO')
    if _month == 6:
        return(str(_month).zfill(2) + ' - JUNHO')
    if _month == 7:
        return(str(_month).zfill(2) + ' - JULHO')
    if _month == 8:
        return(str(_month).zfill(2) + ' - AGOSTO')
    if _month == 9:
        return(str(_month).zfill(2) + ' - SETEMBRO')
    if _month == 10:
        return(str(_month).zfill(2) + ' - OUTUBRO')
    if _month == 11:
        return(str(_month).zfill(2) + ' - NOVEMBRO')
    if _month == 12:
        return(str(_month).zfill(2) + ' - DEZEMBRO')
    else:
        return DescReferencia(InfoDataAtualDetalhada()['mes'])

def CriaEstruturaPastas(pasta_principal, fonte, ano='', referencia=''):
    """
    *OBS*: O parâmetro pasta_principal deve ser enviado com duas barras (\\\\) no final.\n\n

    Se não for enviado nenhum parâmetro de ano, a função pega como referência o ano atual.\n\n

    O parâmetro referência pode ser enviado somente o numero do mês, por exemplo,
    se enviar 1 ou 01, será criada a pasta 01 - JANEIRO e assim por diante.\n
    Se não for enviado nenhum parâmetro, a função pega como referência o mês atual.\n


    """
    if not pasta_principal:
        print('Caminho da pasta principal é campo obrigatório!')
        return False

    if not fonte:
        print('Nome da fonte de arrecadação é campo obrigatório!')
        return False

    _ano = ano if ano else InfoDataAtualDetalhada()['ano']

    _referencia = DescReferencia(referencia) if referencia else DescReferencia(InfoDataAtualDetalhada()['mes'])

    try:
        if not os.path.exists(pasta_principal + fonte + '\\'):
            os.mkdir(pasta_principal + fonte + '\\')

        if not os.path.exists(pasta_principal + fonte + '\\' + _ano + '\\'):
            os.mkdir(pasta_principal + fonte + '\\' + _ano + '\\')

        if not os.path.exists(pasta_principal + fonte + '\\' + _ano + '\\' + _referencia + '\\'):
            os.mkdir(pasta_principal + fonte + '\\' + _ano + '\\' + _referencia + '\\')

        return(pasta_principal + fonte + '\\' + _ano + '\\' + _referencia + '\\')
    except Exception as ex:
        print(ex)
        return False


def CriaPastaAlternativa(caminho='', nome_pasta=''):
    if not caminho:
        return 'Caminho é parâmetro obrigatório'
    
    if not nome_pasta:
        return 'O nome da pasta a ser criada é parâmetro obrigatório'
    
    if not os.path.exists(caminho + nome_pasta + '\\'):
        os.mkdir(caminho + nome_pasta + '\\')
        return caminho + nome_pasta + '\\'
    else:
        return caminho + nome_pasta + '\\'


def LogMensagem(tipo, filename='', erro='', servidor='', mensagem=''):
    """
    Copia arquivo = CA;\n
    Sucesso ao copiar arquivo = SCA;\n
    Erro ao copiar arquivo = ECA;\n
    Mover arquivo = MA;\n
    Sucesso ao mover arquivo = SMA;\n
    Erro ao mover arquivo = EMA;\n
    Arquivo já eiste = AE;\n
    Conexão feita com sucesso FTP/SFTP = C_SFTP;\n
    Erro na conexão com o FTP/SFTP = E_SFTP;\n
    Arquivo ja existe e ja foi processado = A_PROCES;\n
    Erro ao processar o arquivo = EPC;\n
    Erro ao criar a estrutura de pastas = EEP;\n
    Erro ao descompactar o arquivo = EZIP;\n
    Mensagem personalizada = P;\n
    Informações do arquivo importadas para a base de dados = IAS;\n
    Início de processamento de arquivo = PROC_FILE;\n
    Sucesso ao processar arquivo = PROC_FILE_SUC;\n
    Erro ao processar o arquivo = PROC_FILE_ERROR;\n
    Final = FIM;\n
    """
    if tipo == 'CA':
        return '--> Copiando o arquivo ' + filename + ' para ' + servidor + '...\n'

    elif tipo == 'SCA':
        return '--> Arquivo ' + filename + ' copiado com sucesso para ' + servidor + '!!!\n'

    elif tipo == 'ECA':
        return '** Erro ao copiar o arquivo ' + filename + ' para o ' + servidor + '! Erro -> {0}**\n'.format(str(erro))

    elif tipo == 'MA':
        return '--> Movendo o arquivo ' + filename + ' para ' + servidor + '...\n'

    elif tipo == 'SMA':
        return '--> Arquivo ' + filename + ' movido com sucesso para ' + servidor + '!!!\n'

    elif tipo == 'EMA':
        return '** Erro ao mover o arquivo ' + filename + ' para o ' + servidor + '! Erro -> {0}**\n'.format(str(erro))

    elif tipo == 'AE':
        return ('O arquivo ' + filename + ' já existe no(a) ' + servidor + '!\n')

    elif tipo == 'C_SFTP':
        return 'Conexão com o servidor FTP/SFTP ' + servidor + ' feita com sucesso!\n'

    elif tipo == 'E_SFTP':
        return '** Falha ao conectar com o servidor FTP/SFTP ' + servidor + '** Erro -> {0}\n'.format(str(erro))

    elif tipo == 'A_PROCES':
        return 'O arquivo ' + filename + ' já existe no(a) ' + servidor + ' e já foi processado! O arquivo não foi copiado!\n'

    elif tipo == 'EPC':
        return '**Falha ao processar o arquivo ' + filename + '** Erro -> {0}\n'.format(str(erro))

    elif tipo == 'EEP':
        return '**Falha ao criar a estrutura de pastas** Erro -> {0}\n'.format(str(erro))

    elif tipo == 'P':
        return mensagem

    elif tipo == 'EZIP':
        return '**Falha ao descompactar o arquivo '+ filename + ' ** Erro -> {0}\n'.format(str(erro))

    elif tipo == 'IAS':
        return 'Informações do arquivo ' + filename + ' importadas com sucesso para a base de dados.\n'

    elif tipo == 'PROC_FILE':
        return 'Processando o arquivo ' + filename + '...\n'

    elif tipo == 'PROC_FILE_SUC':
        return 'Arquivo ' + filename + ' processado com sucesso!\n'
    
    elif tipo == 'PROC_FILE_ERROR':
        return 'Erro ao processar o arquivo ' + filename + '! ** Erro -> {0}\n'.format(str(erro))

    elif tipo == 'FIM':
        return '\n==================== Fim do processo! ====================\n\n'
    
    elif tipo == 'DIVISAO':
        return '\n===========================================================\n'

def CabecalhoLog(titulo):
    """
    Retorna o cabeçalho para preenchimento do arquivo de log ou string de alerta no e-mail.\n
    Data e hora de execução são preenchidos automaticamente.
    """
    _str = titulo + '\n'

    _str += 'Data: ' + InfoDataAtualDetalhada()['data_completa'] + '\n'

    _str += 'Hora: ' + InfoDataAtualDetalhada()['hora_completa'] + '\n\n'

    return _str

def CaminhoPadraoRetornoSIPARQ(complemento=''):
    """
    O caminho padrão de armazenamento de arquivos no SIPARQ é:\n
    \\192.168.254.251\Processamento de dados\ArquivoRetornoCobranca\ \n

    Se for necessário, pode enviar um complemento para ser inserido no caminho default.\n
    *OBS*: O complemento deve ser enviado com duas \\, inclusive no final. Não enviar as barras no inicio. \n

    EX: NEOENERGIA\\\\TESTE\\\\
    """
    path = '\\\\192.168.254.251\\Processamento de dados\\ArquivoRetornoCobranca\\'
    if complemento:
        return path + complemento
    else:
        path

def CaminhoPadraoEnvioSIPARQ(complemento=''):
    """
    O caminho padrão de armazenamento de arquivos no SIPARQ é:\n
    \\192.168.254.251\Processamento de dados\ArquivoEnvioCobranca\ \n

    Se for necessário, pode enviar um complemento para ser inserido no caminho default.\n
    *OBS*: O complemento deve ser enviado com duas \\, inclusive no final. Não enviar as barras no inicio. \n

    EX: NEOENERGIA\\\\TESTE\\\\
    """
    path = '\\\\192.168.254.251\\Processamento de dados\\ArquivoEnvioCobranca\\'
    if complemento:
        return path + complemento
    else:
        path


def CloseSFTP(ssh, sftp):
    sftp.close()
    ssh.close()

def CloseFTP(ftp):
    ftp['retorno'].quit()

def CriaArquivoLog(caminho, nome, escrever_arquivo=False, cabecalho=False, titulo_cabecalho='', info_arquivo=''):
    """
    O caminho para criação do arquivo de log ja deve estar padronizado e com duas barras no final.\n
    Nome também ja deve estar no padrão. Não precisa enviar a extensão do arquivo, pois será criado em .txt.
    """
    if not caminho:
        print('Caminho da pasta onde será criado o arquivo é campo obrigatório!')
        return False

    if not nome:
        print('Nome do arquivo é campo obrigatório!')
        return False

    if not escrever_arquivo:
        return open(r'' + caminho + nome + '.txt', 'w+')
    else:
        _file = open(r'' + caminho + nome + '.txt', 'w+')

        if cabecalho:
            _file.write(CabecalhoLog(titulo_cabecalho))
        
        _file.write(info_arquivo)

def FontesNeoserv(fonte):
    if fonte == 'P':
        return('CELPE')
    if fonte == 'B':
        return('COELBA')
    if fonte == 'R':
        return('COSERN')
    else:
        return('ELEKTRO')

def MoveFiles(origem, destino):
    shutil.move(origem, destino)

def SelectLisArquivosCodensa():
    sql = 'SELECT * FROM [CTN_COBRANCA].[DBO].[LISTA_ARQUIVOS_LIS_CODENSA]'

    lis = pd.read_sql(
                sql= sql,
                con= ConnectionBD('CTN_COBRANCA'))
    
    return pd.DataFrame(lis)

def ConsultaPendenciasEnel(id_concessionaria='', drive=''):
    sql = ("""SELECT ID_CONCESSIONARIA,
            CASE ITEM_PESQUISA WHEN 'F' THEN 1 WHEN 'O' THEN 2 WHEN 'A' THEN 3 WHEN 'R' THEN 6 END ID_CONSULTA,
            MAX(DT_PESQUISA) DT_PESQUISA,
            ITEM_PESQUISA,
            CASE ID_CONCESSIONARIA WHEN 703 THEN 'Celg' WHEN 57  THEN 'Coelce' WHEN 38 THEN 'Ampla' ELSE '' END AS CONCESSIONARIA
            FROM [controle].[RETORNO_ENEL]
            WHERE ID_CONCESSIONARIA = {}
            GROUP BY ID_CONCESSIONARIA, ITEM_PESQUISA
            ORDER BY CASE ITEM_PESQUISA WHEN 'F' THEN 1 WHEN 'O' THEN 2 WHEN 'A' THEN 3 END""").format(id_concessionaria)

    pendentes = pd.read_sql(sql= sql,
                            con= ConnectionBD(database='CTN_COBRANCA', drive=drive))
    
    return pd.DataFrame(pendentes)

def AjustaMatriculasArquivosLIS():
    retorno_requisicao = ''

    requisicao_bd = ConnectionBD('CTN_COBRANCA').connect()

    requisicao_bd.execution_options(autocommit=True)

    _retorno = requisicao_bd.execute('EXEC [CTN_COBRANCA].[cobranca_importa].[SP_ATUALIZA_MATRICULAS_LIS]')

    for row in _retorno:
        for i in row:
            retorno_requisicao += i
    
    return retorno_requisicao


def RemoveColumns():
    return ('Unnamed', 'COD_PLAN', 'COD_CARG', 'COD_TIP_PRODUC', 'COD_TIP_PRODUC', 'ID.1', 'CODIGO_CARGO', 'PRODUCTO', 'LLAVE', 'ID_RECAUDO', 'ANTIGÜEDAD', 'FACT_X_HACER', 'CAT_CUOT_FACT',
            'COD_TIP_PRODUC', 'FEC_PRIM_VENC', 'FEC_SEG_VENC', 'COD_CARGO')

def RegraFormatLis(lis):
    if lis == 'LIS001':
        return {
                'columns': ['CRMCONTRACTNUMBER', 'NIE', 'VASCONTRACTNUMBER', 'FECHA_INICIO_SUSCRIPCION', 'VALOR', 'ESTADO'],
                'columns_format': ['NIE', 'COD_PLAN', 'ID', 'FEC_INI', 'N_FACT', 'CUOT_X_FACT', 'CUOT_FACT', 'SALDO_INC', 'ANTIGUEDAD', 'SALD_FAC_X_PAGAR', 'SALD_FAC_X_CUOT', 'SALD_FAC_X_PAGAR_IVA', 'SALD_FAC_X_PAGAR_INT_MORA', 'TOT_PAG_CAPT', 'TOT_PAG_IVA', 'TOT_PAG_INT_MORA', 'SALD_X_FACT', 'FEC_FAC', 'CICLO', 'ESTADO', 'TOT_PAG', 'DIAS_MORA', 'COD_TIP_PRODUC', 'N_SERVICIO', 'ID_USAGE'],
                'variables': ['FECHA_INICIO_SUSCRIPCION']
        }
    
    elif lis == 'LIS003':
        return {
            'columns': ['NIE', 'VASCONTRACTNUMBER', 'VALOR', 'FEC_ING_PAG', 'FEC_CARG_ECO', 'N_SERVICIO', 'CRMCONTRACTNUMBER'],
            'columns_format': ['NIE', 'COD_PLAN', 'COD_CARG', 'ID', 'VALOR', 'FEC_ING_PAG', 'FEC_CARG_ECO', 'COD_TIP_PRODUC', 'N_SERVICIO', 'ID_USAGE'],
            'variables': ['FEC_ING_PAG', 'FEC_CARG_ECO']
        }
    
    elif lis == 'LIS004':
        return {
            'columns': ['NIE', 'VASCONTRACTNUMBER', 'NUMERO_FACTURA', 'VALOR', 'FECHA_FACTURA', 'CICLO_FACTURA', 'FEC_CREA_ECO', 'N_SERVICIO', 'FEC_PROCESO', 'CRMCONTRACTNUMBER'],
            'columns_format': ['NIE', 'COD_PLAN', 'ID', 'N_FACT', 'VALOR_FACT_ITEM', 'FEC_FACT', 'CICLO', 'COD_CARG', 'FEC_CREA_ECO', 'ANTIGUEDAD', 'FACT_X_HACER', 'CAT_CUOT_FACT', 'COD_TIP_PRODUC', 'N_SERVICIO', 'FEC_PRIM_VENC', 'FEC_SEG_VENC', 'FEC_PROCESO', 'ID_USAGE'],
            'variables': ['FECHA_FACTURA', 'FEC_CREA_ECO', 'FEC_PROCESO']
        }
    
    elif lis == 'LIS005':
        return {
            'columns': ['NIE', 'VASCONTRACTNUMBER', 'ANTIGUEDAD', 'NUMERO_FACTURA', 'VALOR', 'DIAS_MORA', 'FECHA_FACTURA', 'CRMCONTRACTNUMBER'],
            'variables': ['FECHA_FACTURA']
        }
    
    elif lis == 'LIS012':
        return {
            'columns': ['NIE', 'FEC_AJUSTE', 'CARG_REFAC', 'VALOR_INIC', 'VALOR_AJUST', 'VALOR_MODIF', 'N_AUTORIZ', 'SOCIO', 'ID', 'FEC_CARGUE_ECO', 'COD_PLAN', 'COD_TIP_PRODUC', 'N_SERVICIO', 'ID_USAGE'],
            'variables': ['FEC_AJUSTE', 'FEC_CARGUE_ECO']
        }
    
    elif lis == 'LIS013':
        return {
            'columns': ['NIE', 'FECHA_CANCELACION', 'VALOR', 'VASCONTRACTNUMBER', 'FECHA_INICIO_SUSCRIPCION', 'CRMCONTRACTNUMBER', 'ESTADO'],
            'columns_format': ['NIE', 'FEC_CANCELA', 'COD_CARG', 'COD_PLAN', 'VALOR_NO_PAG_ITEM', 'ID', 'ANTIGUEDAD', 'FACT_X_HACER', 'CANT_CUOT_FACT', 'VALOR_X_FACT_CUOT', 'FEC_CREAC', 'DIAS_MORA', 'COD_TIP_PRODUC', 'N_SERVICIO', 'FEC_PRIM_VENC', 'FEC_SEG_VENC', 'CICLO', 'ID_USAGE'],
            'variables': ['FECHA_INICIO_SUSCRIPCION']
        }
    
    elif lis == 'LIS014':
        return {
            'columns': ['NIE', 'COD_PLAN', 'FEC_CREA_ECO', 'ID', 'CUOTA_ECO', 'VALOR_CUOTA', 'IVA', 'COD_TIP_PRODUC', 'N_SERVICIO', 'ID_USAGE'],
            'variables': ['FEC_CREA_ECO']
        }
    
    elif lis == 'LIS016':
        return {
            'columns': ['NIE', 'COD_PLAN', 'COD_CARG', 'ID', 'VALOR', 'FEC_ING_PAG', 'FEC_CARG_ECO', 'COD_TIP_PRODUC', 'N_SERVICIO', 'ID_USAGE'],
            'variables': ['FEC_ING_PAG', 'FEC_CARG_ECO']
        }
    
    elif lis == 'ANULADOS':
        return {
            'columns': ['NIE', 'COD_PLAN', 'COD_CARG', 'ID', 'VALOR', 'FEC_ING_PAG', 'FEC_CARG_ECO', 'COD_TIP_PRODUC', 'N_SERVICIO', 'ESTADO_PAGO', 'FEC_ANULACION', 'ID_USAGE'],
            'variables': ['FEC_ING_PAG', 'FEC_CARG_ECO', 'FEC_ANULACION']
        }
    
    elif lis == 'FINALIZADOS':
        return {
            'columns': ['NRO_CUENTA', 'NRO_SERVICIO', 'NRO_ID_VENTA', 'MONTO_CUOTA', 'CODIGO_PLAN', 'DESCRIPCION', 'ID_STATE_ESTADO', 'AUDIT_DATE_FECHAFINALIZACION', 'CODE_SOCIO', 'ID_USAGE'],
            'variables': ['AUDIT_DATE_FECHAFINALIZACION']
        }
    
def CountTimeStart():
    return time.time()

def CountTimeEnd(start=''):
    return (time.time() - start)/60

def ReferenciaAtualAnterior():
    data_today = datetime.datetime.today()

    mes_anterior, ano_anterior = (data_today.month - 1, data_today.year) if data_today.month != 1 else (12, data_today.year - 1)
    mes_atual, ano_atual = (data_today.month, data_today.year)

    return mes_anterior, ano_anterior, mes_atual, ano_atual

def ConsultaAluno(drive=''):
    sql = ("""SELECT * FROM
              CEFET_PRODUCAO.DBO.DimREQUISITOS (NOLOCK)""")

    pendentes = pd.read_sql(sql= sql,
                            con= ConnectionBD(database='CEFET_PRODUCAO', drive=drive))
    
    return pd.DataFrame(pendentes)

if __name__ == '__main__':
    print(ConsultaAluno())
        