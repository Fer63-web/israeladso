from flask import Flask, render_template, request

from conexion import crear_tabla, guardar_consulta

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def verificar_paridad():
    resultado = None
    numero = None
    error_bd = False

    if request.method == "POST":
        numero = int(request.form.get("numero"))
        resultado = "par" if numero % 2 == 0 else "impar"

        try:
            guardar_consulta(numero, resultado)
        except Exception as e:
            print("Error al guardar en la base de datos:", e)
            error_bd = True

    return render_template(
        "index.html", resultado=resultado, numero=numero, error_bd=error_bd
    )


if __name__ == "__main__":
    try:
        crear_tabla()
    except Exception as e:
        print("No se pudo crear la tabla:", e)
    app.run(debug=True, port=5001)
