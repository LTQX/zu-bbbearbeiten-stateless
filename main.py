from flask import Flask, render_template, request, redirect, url_for
import helper

app = Flask(__name__)


@app.route("/")
def index():
    items = helper.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        # Falls dein helper.add nur (text) erwartet:
        helper.add(text)
        # Falls du die Variante mit Datum nutzt:
        # helper.add(text, date_str)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index: int):
    helper.update(index)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
