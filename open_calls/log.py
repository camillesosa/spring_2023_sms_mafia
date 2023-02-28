#import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

#from tools.logging import logger

from picGrab import *

import random

#Create pool size for number of suspects
susPool = 6

yml_configs = {}
BODY_MSGS = []

#with open('config.yml', 'r') as yml_file:
#    yml_configs = yaml.safe_load(yml_file)
    

#open file to grab names
with open('names.txt', 'r') as names:
	sumNames = names.read()
	
#create array to hold suspects names
myGame = []

#grab random names from file check for doubles
for i in range(susPool):
	inputName = random.choice(sumNames.splitlines())
	if(inputName in myGame):
		inputName = random.choice(sumNames.splitlines())
		myGame.append(inputName)
	else:
		myGame.append(inputName)
	
print(myGame)


#for the random choice of which will be the werewolf


#choosing the game type from citizen wolf or random game position gPos
def game_choice(gPos):
	if(gPos == 0):
		pass
		#choose to be wolf		
	elif(gPos == 1):
		pass
		#choose to be civil
	elif(gPos == 2):
		pass
		#dont care rando
	

		

def handle_win(winMod):
	
	#logger.debug(request.form)
	
	#call win state
	if(winMod == 0):
		winPic = give_Me_A_Pic(4) #Wolf wins
	elif(winMod ==1):
		winPic = give_Me_A_Pic(2) #Citizen wins
	
	message = g.sms_client.messages.create(
		body="Winner Congradulations",
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'],
		media_url=[winPic])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
	
handle_win(0)
handle_win(1)
	
def handle_lose(loseMod):
	
	#logger.debug(request.form)
	
	#call lose state
	if(winMod == 0):
		losePic = give_Me_A_Pic(2) #wolf loses
	elif(winMod ==1):
		losePic = give_Me_A_Pic(4) #citizen loses

	
	message = g.sms_client.messages.create(
		body="Sorry, you didn't make it",
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'],
		media_url=[losePic])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
	
handle_lose(0)
handle_lose(1)
	
def handle_wolf():
	
	#logger.debug(request.form)
	
	#call wolf pic
	wPic = give_Me_A_Pic(3)
	
	message = g.sms_client.messages.create(
		body="Winner Congradulations",
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'],
		media_url=[wPic])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

handle_wolf()

	
def handle_cit():
	
	#logger.debug(request.form)
	
	#call civ pic 
	cPic = give_Me_A_Pic(1)
	
	message = g.sms_client.messages.create(
		body="You've been choosen to be a citizen",
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'],
		media_url=[cPic])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

handle_cit()
	
	
def handle_wolftakedown(takenDown):
		
	#logger.debug(request.form)
	
	#call who was taken down 
	tdPic = give_Me_A_Pic(5)
	
	message = g.sms_client.messages.create(
		body=takenDown,
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'],
		media_url=[tdPic])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
	
handle_wolftakedown('bill')

