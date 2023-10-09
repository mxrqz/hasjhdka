from flask import Flask, render_template, request
from flask import Flask, send_from_directory
import pyautogui

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("mediaKeys.html")


@app.route("/icon.ico")
def favicon():
    return send_from_directory(
        app.root_path, "icon.ico", mimetype="image/vnd.microsoft.icon"
    )


@app.route("/simular-tecla", methods=["POST"])
def simular_tecla():
    tecla = request.form["tecla"]
    pyautogui.press(tecla)
    print(tecla)
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0")
