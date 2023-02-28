#import yaml
#from flask import request, g
#from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

#from tools.logging import logger

from PIL import Image
#import urllib.request

#yml_configs = {}
BODY_MSGS = []

#with open('config.yml', 'r') as yml_file:
#    yml_configs = yaml.safe_load(yml_file)


#open file to grab ip address for sending images
with open('ip.txt', 'r') as serip:
    ip = serip.read()
    
    
#create url link for citizenIcon
URL = "http://" + ip.strip() + "/static/citizenIcon.jpeg"
#create url link for citizensWinIcon
URLW = "http://" + ip.strip() + "/static/citizensWinIcon.jpeg"
#create url link for wolfIcon
URLwolf = "http://" + ip.strip() + "/static/wolf.jpg"
#create url link for wolfWinsIcon
URLwolfW = "http://" + ip.strip() + "/static/wolf.jpeg"
#create url link for crimesceneIcon
URLS = "http://" + ip.strip() + "/static/crimesceneIcon.jpg"



def give_Me_A_Pic(picSelect):
	if(picSelect == 1):
		return URL
	elif(picSelect ==2):
		return URLW
	elif(picSelect == 3):
		return URLwolf
	elif(picSelect == 4):
		return URLwolfW
	elif(picSelect == 5):
		return URLS
