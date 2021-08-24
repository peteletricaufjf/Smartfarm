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

i = int(input('Digite o começo do intervalo de id para excluir: '))
f = int(input('Digite o fim do intervalo de id para excluir: '))+1
j=0

for j in range (i,f):
    sql = "DELETE FROM dados WHERE id='"
    J = str(j)
    com = sql+J+ "'"
    mycursor.execute(com)
    teste_db.commit()
    
print("Linhas removidas.")

a = "ALTER TABLE dados AUTO_INCREMENT = "
I = str(i)
reset = a+I
mycursor.execute(reset)

df_index = pd.read_sql_query('select * from dados',engine,index_col='id')
print(df_index)
