from enemy import *

type_of_enemy = "Zombie"
enemy = Enemy(type_of_enemy)
enemy.talk()
print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can do attack of {enemy.attack_damage}")