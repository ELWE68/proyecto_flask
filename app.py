from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "¡Hola Flask!"


@app.route("/about")
def about():
    return "Página About - Equipo de Programación"


if __name__ == "__main__":
    app.run(debug=True)
