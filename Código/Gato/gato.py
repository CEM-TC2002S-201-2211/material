from flask import Flask, render_template, session, redirect

def crear_tablero():
    return [" " for i in range(9)]

app = Flask(__name__)
app.secret_key = "Esto no debería ir aquí"

@app.route("/")
def index():
    if "figura_jugador" not in session:
        return render_template("elegir_figura.html")

@app.route("/elegir_figura/<figura>")
def elegir_figura(figura):
    if figura in ["x", "o"]:
        session["tablero"] = crear_tablero()
        session["figura_jugador"] = figura
        session["figura_maquina"] = "o" if figura == "x" else "x"
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)