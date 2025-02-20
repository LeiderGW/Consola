from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "clave_secreta_unica"

@app.route("/", methods=["GET", "POST"])
def index():
    if "color" not in session:
        session["color"] = "#000000"  # Color predeterminado (negro)

    if request.method == "POST":
        session["color"] = request.form["color"]  # Guarda el color en la sesión

    return render_template("index.html", color=session["color"])

if __name__ == "__main__":
    app.run(debug=True)
