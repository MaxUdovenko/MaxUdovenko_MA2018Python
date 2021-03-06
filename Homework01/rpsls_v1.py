# Rock-paper-scissors-lizard-Spock
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers

import random

def name_to_number(name):
    # convert name to number
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Incorrect name!'


def number_to_name(number):
    # convert number to a name
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Incorrect number!'
    

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
    if difference == 1 or difference == 2:
        print('Player wins!')
    elif difference == 3 or difference == 4:
        print('Computer wins!')
    elif difference == 0:
        print("Player and computer tie!")
    else:
        print("Incorrect input data")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
