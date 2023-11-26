enemies_list = []
ENEMIES_LIST_SIZE = 10 #does not currently work

def print_enemies_list():
    print_list_instances(enemies_list)

def print_list_instances(input_list):
    for instant in input_list:
        print(instant)
    print("/end")

def add_enemy(enemy_type="std"):
    if enemy_type == "std":
        enemies_list.append("standard enemy")
    trim_list_size()

def add_standard_enemy():
    add_enemy("std")

def trim_enemies_list_size():
    global enemies_list
    enemies_list = trim_list_size(enemies_list, ENEMIES_LIST_SIZE)

def trim_list_size(input_list, size):
    while len(input_list) > size:
        input_list.pop(0)
    return input_list

# Example usage

add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()

add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()

add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()

print_enemies_list()
