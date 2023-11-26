enemies_list = []
enemies_list_size = 10

def enemies_draw(enemies):
    for enemy in enemies:
        print(enemy)
    print("/end")

def enemies_add(type="std"):
    if type == "std":
        enemies_add_standard()
    enemies_limit_size()

def enemies_add_standard():
    enemies_list.append("standard enemy")

def enemies_limit_size():
    global enemies_list
    enemies_list = limit_list_size(enemies_list, enemies_list_size)

def limit_list_size(input_list, input_size):
    while len(input_list) > input_size:
        input_list.pop(0)
    return input_list

# Example usage
enemies_add_standard()
enemies_add_standard()
enemies_add_standard()
enemies_draw(enemies_list)





"""FIXME
def limit_list_size(input_list, size=10)
  if len(input_list) >= 10: 
    input_list.pop(0)
    """
"""FIXME
def add_enemy():
  enemies.append(n)

  n += 1
 """ 
  """
while True:
  draw_enemies(enemies)
  pause_game()

  #limit_list_size(enemies)
  if len(enemies) >= 10: 
    enemies.pop(0)

  enemies.append(n)

  n += 1
  """
