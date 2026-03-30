import psycopg2

conn = psycopg2.connect(
    dbname="geo_db",
    user="postgres",
    password="Stusrt#9125",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM roubos;")

dados = cursor.fetchall()

print(dados)











