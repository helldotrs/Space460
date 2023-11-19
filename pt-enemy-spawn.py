import time

enemies = []
n = 0

white True:
  time.sleep(1)
  for enemy in enemies:
    print(enemy)
  print("/end")
  
  if len(enemies) >= 10: 
    enemies.pop(0)
  enemies.append(n)

  n += 1

