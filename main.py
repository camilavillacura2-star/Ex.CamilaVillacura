from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def pagina_principal():
    return render_template("paginaPrincipal.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        precio_unitario = 9000
        total_sin = cantidad * precio_unitario

        if 18 <= edad <= 30:
            descuento_pct = 0.15
        elif edad > 30:
            descuento_pct = 0.25
        else:
            descuento_pct = 0.0

        monto_desc = total_sin * descuento_pct
        total_con = total_sin - monto_desc

        return render_template("Ejercicio1.html",
                               nombre=nombre,
                               total_sin=total_sin,
                               monto_desc=monto_desc,
                               total_con=total_con)

    return render_template("Ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("Ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
