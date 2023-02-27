import yaml

from os.path import exists


from PIL import Image
import urllib.request


#open file to grab ip address for sending images
with open('ip.txt', 'r') as serip:
    ip = serip.read()
    
    
#create url link for citizenIcon
URL = "http://" + ip.strip() + "/static/citizenIcon.jpeg"
#create url link for citizensWinIcon
URLW = "http://" + ip.strip() + "/static/citizensWinIcon.jpeg"
#create url link for mafiaIcon
URLMob = "http://" + ip.strip() + "/static/mafiaIcon.jpg"
#create url link for mafiaWinsIcon
URLL = "http://" + ip.strip() + "/static/mafiaWinsIcon.jpeg"
#create url link for crimesceneIcon
URLS = "http://" + ip.strip() + "/static/crimesceneIcon.jpg"



def give_Me_A_Pic(picSelect):
	if(picSelect == 1):
		return URL
	elif(picSelect ==2):
		return URLW
	elif(picSelect == 3):
		return URLMob
	elif(picSelect == 4):
		return URLL
	elif(picSelect == 5):
		return URLS
