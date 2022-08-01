import psycopg2 as psy

conn = psy.connect(dbname ='dbname', user = 'postgres', password= 'postgres')

cursour = conn.cursor()

#Open a cursor to perform database operations
cur = conn.cursor()

#drop any existing dbtable2 tables
#cur.execute("DROP TABLE IF EXISTS dbtable2")

#Create tje dbtable2 table
#cur.execute('''
#            CREATE TABLE dbtable2 (
#                id SERIAL PRIMARY KEY,
#                completed BOOLEAN NOT NULL DEFAULT FALSE
#                );
#            ''')

#Insert new records into dbtable2 using string interpolation
#cur.execute('INSERT INTO dbtable2 (id, completed) VALUES (%s, %s);',\
#    (2,True))

SQL = 'INSERT INTO dbtable2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id':3,
    'completed':True
}
#cur.execute(SQL,data)

cur.execute('SELECT * FROM dbtable2')
result = cur.fetchall()
print(result)

result2 = cur.fetchone()
print('fetchone',result2)

result3 = cur.fetchmany(2)
print('fetchmany(2)',result3)

result4 = cur.fetchone()
print('fetchone',result4)

#commit the transactions to the database
conn.commit()
cur.close()
conn.close()