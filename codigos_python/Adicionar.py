import pandas as pd
import sqlalchemy
import mysql.connector

engine = sqlalchemy.create_engine('mysql+pymysql://u165471834_admin:admin@92.249.44.52/u165471834_smartfarmdb') 

teste_db = mysql.connector.connect(
  host="92.249.44.52",
  user="u165471834_admin",
  password="admin",
  database="u165471834_smartfarmdb"
)

mycursor = teste_db.cursor()

sql = "INSERT INTO dados (Sensor1, Sensor2, Sensor3, Valvula1) VALUES (%s, %s, %s, %s)"
val = [
  ('1', '2', '3', '1')
]

mycursor.executemany(sql, val)
teste_db.commit()
print(mycursor.rowcount, "Dados foram adicionados.")

df_index = pd.read_sql_query('select * from dados',engine,index_col='id')
print(df_index)