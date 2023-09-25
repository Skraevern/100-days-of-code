import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("./50_states.csv")
states_list = data.state.to_list()

print(states_list)

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?"
)

if answer_state in states_list:
    print("Yay")


turtle.mainloop()
