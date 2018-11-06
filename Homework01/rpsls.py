# Rock-paper-scissors-lizard-Spock
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers

import random

def name_to_number(name):
    # convert name to number
    return {'rock': 0, 'Spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}.get(name, 'Incorrect name')


def number_to_name(number):
    # convert number to a name
    return {0: 'rock', 1: 'Spock', 2: 'paper', 3: 'lizard', 4: 'scissors'}.get(number, -1)
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print('\n')

    # print out the message for the player's choice
    print('Player choise is: {}'.format(player_choice))

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print("Computer's choice is: {}".format(comp_choice))

    # compute difference of comp_number and player_number modulo five
    difference = ((player_number - comp_number) % 5)

    # determine winner and print winner message
    print({ 1: 'Player wins!', 
            2: 'Player wins!', 
            3: 'Computer wins!', 
            4: 'Computer wins!'}.get(difference, "Player and computer tie!")
        ) 

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
