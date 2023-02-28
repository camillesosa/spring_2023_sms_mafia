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
killed = 'Mrs. White'
heardAll = 'f'
isM = 'wrong'
hit = 0

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
	
def who():
	message = g.sms_client.messages.create(
		body='Who do you think the murderer is? (Please enter name exactly as shown)',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])

def roundDecision(maybeMurderer, isM, susLeft):
	if(isM == 'wrong'):
		if(susLeft > 1):
			val = 'Oh no! There was another attack. Looks like ' + maybeMurderer + ' was not the murderer. Lets take a look at the new evidence.'
		else:
			val = 'Oh no! ' + maybeMurderer + ' was not the murderer and you failed to find the murderer in time :('
	if(isM == 'right'):
		val = 'Excellent job Detective! ' + maybeMurderer + ' was the murderer!'
	return val

def gameOver(outcome, rounds, saved, name, murderer):
	if(outcome == 'win'):
		if(rounds == 1):
			val = 'It only took you 1 round to find the murderer and you saved everyone else involved! Outstanding work Detective ' + name + ', they better give you a raise!'
		if(rounds > 1):
			val = 'It took you ' + rounds + ' rounds to find the murderer and you saved ' + saved + ' people. Nice work Detective ' + name + '!'
	if(outcome == 'lose'):
		val = 'The murderer was actually ' + murderer + '. I am sorry Detective  ' + name + ', at least you got out of there safe and sound.  Better luck next time.'
	return val

def printList(characters):
	i = 0
	suspectsStr = ''
	while(i < len(characters)):
		if(i == len(characters)-1):
			suspectsStr = suspectsStr + 'and ' + characters[i] + '.'
			i += 1
		else:
			suspectsStr = suspectsStr + characters[i] + ', '
			i += 1
	return suspectStr
	
def handle_request():
	#main
	global state
	global suspects
	global characters
	global murderer
	global rounds
	global killed
	global isM
	global hit
	logger.debug(request.form)
	#while(state != 5):
	if(state == 0):
		introduction()
	if(state == 1):
		handle_welcome(request.form['Body'])
		#killed ='Mrs. White'
		#suspects = ['Miss Scarlet', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard']
		#characters = suspects
		murderer = 'Miss Scarlet'
		rounds = 1
		state += 1
	if(state == 2):
		killed = 'Mrs. White'
		weapUsed = 'hammer'
		killLoc = 'library'
		handle_roundPtOne(killed, weapUsed, killLoc)
		
		state += 1
		hit = 0
	if(state == 3):
		if(hit == 0):
			scarAlibi = "Miss Scarlet: I'm not too sure... I think I was in the gardens at the time of the murder. Oh! Yes I was! I was in the gardens talking with the gardeners. You could ask them, but you already told them to leave, huh?"
			handle_alibi(scarAlibi)
			plumAlibi = "Professor Plum: I was in the study of course! Huh? Someone to back up my alibi... well I was alone so..."
			handle_alibi(plumAlibi)
			peacAlibi = "Mrs. Peacock: I don't remember... I mean I could've been anywhere during that time! Why are you asking me anyways?! I'm obviously not the murderer!"
			handle_alibi(peacAlibi)
			greeAlibi = "Mr. Green: I was in the garage I believe. I might've seen someone else come in, one of the girls for sure... Huh? No, I don't think they saw me."
			handle_alibi(greeAlibi)
			mustAlibi = "Colonel Mustard: I decline to answer. I can't believe you're even asking me! You better find the murderer quick, he's probably dangerous!"
			handle_alibi(mustAlibi)
		
			who()
		if(hit > 0):
			state += 1
		hit += 1
		
	if(state == 4):
		#result
		maybeMurderer = request.form['Body']
		handle_guessConfirm()
		logger.debug('They picked ' + maybeMurderer + ' and the murderer is ' + murderer)
		if(maybeMurderer == murderer):
			isM = 'right'
			state = 14
		else:
			ism = 'wrong'
			state += 1
		result = roundDecision(maybeMurderer, isM, len(characters))
		handle_roundPtTwo(result)
		
		
	if(state == 5):
		killed = 'Mr. Green'
		characters.remove('Mr. Green')
		weapUsed = 'knife'
		killLoc = 'study'
		handle_roundPtOne(killed, weapUsed, killLoc)
		state += 1
		hit = 0
		
	if(state == 6):
		if(hit == 0):
			scarAlibi = "Miss Scarlet: I was in the kitchen this time, I saw Col. Mustard in there too. Please hurry detective, I'm getting scared!"
			handle_alibi(scarAlibi)
			plumAlibi = "Professor Plum: I was with Mrs. Peacock in the gardens. Check with her if you don't believe me. And make it quick! I don't want to be next."
			handle_alibi(plumAlibi)
			peacAlibi = "Mrs. Peacock: My memory is poor, sorry, but I think I was in the gardens. Did I see Professor Plum? Well I know I was talking to a gentleman... Was it him? Oh I'm sorry, I just can't remember."
			handle_alibi(peacAlibi)
			mustAlibi = "Colonel Mustard: I was in the library, honest! I know I was being difficult before, but now I just want this guy caught. No, I was by myself."
			handle_alibi(mustAlibi)
		
			who()
		if(hit > 0):
			state += 1
		hit += 1
		
	if(state == 7):
		#result
		maybeMurderer = request.form['Body']
		if(maybeMurderer == murderer):
			isM = 'right'
			state = 14
		else:
			ism = 'wrong'
			state += 1
		result = roundDecision(maybeMurderer, isM, len(characters))
		
	if(state == 8):
		killed = 'Mrs. Peacock'
		characters.remove('Mrs. Peacock')
		weapUsed = 'book'
		killLoc = 'kitchen'
		handle_roundPtOne(killed, weapUsed, killLoc)
		state += 1
		hit = 0
		
	if(state == 9):
		if(hit == 0):
			scarAlibi = "Miss Scarlet: I can't believe Mrs. Peacock is dead... She was a nice lady... I think I was in the library with Professor Plum around that time. Please save us detective!"
			handle_alibi(scarAlibi)
			plumAlibi = "Professor Plum: That poor old lady... What? Oh, I was in the library. I don't remember seeing anyone else, but it is quite large."
			handle_alibi(plumAlibi)
			mustAlibi = "Colonel Mustard: You are doing a terrible job! Let me make it easier for you, it's not me. I was in the study."
			handle_alibi(mustAlibi)
		
			who()
		if(hit > 0):
			state += 1
		hit += 1
		
	if(state == 10):
		#result
		maybeMurderer = request.form['Body']
		if(maybeMurderer == murderer):
			isM = 'right'
			state = 14
		else:
			ism = 'wrong'
			state += 1
		result = roundDecision(maybeMurderer, isM, len(characters))
		
	if(state == 11):
		killed = 'Colonel Mustard'
		characters.remove('Colonel Mustard')
		weapUsed = 'shovel'
		killLoc = 'garage'
		handle_roundPtOne(killed, weapUsed, killLoc)
		state += 1
		hit = 0
		
	if(state == 12):
		if(hit == 0):
			scarAlibi = "Miss Scarlet: It wasn't me! Oh please believe me detective! Professor Plum must've done it!"
			handle_alibi(scarAlibi)
			plumAlibi = "Professor Plum: Arrest Miss Scarlet immediately! She's clearly the culprit!"
			handle_alibi(plumAlibi)
		
			who()
		if(hit > 0):
			state += 1
		hit += 1
		
	if(state == 13):
		#result
		maybeMurderer = request.form['Body']
		if(maybeMurderer == murderer):
			isM = 'right'
		else:
			ism = 'wrong'
		result = roundDecision(maybeMurderer, isM, len(characters))
		state += 1
		
	if(state == 14):
		endResult = gameOver(outcome, rounds, len(suspects)-1)
		handle_gameOver(endResult)
		#would you like to play again? yes/no?
		playA = request.form['Body']
		if(playA == 'yes' | 'Yes'):
			state = 1
		else:
			state = 6
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
		body='The victim was ' + killed + '. ' + killed + ' was killed with a ' + weapUsed + ' in the ' + killLoc + '. Who would you like to hear from?',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])

def handle_guessConfirm():
	logger.debug(request.form)
	message = g.sms_client.messages.create(
		body='Sargeant: Got it Detective! Keep an eye on them while we solidy everything and prevent another attack.',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
	
def handle_roundPtTwo(result):
	logger.debug(request.form)
	message = g.sms_client.messages.create(
		body=result,
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

def handle_gameOver(endResult):
	logger.debug(request.form)
	
	message = g.sms_client.messages.create(
		body=endResult,
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
