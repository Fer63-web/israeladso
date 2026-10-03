from flask import Flask, render_template, request
 
from conexion import crear_tabla, guardar_estudiante
 
app = Flask(__name__)
 
 
class Estudiante:
    def __init__(self, nombre, programa, nota1, nota2, nota3):
        self.nombre = nombre
        self.programa = programa
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
 
    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
 
    def determinar_estado(self):
        promedio = self.calcular_promedio()
 
        if promedio >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"
 
 
@app.route("/", methods=["GET", "POST"])
def inicio():
 
    estudiante = None
    error_bd = False
 
    if request.method == "POST":
 
        nombre = request.form["nombre"]
        programa = request.form["programa"]
        nota1 = request.form["nota1"]
        nota2 = request.form["nota2"]
        nota3 = request.form["nota3"]
 
        estudiante = Estudiante(
            nombre,
            programa,
            nota1,
            nota2,
            nota3
        )
 
        try:
            guardar_estudiante(estudiante)
        except Exception as e:
            print("Error al guardar en la base de datos:", e)
            error_bd = True
 
    return render_template(
        "index.html",
        estudiante=estudiante,
        error_bd=error_bd
    )
 
 
if __name__ == "__main__":
    try:
        crear_tabla()
    except Exception as e:
        print("No se pudo crear la tabla:", e)
    app.run(debug=True)