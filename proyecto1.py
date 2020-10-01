import psycopg2

#paso1! crear conexion
conn = psycopg2.connect(
    host = "localhost",
    database = "Drek",
    user = "postgres",
    password = "1234"
)

print(" connexion exitosa")

#paso2 crear cursor
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS ALUMNO")

sql = """CREATE TABLE ALUMNO(
    NOMBRE CHAR(100) NOT NULL,
    APELLIDO_PATERNO CHAR(100) NOT NULL,
    APELLIDO_MATERNO CHAR(100),
    EDAD INT,
    SEXO CHAR(1),
    CALIFICACION FLOAT
)"""

cursor.execute(sql)

conn.commit()

print("tabla creada con exito")

#paso Final
conn.close()