import pandas as pd

# data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# data = data['Primary Fur Color']
# #print(data)
# empty = {}
# count_cin = 0
# count_grey = 0
# count_black = 0
#
# for i in data:
#     if i == 'Cinnamon':
#         count_cin += 1
#         empty[i] = count_cin
#     if i == 'Gray':
#         count_grey += 1
#         empty[i] = count_grey
#     if i == 'Black':
#         count_black += 1
#         empty[i] = count_black
#
# news = pd.DataFrame(empty.items(), columns= ['Color', 'Count'])
# news.to_csv('final.csv')

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Grey"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv('squirrel_count.csv')

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
data = pd.read_csv('50_states.csv')

turtle.shape(image)
vlad = turtle.Turtle()
score = 0


def new_turtle(states):
    vlad.penup()
    vlad.hideturtle()
    vlad.goto(state_x, state_y)
    vlad.write(f'{states}', align='center')


is_playing = True


while is_playing:
    exclusion_list = []
    if score == 0:
        chosen_state = screen.textinput(title='Guess the State', prompt='Whats another state?').capitalize()
    else:
        chosen_state = screen.textinput(title='Guess the State', prompt=f'{score}/50 states discovered').capitalize()
    for all_states in data['state']:
        if chosen_state == all_states:
            state = data[data['state'] == chosen_state]
            state_x = int(state['x'].values[0])
            state_y = int(state['y'].values[0])
            new_turtle(chosen_state)
            score += 1
        else:
            continue

screen.mainloop()
