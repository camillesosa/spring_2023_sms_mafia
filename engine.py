from player_pool import *
import random

class Game:
    
    input_history = []
    GAMEOVER = False
    
    def __init__(self):
        self.players, self.rooms, self.villain = createEnviroment() ;
        
    def get_villain_index(self):
        
        Villain_index = None

        for person in self.players:
            if person.guilty == True:
                Villain_index = self.players.index(person)
                break
        return Villain_index
            
            
    def judging_time(self, player_input):
        
        
        
        try:
            if player_input == self.get_villain_index():
                self.GAMEOVER = True
            else:
                self.players[player_input].jail = True
                self.jail_time(player_input);
                #print(f'{self.players[player_input].name} was not the killer')
        except:
            print('That wasnt part of the options 👀')
            
    def round_room(self):
        return random.choice(self.rooms)
    
    def input_whoisguilty(self):
        # Convert it into integer
            player_input = int(input(f"Who do you think is the killer: "))
            self.judging_time(player_input-1) 
            
    def check_outofbounce(self, input):
        if input > len(self.players):
            return False
        return True
    
    def jail_time(self,input):
        self.players.pop(input)
                
    def onthefield(self):
        for i, npc in enumerate(self.players):
            print(f'{i+1}. {npc.name}')
        
            
    def update(self):
        self.scenario_story()
        self.onthefield()
        self.input_whoisguilty()
    
    def debugger(self):
        for attr in self.players :
            print(f'{attr.name} and is {attr.guilty}')

    def get_random(self):
        return self.players[random.randint(0,len(self.players)-1)] 
    
            
    def scenario_story(self):
        npc = self.get_random()
        print(f'You walk into the room and found that {npc.getName()} is in the {self.round_room()} with {npc.getWeapon()} in hand')
        print(f'There is a killer Among us, there are {len(self.players)} people in the house')
        print(f'Who do you think did it?')
        
    def run(self):
        ##ask for username input
        print(f'Welcome to the Slaughter House:')
        #self.debugger()
        while True:                
            self.update();
            if self.GAMEOVER == True:
                print("Congrats!!!! You Found the Killer!!!!")
                break
        print('The nightmare is over')


""" from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='your_twilio_number',
    to='recipient_phone_number',
    body='Hello, this is a test message from Twilio!'
)

print(message.sid)  # optional: print the message SID for reference """