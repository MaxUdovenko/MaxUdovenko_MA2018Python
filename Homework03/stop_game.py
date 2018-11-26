import simplegui

value_to_change = 0
interval = 100

total_stops = 0
successful_stops = 0


def print_integer():
    global value_to_change
    value_to_change += 1
    print(value_to_change)

    
def draw_timer(canvas):
    global  total_stops, successful_stops
    
    canvas.draw_text(format(str(value_to_change)), [250,200], 36, "Red")
    
    canvas.draw_text('{x}/{y}'.format(x=successful_stops,y=total_stops), [420,40], 36, "Yellow")

    
def start_timer():
    timer.start()


def stop_timer():
    global value_to_change,total_stops, successful_stops
    
    if timer.is_running():
        total_stops = total_stops + 1
    
    if format(value_to_change)[-1] == '0' and timer.is_running():
        successful_stops = successful_stops + 1
        
    timer.stop()


def reset_timer():
    global value_to_change, total_stops, successful_stops
    total_stops = 0
    successful_stops = 0
    value_to_change = 0


def format(t):
    template = '0'*(4-len(str(t))) + str(t)
    
    return "{minutes}:{dsec}{sec}.{ms}".format(minutes=int(int(template[:2])/6),
                                               dsec=int(template[:2])%6,
                                               sec=template[-2],
                                               ms=template[-1])


timer = simplegui.create_timer(interval, print_integer)

frame = simplegui.create_frame("Homework #3", 500, 400)

frame.set_draw_handler(draw_timer)

frame.add_button("Start", start_timer, 200)
frame.add_button("Stop", stop_timer, 200)
frame.add_button("Reset", reset_timer, 200)

frame.start()
