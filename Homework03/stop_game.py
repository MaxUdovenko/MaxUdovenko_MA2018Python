import simplegui

counter = 0
interval = 100

total_stops = 0
successful_stops = 0


def print_integer():
    '''prints value to console'''
    global counter
    counter += 1
    print(counter)

    
def draw_timer(canvas):
    '''draws times & stops counter on canvas'''
    global  total_stops, successful_stops
    
    canvas.draw_text(format(counter), [250,200], 36, "Red")
    canvas.draw_text('{x}/{y}'.format(x=successful_stops, y=total_stops), [420,40], 36, "Yellow")

    
def start_timer():
    timer.start()


def stop_timer():
    global counter, total_stops, successful_stops
    
    # timer.is_running()
    # https://py3.codeskulptor.org/docs.html#timer-is_running
    if timer.is_running():
        total_stops += 1
    
    if format(counter)[-1] == '0' and timer.is_running():
        successful_stops += 1
        
    timer.stop()


def reset_timer():
    global counter, total_stops, successful_stops

    total_stops = successful_stops = counter = 0


def format(counter_value):
    template = '0'*(4-len(str(counter_value))) + str(counter_value)
    
    return "{minutes}:{dsec}{sec}.{ms}".format(minutes=int(int(template[:2])/6),
                                               dsec=int(template[:2])%6,
                                               sec=template[-2],
                                               ms=template[-1])


# --- MAIN --- --- --- --- --- --- --- --- --- --- --- ---
timer = simplegui.create_timer(interval, print_integer)

frame = simplegui.create_frame("Homework #3", 500, 400)

frame.set_draw_handler(draw_timer)

frame.add_button("Start", start_timer, 200)
frame.add_button("Stop", stop_timer, 200)
frame.add_button("Reset", reset_timer, 200)

frame.start()
