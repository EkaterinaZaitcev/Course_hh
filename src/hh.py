from abc import ABC, abstractmethod
import json
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

    def __init__(self, file_worker):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__(file_worker)

    def __api_connect(self):
        """Подключение к API hh.ru"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        print("Ошибка получения данных")

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
