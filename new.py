import pandas as pd
import base64
import psycopg2

df = pd.read_csv( "simple.csv")
#print(df)
#print(df.columns)
if 'Password' in df.columns:
    df['Password'] = df['Password'].apply(lambda x: base64.b64encode(x.encode("utf-8")).decode("utf-8"))
print(df)


conn = psycopg2.connect(
   database="test", user='mallesh', password='Mallesh@18', host='localhost', port= '3306'
)

cursor = conn.cursor()


cursor.execute("select version()")