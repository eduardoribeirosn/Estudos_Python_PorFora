import geopandas as gpd
import psycopg2

conn = psycopg2.connect(
    dbname="geo_db",
    user="postgres",
    password="Stusrt#9125",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

query = "SELECT * FROM roubos"

# cursor.execute("SELECT * FROM roubos;")

gdf = gpd.read_postgis(query, conn, geom_col="localizacao")

# dados = cursor.fetchall()

print(gdf.head())











