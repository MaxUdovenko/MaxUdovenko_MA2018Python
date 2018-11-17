import simplegui
import random
import math

secret_number = 0
tries = -1

def input_guess(guess):
    '''
    Input your number to guess the secret number
    '''
    global tries

    if tries == 0:
        label1.set_text('The game is over! New secret number has generated!')
        print('The game is over! New secret number has generated!')
        new_game()
        
    else:
        tries = tries - 1
        
        label_try.set_text('{} tries to end'.format(tries))
    
        if len(guess) == 0:
            # in case user press the button but input field is empte
            guess = 0

        print('Guess was {}'.format(int(guess)))

        guess = int(guess)

        if guess == secret_number:
            label1.set_text('{} is Correct.\nYou may play another game. The random number has generated'.format(guess))
            new_game()

        elif guess < secret_number:
            label1.set_text('{} is Lower'.format(guess))

        else:
            label1.set_text('{} is Higher'.format(guess))
    

def clear_input():
    '''
    Input field cleared and ready for next number
    '''
    input_guess(inp.get_text())
    inp.set_text('')
    label3.set_text('')
    

def new_game(rrange=100):
    '''
    Let`s start new game!
    '''
    print('New game')
    global secret_number 
    secret_number = random.randrange(0, rrange)
    label3.set_text('')
    
    global tries
    tries = math.ceil(math.log(rrange,2))
    label_try.set_text('{} tries to end'.format(tries))


def hint():
    '''
    This function is for testing. It shows secret number ;-)
    '''
    label3.set_text('Secret number is: {}. Please! Do not be a cheater!'.format(secret_number))

    
def change_range_100():
    label2.set_text('Current range is [0:100)')
    new_game()


def change_range_1000():
    label2.set_text('Current range is [0:1000)')
    new_game(rrange=1000)


frame = simplegui.create_frame('Guessing', 200, 300, 300)

label2 = frame.add_label('Current range is [0:100)', 300)
label_try = frame.add_label('', 300)

inp = frame.add_input('Input guess', input_guess, 250)
button1 = frame.add_button('Next try...', clear_input)

label1 = frame.add_label('', 200)

button2 = frame.add_button('Hint', hint)
label3 = frame.add_label('', 200)

# "Rangeis[0,100)"
button3 = frame.add_button('New game Rangeis[0,100)', change_range_100)

# "Rangeis[0,1000)"
button4 = frame.add_button('New game Rangeis[0,1000)', change_range_1000)

new_game()