<h3 align="center">Data Warehouse</h3>
<p align="center">
 Trabalho de Conclusão de Curso
 <br />
</p>


# About the Project

Neste projeto irei realizar a criação de uma base de dados em um modelo estrela utilizando um gerador de dados fictícos

# Criando um database

Primeiro fazer o download do SQL Server 2022 e configurar para acessar utilizando a autenticação do SQL Server, pode fazer o download da versão express.

Após a instalação, abra o SQL Server Management Studio. Conecte-se à instância do servidor que você pretende usar para seu banco de dados.

Uma vez conectado, no 'Object Explorer', clique com o botão direito do mouse no diretório "Databases". Selecione "New Database..." no menu suspenso. Uma janela "New Database" aparecerá.

Na janela "New Database", insira o nome do seu novo banco de dados.

# Criando as tabelas

Clone o repositório em seu servidor local, execute na seguinte ordem os arquivos .SQL

'''CRIANDO_TABELAS.sql'''

# Inserindo os dados nas tabelas

Execute o arquivo .SQL:

'''INSERT_NAS_TABELAS.sql'''

Para poder inserir nas tabelas dimAluno e fato, terá que executar o arquivo python Gerador.py, ele irá popular ambas as tabelas com dados fictícios.

# Criando a procedure

Para criar a procedure que retorna as matérias que determinado aluno pode realizar no próximo semestre, basta executar o arquivo '''Procedure.sql'''


# Contact
Matheus Bicalho [mbicalho.freitas@gmail.com]
Linkedin: [https://www.linkedin.com/in/matheus-bicalho-0a5835205/]
