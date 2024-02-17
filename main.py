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
