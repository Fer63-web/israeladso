import psycopg2

CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "adivina_numero",   # el nombre de la base que creaste en pgAdmin
    "user": "postgres",
    "password": "israel12345",
}


def obtener_conexion():
    return psycopg2.connect(**CONFIG)


def crear_tabla():
    conn = obtener_conexion()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS partidas (
                        id SERIAL PRIMARY KEY,
                        intentos INTEGER NOT NULL,
                        fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                """)
    finally:
        conn.close()


def guardar_partida(intentos):
    conn = obtener_conexion()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO partidas (intentos) VALUES (%s)",
                    (intentos,),
                )
    finally:
        conn.close()