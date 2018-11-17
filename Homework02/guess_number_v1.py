# https://py3.codeskulptor.org/#user302_KXdZ6yHDuQ_4.py
import simplegui
import random

secret_number = 0

def input_guess(guess):
    print('Guess was {}'.format(int(guess)))
    
    guess = int(guess)
    
    if guess == secret_number:
        label1.set_text('{} is Correct'.format(guess))
        
    elif guess < secret_number:
        label1.set_text('{} is Lower'.format(guess))
        
    else:
        label1.set_text('{} is Higher'.format(guess))
    

def clear_input():
    input_guess(inp.get_text())
    inp.set_text('')
    
def new_game():
    global secret_number 
    secret_number = random.randrange(0, 100)


new_game()
frame = simplegui.create_frame('Guessing', 200, 200, 300)
inp = frame.add_input('Input guess', input_guess, 250)
button1 = frame.add_button('Next try...', clear_input)
label1 = frame.add_label('', 200)

# For testing
# print(secret_number)
