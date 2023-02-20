state = 0
while (state != 4):
    if (state == 1):
        # welcome message
        name = input('Welcome Detective! Do you mind confirming your name before I go over the details of the case?\n')
        print('Thank you Detective ', name, ', we are happy to have you on this case. Unfortunately, there seems to be a killer on the loose! We have narrowed the suspects to five individuals.')
        #suspect names
        print('These five suspects were guests at a dinner party at Hill House, a secluded mansion in New England, where the murder took place. In an attempt to prevent escape, we have asked all the guests to stay there while we attempt to find the murderer, but the longer we take to find the murderer, the longer the innocents are in danger of also being attacked. I will take you to Hill House, so you can take a look at the evidence.')
        #randomly assign one suspect to be the murder
        
        #For testing
        murderer = 'Camille'
        killed = 'Steve'
        suspects = ['Luis', 'Francesca', 'Camella', 'Camille', 'Victor']
        # lose if array size < 2
        state = state + 1

        
    if (state == 2):
        print('Victim was...')
        #Randomly pick murder time, murder weapon, and murder location
        #For example, murder occured sometime after 3 but before 5, victim was killed with a hammer in the gardens
        
        #Randomly assign allibis (vague, with some conflicting
        #For example, Victor was with me in the kitchen at 4, but Victor said he was in the garage
        #send media files as well
        
        voted = "F"
        while (voted != "T"):
            text = input
            # fix this: recognizing text to pull out specific input
            # if(text[0-13] == 'The murderer is '):
            # take nickname out of input
            maybeMafia = input('You think the mafia is... ')
            voted = "T"
        state = state + 1

        
    if (state == 3):
       if (maybeMurder != murderer):
            print("Oh no! ", maybeMurderer, " was not the murderer!")
            # look up nickname in citizen array, delete entry
            if (len(suspects) > 1):
                # move on to next round
                print('Looks like the murderer is still out there... Hopefully there are no more attacks...')
                state = 2
            if (len(suspects < 2):
                # mafia wins, go to end state
                print('Oh no! You failed to find the murderer in time :(')
                state = 4

        if (maybeMafia == mafia):
            print("Excellent job Detective! ", murderer, " was the murderer!  Congrats, you win!")
            # win, go to end state
            state = 4

        # look up nickname in citizen array, delete entry
        index = 0
        while (index < len(citizenArray)):
            if (citizenArray[index] == killed):
                citizenArray.remove(killed)
                index = len(citizenArray)
            else:
                index = index + 1



    if (state == 4):
        # end state
        # play again question?  maybe make it a vote?
        playAgain = input(
            'Thanks for playing! Would you like to play again? yes/no\n')
        if (playAgain == 'yes'):
            state = 1
        if (playAgain == 'no'):
            print('Thanks again for playing!')
            state = 4
        # end script
