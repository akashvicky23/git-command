class Enemy:
    def __init__(self,type_of_enemy:str):
        self.type_of_enemy = type_of_enemy    
        self.health_points = 10
        self.attack_damage = 1
    def talk(self):
        print("I'm an enemy")