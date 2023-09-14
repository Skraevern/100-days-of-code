#Use a Debugger

# https://pythontutor.com/render.html#mode=display

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item) ## Missing indentation
    print(b_list)

mutate([1,2,3,5,8,13])

