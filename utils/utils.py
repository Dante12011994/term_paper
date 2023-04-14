import requests as requests
import urllib3 as urllib3
from utils.classes import Operetion

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




def open_json(adres):
    """
    Вызывает и раскрывает библиотеку с удаленного сервера
    """
    file = requests.get(adres, verify=False)
    return file.json()


def class_assignment(list_):
    """
    Присваевает классу "Operation" каждый элемент библиотеки.
    :param list_: Библиотека
    :return: Список элементов класса
    """
    list_of_transaktions = []
    for element in list_:
        list_of_transaktions.append(Operetion(element['state'],
                                              element['date'],
                                              element['operationAmount']['amount'],
                                              element['operationAmount']['currency']['name'],
                                              element['description'],
                                              element.get('from'),
                                              element['to']))
    return list_of_transaktions


def sort_list(list_):
    """
    Возвращает список элементов класса отсортированных по дате,
    от последней операции к самой стаарой.
    """
    return sorted(list_, key=lambda element: element.date, reverse=True)


def print_operations(list_):
    """
    Выводит на экран 5 последних выполненных операций
    """
    list_ = sort_list(list_)
    count = 0
    x = ""
    for element in list_:
        if element.state == "EXECUTED":
            element.separetion()
            count += 1
            x += element.return_operation()
        if count == 5:
            break
    return x