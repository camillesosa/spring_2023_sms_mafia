import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

from tools.logging import logger
from players.player import player

import random
import json
import pickle

from PIL import Image
import urllib.request



yml_configs = {}
BODY_MSGS = []


with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

#open file to grab responses
with open('some_responses.txt', 'r') as myfile:
	all_file = myfile.read()
	
#open file to grab ip address for sending images
with open('ip.txt', 'r') as serip:
    ip = serip.read()

#create url link for citizenIcon
URL = "http://" + ip.strip() + "/static/citizenIcon.jpeg"


#def image_setup:
#    img = Image.open(URL)
#    return img.show()
LOGIC = {}

def handle_request():
	logger.debug(request.form)
	
	#load pickle p if it exist
	act = None
	if exists( f"users/{request.form['From']}.pkl") :
		with open(f"users/{request.form['From']}.pkl", 'rb') as p:
			act = pickle.load(p)
	else:#save who the player is from 
		act = player(request.form['From'])
		output = act.get_output(request.form['Body'])
	
	
	for o_msg in output:

		message = g.sms_client.messages.create(
			body=o_msg,#random.choice(all_file.splitlines()),
			from_=yml_configs['twillio']['phone_number'],
			to=request.form['From'],
			media_url=[URL]
			#media_url=['http://54.183.213.231/static/citizenIcon.jpeg'])
    			#print(request.form['Body'])
    			
    	#write back the response to users pickle		
    	with open(f"users/{request.form['From']}.pkl", 'wb') as p:
    		pickle.dump( act, p)
    			
	return json_response( status = "ok" )
