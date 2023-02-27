import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

from tools.logging import logger
#from players.actors import actor

import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []

state = 0
suspects = ['Miss Scarlet', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard']
characters = ['Miss Scarlet', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard']
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

#open file to grab responses
with open('some_responses.txt', 'r') as myfile:
	all_file = myfile.read()

def introduction():
	message = g.sms_client.messages.create(
		body='Welcome Detective, to CLUE: Text to find Treachery! Do you mind confirming your name before I go over the details of the case?',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
	
def who(suspects):
	message = g.sms_client.messages.create(
		body='The suspects are: ' + suspects + ' Who do you think the murderer is? (Please enter name exactly as shown)',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
	
def makeAlibi(suspect, status):
	if(status == 'do not remember'):
		additions = ['Sorry...', "Why are you asking me anyways?! I'm not the murderer!", "I wouldn't tell you anyways."] 
		alibi = suspect + ': I ' + status + '... ' + additions[random.randint(0, 2)]
	else:
		additions = ["You don't think it was me, right?", "But why are you asking me? I didn't do it!", "Please find the killer soon, I'm scared!"]
		alibi = suspect + ': I ' + status + ' at the time of the murder. ' + additions[random.randint(0, 2)]
	return alibi
	
def handle_request():
	#main
	global state
	global suspects
	global characters
	global murderer
	global rounds
	logger.debug(request.form)
	#while(state != 5):
	if(state == 0):
		introduction()
	if(state == 1):
		handle_welcome(request.form['Body'])
		killed ='Mrs. White'
		#suspects = ['Miss Scarlet', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard']
		#characters = suspects
		murderer = suspects[random.randint(0, 4)]
		suspects.remove(murderer)
		rounds = 1
		state += 1
	if(state == 2):
		#victim, murder weapon, location, and time change each round
		weapons = ['hammer', 'kitchen knife', 'shovel', 'book', 'pen']
		keyClue = random.randint(0, 4)
		places = ['garage', 'kitchen', 'gardens', 'library', 'study']
		#use keyClue for murder weapon and murderer (true location)
		weapUsed = weapons[keyClue]
		killLoc = places[random.randint(0, 4)]
		handle_roundPtOne(killed, weapUsed, killLoc)
		#add alibis here (might just text all alibis tbh)
		#alibis for inocent suspects
		alibis = ['was with ', 'was by myself', 'do not remember']
		if(rounds > 1):
			alibis.remove('do not remember')
		susToUse = suspects
		i = 0
		while(i < len(suspects)):
			randomLoc = random.randint(0, 4)
			while(randomLoc == keyClue):
				randomLoc = random.randint(0, 4)
			alibi = alibis[random.randint(0, len(alibis)-1)]
			if(alibi == 'was with '):
				if(len(susToUse) == 0):
					alibi = 'was by myself'
				else:
					using = random.randint(0, len(susToUse)-1)
					alibi = alibi + susToUse[using] + ' in the ' + places[randomLoc]
					susToUse.remove(susToUse[using])
					iAlibi = makeAlibi(suspects[i], alibi)
					#make handle_alibi call for each specific suspect, if possible, have user input name of suspect that they want to hear from
					handle_alibi(iAlibi)
			if(alibi == 'was by myself'):
				alibi = alibi + ' in the ' + places[randomLoc]
				iAlibi = makeAlibi(murderer, alibi)
				#make handle_alibi call for each specific suspect, if possible, have user input name of suspect that they want to hear from
				handle_alibi(iAlibi)
			if(alibi == 'do not remember'):
				iAlibi = makeAlibi(murderer, alibi)
				#make handle_alibi call for each specific suspect, if possible, have user input name of suspect that they want to hear from
				handle_alibi(iAlibi)
			i += 1
		#false alibi for murderer
		randomLoc = random.randint(0, 4)
    		while(randomLoc == keyClue):
    			randomLoc = random.randint(0, 4)
		alibi = alibis[random.randint(0, len(alibis)-1)]
		if(alibi == 'was with'):
			alibi = alibi + suspects[random.randint(0, len(suspects)-1)] + ' in the ' + places[randomLoc]
			iAlibi = makeAlibi(murderer, alibi)
			#make handle_alibi call for each specific suspect, if possible, have user input name of suspect that they want to hear from
			handle_alibi(iAlibi)
		if(alibi == 'was by myself'):
			alibi = alibi + ' in the ' + places[randomLoc]
			iAlibi = makeAlibi(suspects[i], alibi)
			#make handle_alibi call for each specific suspect, if possible, have user input name of suspect that they want to hear from
			handle_alibi(iAlibi)
		if(alibi == 'do not remember'):
			iAlibi = makeAlibi(suspects[i], alibi)		
			#make handle_alibi call for each specific suspect, if possible, have user input name of suspect that they want to hear from
			handle_alibi(iAlibi)
		i = 0
		suspectsStr = ''
		while(i < len(characters)):
			if(i == len(characters)-1):
				suspectsStr = suspectsStr + 'and ' + characters[i] + '.'
				i += 1
			else:
				suspectsStr = suspectsStr + characters[i] + ', '
				i += 1
		who(suspectsStr)
	if(state == 3):
		maybeMurderer = request.form['Body']
		logger.debug('They picked ' + maybeMurderer)
		logger.debug('Murderer is ' + murderer)
		if(maybeMurderer != murderer):
			suspects.remove(maybeMurderer)
			characters.remove(maybeMurderer)
			if(len(suspects)-1 == 1):
				handle_roundPtTwo(maybeMurderer, "wrong", len(suspects)-1)
				rounds += 1
				state = 3
				outcome = 'lose'
			if(len(suspects)-1 > 1):
				handle_roundPtTwo(maybeMurderer, "wrong", len(suspects)-1)
				rounds += 1
				state = 1
				killed = suspects[random.randint(0, len(suspects)-1)]
				suspects.remove(killed)
				characters.remove(killed)
		else:
			handle_roundPtTwo(maybeMurderer, "right", len(suspects)-1)
			state = 3
			outcome = 'win'
			#handle_roundPtTwo(request.form['Body'])
	state += 1
	if(state == 4):
		handle_gameOver(outcome, rounds, len(suspects)-1)
		#would you like to play again? yes/no?
		playA = request.form['Body']
		if(playA == 'yes' | 'Yes'):
			state = 1
		else:
			state = 5
			#end
	if(state == 0):
		state += 1
	return json_response( status = "ok" )

def handle_welcome(name):
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		body='Thank you Detective ' + name + ', we are happy to have you on this case. Unfortunately, there seems to be a killer on the loose! The victim is Mrs. White, and we have narrowed the suspects to five individuals: Miss Scarlet, Professor Plum, Mrs. Peacock, Mr. Green, and Colonel Mustard. These five suspects were guests at a dinner party at Mountain Manor, a secluded mansion here in California, where the murder took place. In an attempt to prevent escape, we have asked all the guests to stay there while we attempt to find the murderer, but the longer we take to find the murderer, the longer the innocents are in danger of also being attacked. One of the guests is definitely the traitor, you just have to find out which one it is! I will take you to the manor, so you can take a look at the evidence.',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )


def handle_roundPtOne(killed, weapUsed, killLoc):
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		body='The victim was ' + killed + '. ' + killed + ' was killed with a ' + weapUsed + ' in the ' + killLoc + '.',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])

def handle_roundPtTwo(maybeMurderer, isM, susLeft):
	logger.debug(request.form)
	if(isM == 'wrong'):
		if(susLeft > 1):
			message = g.sms_client.messages.create(
				#if Suspects array is too small, print different message as player has lost
				body='Oh no! ' + maybeMurderer + ' was not the murderer! Looks like the murderer is still out there. We need to find them before they attack again!',
				from_=yml_configs['twillio']['phone_number'],
				to=request.form['From'])
		else:
			message = g.sms_client.messages.create(
				#if Suspects array is too small, print different message as player has lost
				body='Oh no! ' + maybeMurderer + ' was not the murderer and you failed to find the murderer in time :(',
				from_=yml_configs['twillio']['phone_number'],
				to=request.form['From'])
	if(isM == 'right'):
		message = g.sms_client.messages.create(
			#if Suspects array is too small, print different message as player has lost
			body='Excellent job Detective! ' + maybeMurderer + ' was the murderer!',
			from_=yml_configs['twillio']['phone_number'],
			to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_alibi(alibi):
	logger.debug(request.form)
	#the murderers fake alibi
	message = g.sms_client.messages.create(
		body=alibi,
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_gameOver(outcome, rounds, saved, name, murderer):
	logger.debug(request.form)
	if(outcome == 'win'):
	#if(rounds == 1):
	#	message = g.sms_client.messages.create(
	#		body='It only took you 1 round to find the murderer and you saved everyone else involved! Outstanding work Detective ' + name + ', they better give you a raise!',
	#		from_=yml_configs['twillio']['phone_number'],
	#		to=request.form['From']
	#if(rounds > 1):
		message = g.sms_client.messages.create(
			body='It took you ' + rounds + ' rounds to find the murderer and you saved ' + saved + ' people. Nice work Detective ' + name + '!',
			from_=yml_configs['twillio']['phone_number'],
			to=request.form['From'])
	if(outcome == 'lose'):
		message = g.sms_client.messages.create(
			body='The murderer was actually ' + murderer + '. I am sorry Detective  ' + name + ', at least you got out of there safe and sound.  Better luck next time.',
			from_=yml_configs['twillio']['phone_number'],
			to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
