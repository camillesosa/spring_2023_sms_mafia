from player_pool import *
import random

class Game:
    
    input_history = []
    GAMEOVER = False
    
    def __init__(self):
        self.players, self.rooms, self.villain = createEnviroment() ;
    
    def judging_time(self, player_input):
        for person in self.players:
            if player_input == self.villain.name:
                self.GAMEOVER = True
            else:
                if(player_input == person.name):
                    person.jail = True
                
    def round_room(self):
        return random.choice(self.rooms)
    
    def input_whoisguilty(self):
        #! change to number options ex: 1 Carlos Slim ..  2 pokemon .. etc
        player_input = input(f"who do you think is the killer: ")
        
        for person in self.players:
            if person.name.upper() != player_input.upper():
                print('name not in the list')
            else:
                self.input_history.append(player_input)
                self.judging_time(player_input.upper())
        
        
    def checkplayers(self):
        for player in self.players:
            if player.jail == True:
                self.players.remove(player)
                print(f'You have sent {player.name} to jail')
            
    def update(self):
        self.checkplayers();
        self.input_whoisguilty()
        
    def run(self):
        ##ask for username input
        print(f'welcome to the slaughter house:')
        while True:                
            self.update();
            print(f'There is a killer Among us, there are {len(self.players)} player in the match')
            print(f'you walk into the room and found that {self.players[random.randint(0, 4)].getName()} is in the {self.rooms[random.randint(0, 4)]} with {self.players[random.randint(0, 4)].getWeapon()} in her hand')
            print(f'Who is the killer?')
            if self.GAMEOVER == True:
                break
