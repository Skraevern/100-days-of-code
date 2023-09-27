import turtle
import pandas
from state_handler import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

arrow = StateWriter()

score = 0
guessed_states = []

# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("./50_states.csv")
states_list = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"Guess the State. {score}/50", prompt="What's another state's name?"
    ).title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        arrow.write_state(answer_state, state_row.x.item(), state_row.y.item())
        score += 1
        screen.title(f"U.S. States Game.")

remaining_states = [state for state in states_list if state not in guessed_states]
remaining_states_frame = pandas.DataFrame(remaining_states)
remaining_states_frame.to_csv("./states_to_learn")
