import psycopg2 as psy

conn = psy.connect(dbname ='dbname', user = 'postgres', password= 'postgres')

cursour = conn.cursor()

#Open a cursor to perform database operations
cur = conn.cursor()

#drop any existing dbtable2 tables
cur.execute("DROP TABLE IF EXISTS dbtable2")

#Create tje dbtable2 table
cur.execute('''
            CREATE TABLE dbtable2 (
                id SERIAL PRIMARY KEY,
                completed BOOLEAN NOT NULL DEFAULT FALSE
                );
            ''')

cur.execute('''
            INSERT INTO dbtable2 (id, completed) VALUES (1, FALSE);
            ''')

#commit the transactions to the database
conn.commit()
cur.close()
conn.close()