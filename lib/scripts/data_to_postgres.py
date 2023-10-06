import psycopg2
import pandas as pd
from sqlalchemy import create_engine
  
  
conn_string = 'postgres://user:password@host/data1'
  
db = create_engine(conn_string)
conn = db.connect()
  
  
# our dataframe
data = {'Name': ['Tom', 'dick', 'harry'],
        'Age': [22, 21, 24]}
  
# Create DataFrame
df = pd.DataFrame(data)
df.to_sql('data', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  
sql1 = '''select * from data;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)
  
# conn.commit()
conn.close()