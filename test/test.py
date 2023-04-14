# import pytest
import json
from utils.utils import open_json, class_assignment, sort_list, print_operations
from datetime import date
from utils.classes import Operetion

with open("test.json", encoding="utf-8") as file:
    test = json.load(file)

test_list = class_assignment(test)


def test_open_json():
    assert open_json('https://jsonkeeper.com/b/7M5T') == [1, 2, 3]


def test_class_assignment():
    # test_list = class_assignment(test)
    assert test_list[0].state == "EXECUTED"
    assert str(test_list[0].date) == "2019-08-26"
    assert test_list[0].amount == "31957.58"
    assert test_list[0].name == "руб."
    assert test_list[0].description == "Перевод организации"
    assert test_list[0].from_ == "Maetsro 1596837868705199"
    assert test_list[0].to == "Счет 64686473678894779589"


def test_return_operation():
    assert test_list[0].return_operation() == """26.08.2019 Перевод организации
Maetsro 1596837868705199-> Счет 64686473678894779589
31957.58 руб.
"""

def test_print_operation():
    assert print_operations(test_list) == """26.08.2019 Перевод организации
Maetsro 1596 83** **** 5199 -> Счет **9589
31957.58 руб.
"""