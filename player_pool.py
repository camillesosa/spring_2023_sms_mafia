from random import randint
import random
import json

from NPC import NPC

with open('enviroment.json') as json_file:
    data = json.load(json_file)
    
Weapons = data['weapon_list']
    
def createPlayers():
    
    characters =[]

    for npc in data['characters']:
        characters.append(NPC(npc['name'],npc['age']))
        
    assignWeapon(characters) 
    
    Villain = random.choice(characters)
    Villain.setGuilty(True)
    
    
    debug(characters, Villain)
    
    return characters, Villain
    

def debug(characters, Villain):
    print('Chartacters Debugger:')
    print(f'The Villain is:{Villain.getName()}')
    for x in characters:
        print(f'NPCs:{x.getName()} ____ Weapon:{x.getWeapon()} _____ Guilty:{x.getGuilty()}')
    
    
def assignWeapon(characters):
    for character in characters:
        character.setWeapon(randomizeGun())
        
def randomizeGun():
    value = randint(0, len(Weapons)-1)
    temp = Weapons[value]
    Weapons.remove(temp)
    return temp
            
"""
tengo lista de gente..
las personas no pueden tener la misma pistola
tiene que ser generada random

haces loop
genera una pistola, dasela.. si la persona ya tiene esa pistola, dale otra

"""