from random import randint
import random
import json

from NPC import NPC

characters =[]

with open('enviroment.json') as json_file:
    data = json.load(json_file)
    
Weapons = data['weapon_list']
Rooms = data['room']
    
def createEnviroment():
    
    for npc in data['characters']:
        characters.append(NPC(npc['name'],npc['age']))
        
    assignWeapon(characters) 
    
    Villain = random.choice(characters)
    Villain.setGuilty(True)
    
    ##debug(characters, Villain)
    
    return characters, Rooms, Villain

""" def debug(characters, Villain):
    print('Chartacters Debugger:')
    print(f'The Villain is:{Villain.getName()}')
    for x in characters:
        print(f'NPCs:{x.getName()} ____ Weapon:{x.getWeapon()} _____ Guilty:{x.getGuilty()}')
    
    """
    
def assignWeapon(characters):
    for character in characters:
        character.setWeapon(randomizeGun())
        
def randomizeGun():
    value = randint(0, len(Weapons)-1)
    temp = Weapons[value]
    Weapons.remove(temp)
    return temp
