import psycopg2
import geopandas as gpd

conn = psycopg2.connect(
    dbname="geo_db",
    user="postgres",
    password="Stusrt#9125",
    host="localhost",
    port="5432",
)

cursor = conn.cursor()

# cursor.execute("CREATE TABLE roubos_desafio (id SERIAL PRIMARY KEY, descricao TEXT, localizacao GEOMETRY(Point, 4326))")

# cursor.execute("""INSERT INTO roubos_desafio (descricao, localizacao) VALUES
#                                                                    ('Roubo 1', ST_SetSRID(ST_MakePoint(-46.63, -23.55), 4326)),
#                                                                    ('Roubo 2', ST_SetSRID(ST_MakePoint(-46.66, -23.55), 4326)),
#                                                                    ('Roubo 3', ST_SetSRID(ST_MakePoint(-46.63, -23.50), 4326))""")
#
# gdf = gpd.GeoDataFrame(cursor.execute("SELECT * FROM roubos_desafio"))
# query = "SELECT * FROM roubos_desafio"
#
# gdf = gpd.read_postgis(query, conn, geom_col="localizacao")
#
# print(gdf)

cursor.execute("SELECT * FROM roubos_desafio rd, bairros_desafio bd WHERE ST_Within(rd.localizacao, bd.localizacao)")

print(cursor.fetchall())