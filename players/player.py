from players.actors import actor
import json

#Create db for the objects within the game_chat.json file 
#read from file and load into mem
Our_Game_Logic = {}
with open('game_chat.json', 'r') as gLFile:
    Our_Game_Logic = json.loads(gLFile.read())
    
#create player class init with actor param    
class player(actor):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.score = 0
    
    #function to grab the players input return invalid if input not found    
    def get_output(self, msg_input):
        found_match = False
        output = [  ]
        if type( Our_Game_Logic[ self.state]['next_state'] ) != str: #choices
            for next_state in Our_Game_Logic[self.state]['next_state']:
                if msg_input.lower() == next_state['input'].lower():
                    self.state = next_state['next_state']
                    if 'point_delta' in next_state:
                        self.score += next_state['point_delta']
                        output.append(f"Your Score {self.score}" )
                    found_match = True
                    break
                    
            #return an invalid choice when found_match is false        
            if found_match == False:
                return ['Ooops... Invalid choice... Choose again']
                
        while True:
            output.append(Our_Game_Logic[ self.state ]['content'])
            if 'next_state' not in Our_Game_Logic[ self.state ] or type( Our_Game_Logic[ self.state ]['next_state'] ) != str:
                break
            self.state = Our_Game_Logic[ self.state ]['next_state']
            
        return output
