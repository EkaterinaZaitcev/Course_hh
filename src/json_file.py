from abc import ABC, abstractmethod

import json
import os.path


class JSONVacancy(ABC):
    """Абстрактный метод для создания и удаления JSON-файлов"""

    @abstractmethod
    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self,words_del):
        """Метод для удаления не нужного файла"""
        pass


class HH_Vacancy(JSONVacancy):
    """Класс для создания и удаления файлов с данными по вакансиям из сайта HH.ru"""

    def __init__(self, file_name_save='data/vacancies_1.json'):
        """Инициализатор класса"""
        self.__file_name_save = file_name_save

    def get_file_name(self):
        return self.__file_name_save
