import psycopg2
import geopandas as gpd

conn = psycopg2.connect(
    dbname="base_roubos",
    user="postgres",
    password="Stusrt#9125",
    host="localhost",
    port="5432",
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM roubos WHERE bairro = 'PINHEIROS'")

query = "SELECT * FROM roubos WHERE bairro = 'PINHEIROS'"

gdf = gpd.read_postgis(query, conn, crs="EPSG=4326")

print(cursor.fetchall())