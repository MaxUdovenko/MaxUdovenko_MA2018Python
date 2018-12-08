# implementation of card game - Memory

import simplegui
import random

shift = 50

shaffled_list = list()

click = 0
buffer = -1

counter = 0

# helper function to initialize globals
def new_game():
    global shaffled_list, state_list, counter
    
    counter = 0
    counter_label.set_text('Turns = {}'.format(counter))
    
    shaffled_list = [str(x) for x in range(8)] * 2
    random.shuffle(shaffled_list)
    
    for item in range(16):
        shaffled_list[item] = { 'flipped': 0, 'pinned': 0, 'value': shaffled_list[item],}


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global click, buffer, counter
    
    flipped_card = pos[0]//50
    if shaffled_list[flipped_card]['pinned'] == 0:
        # •	1 pt - The game ignores clicks on exposed cards.
        counter += 1
        counter_label.set_text('Turns = {}'.format(counter))
    
    if click == 0:
        if buffer > -1:
            shaffled_list[buffer]['flipped'] = 0
            
        shaffled_list[flipped_card]['flipped'] = 1
        buffer = flipped_card
        click = 1
    else:
        shaffled_list[flipped_card]['flipped'] = 1
        
        if shaffled_list[flipped_card]['value'] == shaffled_list[buffer]['value']:
            click = 0
            shaffled_list[buffer]['pinned'] = 1
            shaffled_list[flipped_card]['pinned'] = 1
            buffer = -1
        else:
            # click = 0
            shaffled_list[buffer]['flipped'] = 0
            buffer = flipped_card


# cards are logically 50x100 pixels in size    
def draw(canvas):
    for item in range(16):
        if shaffled_list[item]['flipped'] == 0:    
            canvas.draw_polygon([(shift*item, 0), 
                                 (shift*item, 100), 
                                 ((shift*item)+50,100), 
                                 ((shift*item)+50,0)], 2, 'Red', 'Green')
            
        elif shaffled_list[item]['flipped'] == 1 or shaffled_list[item]['pinned'] == 1:
            canvas.draw_text(shaffled_list[item]['value'],[shift*item+10,75],60, "White")
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
counter_label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric