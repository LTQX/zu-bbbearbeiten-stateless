from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    isCompleted: bool = False


def add(text):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted

def add(a, b):
    return a + b