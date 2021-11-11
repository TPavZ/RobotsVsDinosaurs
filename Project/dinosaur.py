class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.ap = attack_power
        self.health = health

    def dino_attack(self, robot): #void
        pa_bot_health = robot.health - self.ap.attack_power #dino health - weapon damage number
        return pa_bot_health
        
        #this makes is what makes  sense to me will it work? not sure.