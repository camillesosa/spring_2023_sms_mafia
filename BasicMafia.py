state = 0
while (state != 4):
    if (state == 0):
        # welcome message
        print(
            'Welcome to Mafia! First and foremost, you will be assigned a nickname. Note: From here on out, you will only be identified by your nickname. Once everyone has been assigned a nickname, I will explain how to play the game!\n')
        # nick name assigner
        # put in dictionary here
        # (nickname, phonenumber)
        # rules
        print(
            'Here is how to play the game: A player is randomly selected to be the mafia, and their goal is to kill the citizens without being caught. The citizens goal, which are the rest of you, is to find and arrest the mafia! After each round, the killed player is revealed and the citizens will be allowed to discuss who the mafia is. Once a consensus is reached, one citizen will be asked to state the suspected mafia in the following format: The mafia is [nickname]. If you were right, then the citizens won!  If you were wrong however, the game will move on to the next round. The mafia has won when there is just one villager left standing.\n')
        state = state + 1

    if (state == 1):
        # message seperately and assign roles
        assignMafia = 'You are the mafia. You will use this chat to choose which citizen to kill. Please await further instructions.'
        # for testing
        mafia = 'Camille'
        assignCitizen = 'You are a citizen. Good luck and stay safe!'
        # put citizens in a dynamic array (nicknames)
        # for testing
        citizenArray = ['Luis', 'Francesca', 'Camella']
        # mafia win if array size < 2
        # choose random mafia, if mafia send assignMafia to number, send assignCitizen to everyone else

        print('The roles have now been assigned, get ready for the first round...')
        state = state + 1

    if (state == 2):
        print('Time for everyone to go to sleep...')

        # send to mafia privately
        forMafia = 'Who would you like to kill?  Please just text the nickname with no punctuation\n'
        killed = input(forMafia)
        # look up nickname in citizen array, delete entry
        index = 0
        while (index < len(citizenArray)):
            if (citizenArray[index] == killed):
                citizenArray.remove(killed)
                index = len(citizenArray)
            else:
                index = index + 1
        print('Got it, thanks!\n')

        # to group chat
        print('Goodmorning! Last night, it seems the mafia has attacked! There are ', (len(citizenArray)),
              ' of you left! ', killed,
              ' has been killed :( Someone here must be the mafia! Discuss who you think is the mafia, and once a consensus is reached, someone please state the suspected werewolf in the following format: The mafia is [nickname]')
        voted = "F"
        while (voted != "T"):
            text = input
            # fix this: recognizing text to pull out specific input
            # if(text[0-13] == 'The mafia is '):
            # take nickname out of input
            youThink = 'You think the mafia is... '
            maybeMafia = input('You think the mafia is... ')
            voted = "T"
        state = state + 1

    if (state == 3):
        if (maybeMafia != mafia):
            print("Oh no! ", maybeMafia, " was not the mafia!")
            # look up nickname in citizen array, delete entry
            if (len(citizenArray) > 1):
                # move on to next round
                print('Looks like the mafia is still out there... Hopefully there are no more attacks...')
                state = 2
            if (len(citizenArray) < 2):
                # mafia wins, go to end state
                print('Oh no! The mafia has won - congrats mafia!')
                state = 4

        if (maybeMafia == mafia):
            print("The villagers are safe! ", mafia, " was the mafia!  Congrats citizens, you have won!")
            # citizens win, go to end state
            state = 4

    if (state == 4):
        # end state
        # play again question?  maybe make it a vote?
        playAgain = input(
            'Thanks for playing! Would you like to play again? Note: nicknames would remain the same. yes/no\n')
        if (playAgain == 'yes'):
            state = 1
        if (playAgain == 'no'):
            print('Thanks again for playing!')
            state = 4
        # end script