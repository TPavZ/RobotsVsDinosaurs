from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Gun", 50)
        

    def bot_attack(self, dinosaur): #void - use attack power to damage oponent(dino). return health post attack = "pa"
       dinosaur.health -= self.weapon.wap
       return dinosaur.health
 
#wall_e = Robot("WALL-E", 50, Weapon("Compactor", 30)) #weapon pinch
#droideka = Robot("Droideka", 100, Weapon("Rapid Fire canons", 45)) 
#c12 = Robot("C12", 100, Weapon("Missile Storm", 55))