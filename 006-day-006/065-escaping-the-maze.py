# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() == False:
    if wall_on_right() == False:
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

"""