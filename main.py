from flask import Flask, render_template, request, redirect, url_for, Response
import helper
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    items = helper.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    """
    Fügt ein neues Item mit Text und Datum hinzu.
    Das Datum wird automatisch auf das aktuelle Datum gesetzt.
    """
    text = request.form.get("text", "").strip()
    if text:
        # Automatisches Datum im Format YYYY-MM-DD
        today = datetime.today().strftime("%Y-%m-%d")
        helper.add(text, today)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index: int):
    """
    Schaltet den Erledigt-Status (isCompleted) um.
    """
    helper.update(index)
    return redirect(url_for("index"))


# ---------------------------
# 🧱 Erweiterung für LZ 4.1
# CSV-Export als Download
# ---------------------------
@app.route("/download")
def download_csv():
    """
    Gibt alle Items als CSV-Datei zurück.
    """
    csv_data = helper.get_csv()
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=zu-bbbearbeiten.csv"},
    )


if __name__ == "__main__":
    app.run(debug=True)
