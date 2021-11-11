from robot import Robot # need to make a list of the bots we crate using the bot class.
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self): #void name of bots = Robot(name, health, weapon) and weapon from Weapon(name, power)
        wall_e = Robot("WALL-E", 50, Weapon("Compactor", 30)) #weapon pinch
        droideka = Robot("Droideka", 100, Weapon("Rapid Fire canons", 45)) 
        c12 = Robot("C12", 100, Weapon("Missile Storm", 55))
        self.robots.append(wall_e)
        self.robots.append(droideka)
        self.robots.append(c12)

