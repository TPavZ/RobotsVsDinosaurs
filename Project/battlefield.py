from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
#import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()   
        self.herd = Herd()

    def run_game(self): # takes input from welcome to start the game.
        start_game = self.display_welcome()
        if start_game == True:
            print("\nLets get ready to RUMBLE!!!\nRobots have been granted first attack.\n") #need to initialize the battle here.
            #*** need to initialize the battle here, collect fighters, battle, then end battle.
            self.herd.create_herd()
            self.fleet.create_fleet()
            self.battle()
            #self.display_winners() #STOP, Battle is over
        else:
            self.run_game() #attempt to start game again.


    def display_welcome(self): #message and startup yes / no
        print("\n***WELCOME TO THE BATTLEFIELD***\n\n\t\tRobots\n\tVs.\n\t\tDinosaurs\n")
        new_game = input("Start A New Game? Yes or No: ").lower()
        if new_game == "yes": #then what team goes first?
            return True
        else:
            return False

    def battle(self): #as default dino will attack first. can set up random attacker later probs best to do that here.
        #turns first.
        #select bot or dino out of the options 
        #once selected the back and forth of the fight needs to happen until one reaches 0 health left, at this point we need to look 
        #   back to the selection.
        #once all the fights on one team have been eliminated, the fight is over and the remaining team wins.
        #take and display options (from below) to choose a fighter to use.
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            self.robo_turn()
            self.dino_turn()            
        #if len(self.herd.dinosaurs) == 0 or len(self.fleet.robots) == 0: #STOP, Battle is over
            #self.display_winners()
                
            
            
            
            
        #need to .pop dead competetors out of the lists

    def dino_turn(self): #void Make the dino attack
        #take a dino of choice
        #have the dino attack bot
        #use attack damage to subtract health from bot
        #selection = int(input("choose a dino to attack [0, 1, or 2]:"))
        #print(self.herd.dinosaurs[0])
        #move = robot[index of selection] health - dino[index of selection] attack damage.
        #take dino of selection then attack damage is subtracted from the robo health.
        #take robot index one and subrtract dino index one attack damage.
        self.show_doo()
        dino_selection = int(input("choose a Dinosaur to attack with. [0, 1, or 2]:"))
        self.show_roo()
        robo_selection = int(input("choose a Robot to attack. [0, 1, or 2]:"))
        self.herd.dinosaurs[dino_selection].dino_attack(self.fleet.robots[robo_selection])
        if self.fleet.robots[robo_selection].health <= 0:
            self.fleet.robots.remove(self.fleet.robots[robo_selection])
        #if len(self.fleet.robots) == 0:
            #self.display_winners()
            
        


    def robo_turn(self): #void Make the bot attack
        #take a bot of choice
        #have the bot attack dino
        #use attack damage to subtract health from dino
        self.show_roo()
        dino_selection = int(input("choose a Robot to attack with. [0, 1, or 2]:"))
        self.show_doo()
        robo_selection = int(input("choose a Dinosaur to attack. [0, 1, or 2]:"))
        self.fleet.robots[robo_selection].bot_attack(self.herd.dinosaurs[dino_selection])
        if self.herd.dinosaurs[dino_selection].health <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_selection])
        #if len(self.herd.dinosaurs) == 0:
            #self.display_winners()

    def show_doo(self): #void doo=dino opponent options, print each bot in fleet name and health
        index = 0
        for dino in self.herd.dinosaurs:
            print(f"{index} - {dino.name} - Attack Power: {dino.attack_power} - Health: {dino.health}")
            index += 1
            
        

    def show_roo(self): #void roo=robo opponent options, print each dino in herd name and health
        index = 0
        for bot in self.fleet.robots:
            print(f"{index} - {bot.name} - Attack Weapon & Power: {bot.weapon.wn}, {bot.weapon.wap} - Health: {bot.health}")
            index += 1
            

    def display_winners(self): #void who wins and how?
        #team with one remaining attacker wins.
        if len(self.herd.dinosaurs) == 0:
            print("Battle Champions Are The Robots!")
        elif len(self.fleet.robots) == 0:
            print("Battle Champions Are The Dinosaurs!")
            