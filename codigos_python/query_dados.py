# import pandas as pd
# import sqlalchemy

# engine = sqlalchemy.create_engine('mysql+pymysql://u165471834_admin:admin@92.249.44.52/u165471834_smartfarmdb') 
# df_index = pd.read_sql_query('select * from dados',engine,index_col='id')
# print(df_index)


"""
Testes para os codigos
"""
dict={
    'Sensor1': 1,
    'Sensor2': 2,
    'Senseor3': 3,
    'Valvula': 4
}

val = [
  ('1', '2', '3', '1')
]
print(dict)
str_cols = ','.join(dict.keys())
str_values=[]
str_values.append([dict[tag] for tag in dict.keys()])
print(len(str_values))
print(len(val))
