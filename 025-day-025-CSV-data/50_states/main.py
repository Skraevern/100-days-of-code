import turtle
import pandas
from state_handler import StateObject

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state = StateObject()


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("./50_states.csv")
states_list = data.state.to_list()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?"
    )

    if answer_state in states_list:
        state_row = data[data.state == answer_state]
        x = state_row.x.item()
        y = state_row.y.item()
        state.write_state(answer_state, x, y)


turtle.mainloop()
