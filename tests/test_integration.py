# tests/test_integration.py
import pytest
from datetime import datetime

from main import app as flask_app
import helper


@pytest.fixture()
def client():
    # Flask im Testmodus & frische Items pro Test
    flask_app.config["TESTING"] = True
    helper.items.clear()
    with flask_app.test_client() as c:
        yield c


def test_full_flow_add_update_download(client):
    # --- Add ---
    today = datetime.today().strftime("%Y-%m-%d")
    r = client.post("/add", data={"text": "Meeting mit Team"}, follow_redirects=True)
    assert r.status_code == 200  # Redirect auf Index + OK
    # Seite zeigt den neuen Eintrag (falls Template vorhanden)
    assert b"Meeting mit Team" in r.data

    # --- Update (toggle completed) ---
    r2 = client.get("/update/0", follow_redirects=True)
    assert r2.status_code == 200
    # Der Eintrag ist weiterhin sichtbar
    assert b"Meeting mit Team" in r2.data

    # --- Download CSV ---
    resp = client.get("/download")
    assert resp.status_code == 200
    assert resp.mimetype == "text/csv"

    body = resp.data.decode("utf-8").strip().splitlines()
    # Header aus helper.get_csv()
    assert body[0] == "Title,Category,Description,Date"
    # Der neue Eintrag ist in der CSV (Category/Description leer, Datum = today)
    assert f"Meeting mit Team,,,{today}" in body[1]
