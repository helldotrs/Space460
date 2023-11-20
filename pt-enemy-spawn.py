import time

enemies = []
n = 1

def draw_enemies(enemies):
  for enemy in enemies:
    print(enemy)
  print("/end")

def pause_game(t=1):
  time.sleep(t)

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
