#Arquivo central para reunir as funcoes necessarias para serem aplicadas na smartfarm
import mysql.connector
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import time


class ComandCenter():

    def __init__(self,host_ip,user,password,database,tablename,tags):
        """
        Construtor central da classe responsavel
        por iniciar as variaveis do codigo
        e iniciar conexao com a base de dados

        Args:
            host_ip (str): ip do host da base de dados
            user (str): usuario para acessar a base de dados
            password (str): senha para acessar a base de dados
            database (str): nome da base de dados a ser acessada
            tablename (str): nome da tabela a ser modificada
            tags (dict): Dicionario dos sensores e valvulas do sistema
        """
        self.__host = host_ip
        self.__user = user
        self.__pw = password
        self.__dbpath = database
        self._table_name = tablename
        self._db = mysql.connector.connect (
            host=self.__host,
            user= self.__user,
            password= self.__pw,
            database= self.__dbpath
        )
        self._cursor = self._db.cursor()
        #TODO:(testar funcionamento do addr)
        addr = 'mysql+pymysql://'+self.__user + ':' + self.__pw + "@" + self.__host + '/' + self.__dbpath
        self._engine = sqlalchemy.create_engine(addr)

    def getData(self):
        """
        Obtem dados da DB e faz  print no console
        """
        df_index = pd.read_sql_query('select * from {self._table_name}',self._engine,index_col='id')
        print(df_index)

    def addData(self,data):
        #TODO: Adicionar o Lock.aquire() e Lock.release()
        str_cols = str_cols = ','.join(data.keys())
        str_values = []
        str_values.append([data[tag] for tag in data.keys()])
        sql = f'INSERT INTO {self._table_name} ({str_cols}) VALUES (%s, %s, %s, %s)'
        self._cursor.executemany(sql,str_values)
        print(self._cursor.rowcount, "Dados foram adicionados.")

    def removeData(self):
        pass

    def getValveState(self):
        pass

    def controleValvula(self):
        pass
