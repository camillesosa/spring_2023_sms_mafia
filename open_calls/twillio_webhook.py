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



def handle_request():
	logger.debug(request.form)
	message = g.sms_client.messages.create(
		body='Welcome Detective! Do you mind confirming your name before I go over the details of the case?',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
	if(global state == 1):
		handle_welcome(request.form['Body'])
	global state += 1
	return json_response( status = "ok" )

def handle_welcome(name):
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		body='Thank you Detective ' + name,
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_gameRules():
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		#name = input after handle_welcome
		body='Thank you Detective BLANK we are happy to have you on this case. Unfortunately, there seems to be a killer on the loose! The victim is Mrs. White, and we have narrowed the suspects to five individuals: Miss Scarlet, Professor Plum, Mrs. Peacock, Mr. Green, and Colonel Mustard. These five suspects were guests at a dinner party at Hill House, a secluded mansion in New England, where the murder took place. In an attempt to prevent escape, we have asked all the guests to stay there while we attempt to find the murderer, but the longer we take to find the murderer, the longer the innocents are in danger of also being attacked. I will take you to Hill House, so you can take a look at the evidence.',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_roundPtOne():
	logger.debug(request.form)

	message = g.sms_client.messages.create(
		#victim, murder weapon, location, and time change each round
		#probably pass these as an argument for handle
		body='Victim was... Victim was killed by ... in... around these times: blank...',
		from_=yml_configs['twillio']['phone_number'],
		to=request.form['From'])
    	#print(request.form['Body'])
	return json_response( status = "ok" )

def handle_roundPtTwo():
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
