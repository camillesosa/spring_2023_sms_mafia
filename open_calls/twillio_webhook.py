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
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

#open file to grab responses
with open('some_responses.txt', 'r') as myfile:
	all_file = myfile.read()

def introduction():
	message = g.sms_client.messages.create(
		body='Welcome Detective! Do you mind confirming your name before I go over the details of the case?',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
	
def handle_request():
	#main
	global state
	logger.debug(request.form)
	if(state == 0):
		introduction()
	if(state == 1):
		handle_welcome(request.form['Body'])
		killed ='Mrs. White'
		suspects = ['Miss Scarlet', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard']
		murderer = suspects[random.randint(0, 4)]
		suspects.remove(murderer)
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
		#add alibis here
		handle_roundPtTwo(request.form['Body'])
	state += 1
	return json_response( status = "ok" )

def handle_welcome(name):
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		body='Thank you Detective ' + name + ', we are happy to have you on this case. Unfortunately, there seems to be a killer on the loose! The victim is Mrs. White, and we have narrowed the suspects to five individuals: Miss Scarlet, Professor Plum, Mrs. Peacock, Mr. Green, and Colonel Mustard. These five suspects were guests at a dinner party at Hill House, a secluded mansion in New England, where the murder took place. In an attempt to prevent escape, we have asked all the guests to stay there while we attempt to find the murderer, but the longer we take to find the murderer, the longer the innocents are in danger of also being attacked. I will take you to Hill House, so you can take a look at the evidence.',
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
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_roundPtTwo(maybeMurderer):
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		#player guessed right or wrong
		#if Suspects array is too small, print different message as player has lost
		#probably pass these as an argument for handle
		body='You were...',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_gameOver():
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		body='Thanks for playing!  Would you like to play again?',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )
