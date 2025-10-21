import helper


def test_add_basic():
    helper.items.clear()
    helper.add("Testaufgabe", "2024-10-21")
    assert len(helper.items) == 1
    assert helper.items[0].text == "Testaufgabe"
    assert helper.items[0].date == "2024-10-21"


def test_sort():
    helper.items.clear()
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]
    for text, date in todos:
        helper.add(text, date)

    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i + 1].date
