# tests/test_csv.py
import helper


def setup_function():
    # falls du eine globale Liste nutzt:
    if hasattr(helper, "items"):
        helper.items.clear()


def test_get_csv_basic():
    # Given
    helper.add("Titel A", "Kategorie X", "Beschreibung", "2025-10-21")
    helper.add("Titel B", "Kategorie Y", "Noch was", "2025-10-22")

    # When
    csv_text = helper.get_csv()

    # Then: Header + 2 Zeilen, Kommas als Trennzeichen
    lines = csv_text.strip().splitlines()
    assert lines[0].lower().startswith("title,")  # header vorhanden
    assert len(lines) == 3
    assert "Titel A,Kategorie X,Beschreibung,2025-10-21" in lines[1]
    assert "Titel B,Kategorie Y,Noch was,2025-10-22" in lines[2]


def test_get_csv_escaping_commas_and_quotes():
    # Given: Felder mit Komma und Anführungszeichen
    helper.add(
        'Titel, "A"',
        "Cat,egory",
        'Text "mit" Kommas, und Quotes',
        "2025-10-21",
    )

    # When
    csv_text = helper.get_csv()

    # Then: Felder mit Komma/Quote sind in Anführungszeichen, Quotes verdoppelt
    line = csv_text.strip().splitlines()[1]
    expected = '"Text ""mit"" Kommas, und Quotes"'
    assert '"Titel, ""A"""' in line
    assert '"Cat,egory"' in line
    assert expected in line
