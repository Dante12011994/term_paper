import requests as requests
import urllib3 as urllib3
from utils.classes import Operetion

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def open_json():
    file = requests.get("https://jsonkeeper.com/b/Y2QV", verify=False)
    return file.json()


def class_assignment(list_):
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
    return sorted(list_, key=lambda element: element.date, reverse=True)


def print_operations(list_):
    list_ = sort_list(list_)
    count = 0
    num = 0
    while count < 5:
        element = list_[num]
        if element.state == "EXECUTED":
            element.separetion()
            print(element.print_operation())
            count += 1
        num += 1
