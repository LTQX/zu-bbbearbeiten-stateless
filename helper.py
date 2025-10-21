from dataclasses import dataclass
import operator
from typing import List

items: List["Item"] = []


@dataclass
class Item:
    # Für CSV brauchen wir title/category/description/date
    title: str
    category: str
    description: str
    date: str
    isCompleted: bool = False

    # Rückwärtskompatibilität: bisher hast du im Template `item.text` benutzt
    @property
    def text(self) -> str:
        return self.title


def add(*args):
    """
    Rückwärtskompatibel:
      - add(text, date)
      - add(title, category, description, date)
    """
    if len(args) == 2:
        title, date = args
        category = ""
        description = ""
    elif len(args) == 4:
        title, category, description, date = args
    else:
        raise TypeError(
            "add() expects (text, date) or " "(title, category, description, date)"
        )

    items.append(Item(str(title), str(category), str(description), str(date)))
    # Nach Datum sortieren (YYYY-MM-DD Strings sind lexikographisch sortierbar)
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index: int):
    return items[index]


def update(index: int):
    items[index].isCompleted = not items[index].isCompleted


# ---------- CSV-Export für LZ 4.1 ----------


def _csv_escape(value: str) -> str:
    """
    CSV-konformes Escaping:
      - doppelte Anführungszeichen werden verdoppelt
      - Felder mit Komma/Quote/Zeilenumbruch werden in Quotes gesetzt
    """
    s = value.replace('"', '""')
    if ("," in s) or ('"' in value) or ("\n" in s) or ("\r" in s):
        return f'"{s}"'
    return s


def get_csv() -> str:
    """
    Erstellt CSV mit Header: Title,Category,Description,Date
    """
    header = "Title,Category,Description,Date"
    lines = [header]
    for it in items:
        row = ",".join(
            [
                _csv_escape(it.title),
                _csv_escape(it.category),
                _csv_escape(it.description),
                _csv_escape(it.date),
            ]
        )
        lines.append(row)
    return "\n".join(lines) + "\n"
