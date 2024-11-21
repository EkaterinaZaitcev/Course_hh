def filter_vacancies(vacancies, filter_city):
    """Фильтрует вакансии по городу """
    return [v for v in vacancies if v.name == filter_city]


def sort_vacancies(vacancies):
    """Сортирует список вакансий по убыванию зарплаты"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies, n):
    """Возвращает указанное количество вакансий"""
    sorted_vacancies = sort_vacancies(vacancies)
    return sorted_vacancies[:n]


def print_vacancies(vacancies):
    """Выводит информацию о вакансиях в консоль"""
    if vacancies:
        for v in vacancies:
            print(v)
            print('-' * 100)
    else:
        print("Нет подходящих вакансий")
