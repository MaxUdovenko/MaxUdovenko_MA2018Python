import simplegui
import random

secret_number = 0

def input_guess(guess):
    '''
    Input your number to guess the secret number
    '''
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
    

def new_game():
    '''
    Let`s start new game!
    '''
    print('New game')
    global secret_number 
    secret_number = random.randrange(0, 100)


def hint():
    '''
    This function is for testing. It shows secret number ;-)
    '''
    label3.set_text('Secret number is: {}. Please! Do not be a cheater!'.format(secret_number))

new_game()

frame = simplegui.create_frame('Guessing', 200, 300, 300)

label2 = frame.add_label('Current range is [0:100)', 300)

inp = frame.add_input('Input guess', input_guess, 250)
button1 = frame.add_button('Next try...', clear_input)

label1 = frame.add_label('', 200)

button2 = frame.add_button('Hint', hint)
label3 = frame.add_label('', 200)

