import json
import os

from config import DATA_DIR
from src.json_file import JSONSaver
from src.vacancy import Vacancy


def test_saver():
    saver = JSONSaver("test.json")
    vac = Vacancy("Программист", "https://hh", "требования", "обязанности")

    saver.add_vacancy(vac)
    file = os.path.join(DATA_DIR, "test.json")

    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    assert data == [
        {
            "name": "Программист",
            "url": "https://hh",
            "requirement": "требования",
            "responsibility": "обязанности",
            "salary": 0,
        }
    ]