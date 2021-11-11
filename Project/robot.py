from weapon import Weapon


class Robot:
    def __init__(self, name, health, Weapon):
        self.name = name
        self.health = health
        self.weapon = Weapon
        pass

    def bot_attack(self, dinosaur): #void - use attack power to damage oponent(dino). return health post attack = "pa"
       pa_dino_health = dinosaur.health - self.wap.attack_power #dino health - weapon damage number
       return pa_dino_health

    #this makes is what makes  sense to me will it work? not sure.