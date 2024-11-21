class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('name', 'city', 'salary', 'result', 'data_base_hh')

    def __init__(self, name, city, salary,data_base_hh ):
        """Инициализатор для класса"""
        self.name = name
        self.city = city
        self.salary = self.__salary_validation(salary)
        self.data_base_hh = data_base_hh
        self.result = []

    @staticmethod
    def __salary_validation(salary: int):
        """Валидация зарплаты"""
        if salary:
            return salary
        return 0

    def __le__(self, other, my_list):
        """ Магический метод фильтрации списка вакансий по заработной плате"""
        res_salary = []
        for i in my_list:
            if other <= i["salary"]["from"]:
                res_salary.append(i)
        return res_salary
