enemies_list = []
enemies_list_size = 10

def draw_enemies(enemies):
    """Print the list of enemies."""
    for enemy in enemies:
        print(enemy)
    print("/end")

def add_enemy(enemy_type="std"):
    """Add an enemy to the list based on the given type."""
    if enemy_type == "std":
        add_standard_enemy()
    limit_list_size()

def add_standard_enemy():
    """Add a standard enemy to the list."""
    enemies_list.append("standard enemy")

def limit_list_size():
    """Limit the size of the enemies list."""
    global enemies_list
    enemies_list = trim_list_size(enemies_list, enemies_list_size)

def trim_list_size(input_list, size):
    """Trim the list size to the specified size."""
    while len(input_list) > size:
        input_list.pop(0)
    return input_list

# Example usage
add_standard_enemy()
add_standard_enemy()
add_standard_enemy()
draw_enemies(enemies_list)
