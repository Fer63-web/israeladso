import os
import psycopg2
 

import psycopg2

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="estudiantes",
        user="postgres",
        password="israel12345"
    )
def crear_tabla():
    """Crea la tabla de estudiantes si no existe."""
    conn = obtener_conexion()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS estudiantes (
                        id SERIAL PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        programa VARCHAR(100) NOT NULL,
                        nota1 NUMERIC(2,1) NOT NULL,
                        nota2 NUMERIC(2,1) NOT NULL,
                        nota3 NUMERIC(2,1) NOT NULL,
                        promedio NUMERIC(3,2) NOT NULL,
                        estado VARCHAR(20) NOT NULL,
                        fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                """)
    finally:
        conn.close()
 
 
def guardar_estudiante(estudiante):
    """Guarda el estudiante con su promedio, estado y la fecha actual."""
    conn = obtener_conexion()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO estudiantes
                        (nombre, programa, nota1, nota2, nota3, promedio, estado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        estudiante.nombre,
                        estudiante.programa,
                        estudiante.nota1,
                        estudiante.nota2,
                        estudiante.nota3,
                        round(estudiante.calcular_promedio(), 2),
                        estudiante.determinar_estado(),
                    ),
                )
    finally:
        conn.close()