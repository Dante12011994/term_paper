# import pytest
import json
from utils.utils import open_json, class_assignment, sort_list, print_operations
from datetime import date
from utils.classes import Operetion

# Открываем тестовые данные из json
with open("test.json", encoding="utf-8") as file:
    test = json.load(file)

# Присваиваем тестовые экземпляры класса
test_list = class_assignment(test)


def test_open_json():
    """
    Тестируем функцию получения информации через requests
    """
    assert open_json('https://jsonkeeper.com/b/7M5T') == [1, 2, 3]


def test_class_assignment():
    """
    Тестируем класс
    """
    assert test_list[0].state == "EXECUTED"
    assert str(test_list[0].date) == "2019-08-26"
    assert test_list[0].amount == "31957.58"
    assert test_list[0].name == "руб."
    assert test_list[0].description == "Перевод организации"
    assert test_list[0].from_ == "Maetsro 1596837868705199"
    assert test_list[0].to == "Счет 64686473678894779589"


def test_print_operation():
    """
    Тестируем вывод информации на экран
    """
    assert print_operations(test_list) == """26.08.2019 Перевод организации
Maetsro 1596 83** **** 5199 -> Счет **9589
31957.58 руб.

04.04.2019 Перевод со счета на счет
Счет **8542 -> Visa Platinum 8990 92** **** 5229
79114.93 USD

23.03.2019 Перевод со счета на счет
-> Счет **1160
43318.34 руб.

"""

