import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://u165471834_admin:admin@92.249.44.52/u165471834_smartfarmdb') 
df_index = pd.read_sql_query('select * from dados',engine,index_col='id')
print(df_index)

