from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    nom = "Shrek"
    lista = ["Burro", "Fiona", "Spider-man", "El hada madrina"]
    # lista = [f"<li>{i}</li>" for i in lista]
    return render_template("index.html",
                           nombre=nom, 
                           lista=lista)
    
@app.route("/path_param/<var>")
def path_param(var):
    valor1 = request.args.get("valor1")
    return render_template("index.html", 
                           nombre=var, 
                           lista=[valor1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)