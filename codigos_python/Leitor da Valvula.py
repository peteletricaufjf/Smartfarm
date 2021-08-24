import pandas as pd
import sqlalchemy
import mysql.connector
from sqlalchemy.orm import sessionmaker 
import time

engine = sqlalchemy.create_engine('mysql+pymysql://u165471834_admin:admin@92.249.44.52/u165471834_smartfarmdb') 

Session = sessionmaker(bind=engine)
session = Session()

teste_db = mysql.connector.connect(
  host="92.249.44.52",
  user="u165471834_admin",
  password="admin",
  database="u165471834_smartfarmdb"
)

mycursor = teste_db.cursor()

VALV = pd.read_sql_query('SELECT Valvula1 FROM dados WHERE id IN (SELECT MAX(id) FROM dados)',engine)
valv = str(VALV)
valv = valv.replace('   Valvula1\n0         ','')

if valv == '1':
    print('Válvula Aberta')

while valv == '1':
    VALV = pd.read_sql_query('SELECT Valvula1 FROM dados WHERE id IN (SELECT MAX(id) FROM dados)',engine)
    valv = str(VALV)
    valv = valv.replace('   Valvula1\n0         ','')
    #print(valv)
    time.sleep(1)
print('Válvula Fechada')

