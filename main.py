from utils.utils import open_json, print_operations, class_assignment

adres = "https://jsonkeeper.com/b/Y2QV"

# Открываем библиотеку
list_operations = open_json(adres)

# Присваиваем классу элементы библиотеки
list_operations = class_assignment(list_operations)

# Выводим необходимую инфомацию
print_operations(list_operations)
