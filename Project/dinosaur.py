class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def dino_attack(self, robot): #void
        robot.health -= self.attack_power 
        return robot.health
        
        #this makes is what makes  sense to me will it work? not sure.