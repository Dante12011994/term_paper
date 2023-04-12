from utils.utils import open_json, print_operations, class_assignment

list_operations = open_json()
list_operations = class_assignment(list_operations)
print_operations(list_operations)
