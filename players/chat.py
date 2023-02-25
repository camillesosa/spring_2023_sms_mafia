import json
from players.actors import actor
import random


LOGIC = {}
with open('chatbot_comments.json', 'r') as myComm:
	LOGIC = json.loads(myComm.read())
	


class chat(actor):
	def __init__(self, phone_number):
		super().__init__(phone_number)
		self.score = 0
		
	
	def get_output(self,msg_input):
		
		
		msg = None
		for i in range( len(LOGIC[ "misc in" ]) ):
			msg = random.choice( LOGIC[ "misc in" ])
			if msg not in self.prev_msgs:
				break
				
		if msg == None:
			return [ random.Choice( LOGIC[ "misc in" ] ) ]
		else:
			return [ msg ]
