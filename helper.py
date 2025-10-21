from dataclasses import dataclass
import operator

items = []


@dataclass
class Item:
    text: str
    date: str
    isCompleted: bool = False


def add(text: str, date: str):
    # Beispiel-Transformation aus deinem alten Code weglassen,
    # damit Tests klar sind. Wenn nötig, wieder ergänzen.
    items.append(Item(text, date))
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index: int):
    return items[index]


def update(index: int):
    items[index].isCompleted = not items[index].isCompleted
