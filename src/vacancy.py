class Vacancy:
    __slots__ = ('title', 'alternate_url', 'name', 'salary', 'salary_from', 'salary_to')
    def __init__(self, title, alternate_url, name, salary):
        self.title = title
        self.alternate_url = alternate_url
        self.name = name
        self.salary = salary
        self.validate__()

    def validate__(self):
        """Валидация отображения ЗП по признаку отсутствия информации или цифр в графе ЗП от или до"""
        if not self.salary:
            self.salary_from = 0
            self.salary_to = 0
            return

        if not self.salary["from"]:
            self.salary_from = 0
        else:
            self.salary_from = self.salary["from"]

        if not self.salary["to"]:
            self.salary_to = 0
        else:
            self.salary_to = self.salary["to"]

    @classmethod
    def create_vacancies(cls, hh_vacancies):
        """Преобразование словарей из json файла в экземпляры класса Vacancy"""
        instances_vacancy = []
        for vacancies_info in hh_vacancies:
            title = vacancies_info['name']
            alternate_url = vacancies_info['alternate_url']
            salary = vacancies_info['salary']
            name = vacancies_info['area']['name']
            vacancy = cls(title, alternate_url, name, salary)
            instances_vacancy.append(vacancy)
        return instances_vacancy

    def __lt__(self, other):
        """Сравнение экземпляров класса Vacancy по ЗП"""
        return self.salary_from < other.salary_from

    def __str__(self):
        """Вывод объекта класса Vacanсy для пользователя"""
        return f'{self.title}, город {self.name}, ЗП от {self.salary_from} до {self.salary_to}, ссылка: {self.alternate_url}'

