import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

from tools.logging import logger

import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []


with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

#open file to grab responses
with open('some_responses.txt', 'r') as myfile:
	all_file = myfile.read()


def handle_request():
	logger.debug(request.form)

	message = g.sms_client.messages.create(
			body=random.choice(all_file.splitlines()),
			from_=yml_configs['twillio']['phone_number'],
			to=request.form['From'])

	return json_response( status = "ok" )
