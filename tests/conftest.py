import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies_dict():
    vacs = [
        {
            "name": "Программист",
            "url": "https://hh",
            "requirement": "требования",
            "responsibility": "обязанности",
            "salary": 0,
        },
        {
            "name": "Программист2",
            "url": "https://hh2",
            "requirement": "требования2",
            "responsibility": "обязанности2",
            "salary": 120000,
        },
    ]

    return vacs


@pytest.fixture
def vacancies_objects():
    vacs = [
        Vacancy("Программист", "https://hh", "требования", "обязанности", 100000),
        Vacancy("Программист1", "https://hh1", "требования 1", "обязанности 1", 0),
        Vacancy("Программист2", "https://hh2", "требования 2", "обязанности 2", 50000),
        Vacancy("Программист3", "https://hh3", "требования 3", "обязанности 3", 10000),
    ]

    return vacs