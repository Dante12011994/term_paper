from utils.utils import open_json, print_operations, class_assignment

# Открываем библиотеку
list_operations = open_json()

# Присваиваем классу элементы библиотеки
list_operations = class_assignment(list_operations)

# Выводим необходимую инфомацию
print_operations(list_operations)
