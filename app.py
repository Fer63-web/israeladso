from flask import Flask, render_template, request
import random

from conexion import crear_tabla, guardar_partida

app = Flask(__name__)

numero_secreto = random.randint(1, 100)
intentos = 0

# Crea la tabla al iniciar la aplicación
crear_tabla()


@app.route("/", methods=["GET", "POST"])
def inicio():
    global numero_secreto, intentos

    mensaje = ""
    intentos_mostrados = intentos

    if request.method == "POST":
        try:
            numero = int(request.form["numero"])

            if numero < 1 or numero > 100:
                mensaje = "El número debe estar entre 1 y 100."

            else:
                intentos += 1
                intentos_mostrados = intentos

                if numero < numero_secreto:
                    mensaje = "El número secreto es mayor."

                elif numero > numero_secreto:
                    mensaje = "El número secreto es menor."

                else:
                    mensaje = f"¡Correcto! El número era {numero}."
                    mensaje += f" Lo adivinaste en {intentos} intentos."

                    try:
                        guardar_partida(intentos)
                    except Exception as e:
                        print("Error al guardar en la base de datos:", e)
                        mensaje += " (No se pudo guardar la partida.)"

                    # Se reinicia el juego para no guardar la misma partida dos veces
                    numero_secreto = random.randint(1, 100)
                    intentos = 0

        except ValueError:
            mensaje = "Ingresa un número válido."

    return render_template(
        "index.html",
        mensaje=mensaje,
        intentos=intentos_mostrados
    )


@app.route("/reiniciar")
def reiniciar():
    global numero_secreto, intentos

    numero_secreto = random.randint(1, 100)
    intentos = 0

    return render_template(
        "index.html",
        mensaje="Nuevo número generado. ¡Intenta adivinarlo!",
        intentos=intentos
    )


if __name__ == "__main__":
    app.run(debug=True)