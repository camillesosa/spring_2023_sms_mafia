import random

from tools.logging import logger

#class BasicMafia:
  #def __init__(self,state):
    #self.state = state
state = 1
while(state != 4):
  if (state == 1):
    # welcome message
    PlayerName = 'Cam'
    # name = input('Welcome Detective! Do you mind confirming your name before I go over the details of the case?\n')
    fn = getattr(__import__('open_calls.'+proc_name), proc_name)
    resp = fn.handle_welcome()
    #name = input after handle_welcome
    #logger.debug('Thank you Detective', name, ', we are happy to have you on this case. Unfortunately, there seems to be a killer on the loose! We have narrowed the suspects to five individuals: ')
    #maybe pass input from handle_welcome into handle_gameRules for name
    resp = fn.handle_gameRules()
    # suspect names
    logger.debug('Camella, Camille, Francesca, Luis, and Victor.\n')
    logger.debug('These five suspects were guests at a dinner party at Hill House, a secluded mansion in New England, where the murder took place. In an attempt to prevent escape, we have asked all the guests to stay there while we attempt to find the murderer, but the longer we take to find the murderer, the longer the innocents are in danger of also being attacked. I will take you to Hill House, so you can take a look at the evidence.')
    # randomly assign one suspect to be the murder

    # For testing
    killed = 'Mrs. White'
    suspects = ['Miss Scarlet', 'Professor Plum', 'Mrs. Peacock', 'Mr. Green', 'Colonel Mustard']
    murderer = suspects[random.randint(0, 4)]
    suspects.remove(murderer)
    # lose if array size < 2
    rounds = 1
    state = self.state + 1

        
  if (state == 2):
    print('Victim was', killed, 'and they were killed with [INSERT WEAPON] at the [INSERT LOCATION].')
    #Randomly murder weapon and murder location
    #For example, victim was killed with a hammer in the gardens
        
    #Randomly assign allibis (vague, with some conflicting
    #For example, someone says "Victor was with me in the kitchen at the time of the murder", but Victor said he was in the garage
    #send media files as well for murder weapon and location
        
    voted = "F"
    while (voted != "T"):
      text = input
      # fix this: recognizing text to pull out specific input
      # if(text[0-13] == 'The murderer is '):
      # take nickname out of input
      maybeMurderer = input('You think the murderer is... ')
      voted = "T"
            
    state = state + 1

        
  if (state == 3):
    if (maybeMurderer != murderer):
      print("Oh no!", maybeMurderer, "was not the murderer!")
      # look up nickname in citizen array, delete entry
      suspects.remove(maybeMurderer)
      if (len(suspects) > 1):
        # move on to next round
        print('Looks like the murderer is still out there. We need to find them before they attack again!')
                
        #pick new murder victim randomly
        killed = suspects[random.randint(0, suspects.len())]
        suspects.remove(killed)
        rounds = rounds + 1
        state = 2
      else:
        # murderer wins, go to end state
        print('Oh no! You failed to find the murderer in time :(\n The murderer was actually', murderer, ':(')
        state = 4

    if (maybeMurderer == murderer):
      print("Excellent job Detective!", murderer, "was the murderer!  Congrats, you win!")
      # win, go to end state
      if (rounds > 1):
        print('It took you', rounds, 'rounds to find the killer, and you saved', len(suspects)-1, 'people.\n')
      else:
        print('Wow! It only took you 1 round to find the killer, and you saved', len(suspects)-1, 'people!\n')
      state = 4


  if (state == 4):
    # end state
    # play again question?  maybe make it a vote?
    playAgain = input('Thanks for playing! Would you like to play again? yes/no\n')
    if (playAgain == 'yes'):
      state = 1
    if (playAgain == 'no'):
      print('Thanks again for playing!')
      state = 4
      #end script
