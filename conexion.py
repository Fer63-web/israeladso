import psycopg2

CONFIG = {
    "host": "localhost",          
    "port": "5432",              
    "dbname": "par_impar_db",     
    "user": "postgres",           
    "password": "israel12345",               
}


def obtener_conexion():
    return psycopg2.connect(**CONFIG)


def crear_tabla():
    """Crea la tabla de consultas si no existe."""
    conn = obtener_conexion()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS consultas (
                        id SERIAL PRIMARY KEY,
                        numero BIGINT NOT NULL,
                        resultado VARCHAR(5) NOT NULL,
                        fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                """)
    finally:
        conn.close()


def guardar_consulta(numero, resultado):
    """Guarda el número, si es par/impar y la fecha actual."""
    conn = obtener_conexion()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO consultas (numero, resultado) VALUES (%s, %s)",
                    (numero, resultado),
                )
    finally:
        conn.close()


if __name__ == "__main__":
    # Prueba rápida: python conexion.py
    crear_tabla()
    print("Conexión exitosa y tabla lista")
