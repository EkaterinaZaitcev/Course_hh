from abc import ABC, abstractmethod
import json
from unittest import result

import requests


class Parser(ABC):
    """Родительский класс get-запросов"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод отправки get-запроса на сайт Head Hunter"""
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []


    def load_vacancies(self, keyword):
        try:
            self.__params['text'] = keyword
            while self.__params.get('page') != 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
                #print(vacancies)
        except Exception as e:
            print(e)
            print("Ошибка в классе HH")
            return []
