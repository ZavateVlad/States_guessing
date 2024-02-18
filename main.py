import csv
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
data = pd.read_csv('50_states.csv')
turtle.shape(image)

write_turtle = turtle.Turtle()
score = 0
exclusion_list = []
not_guessed = []


def new_turtle(states):
    write_turtle.penup()
    write_turtle.hideturtle()
    write_turtle.goto(state_x, state_y)
    write_turtle.write(f'{states}', align='center')


is_playing = True


while is_playing:
    if score == 0:
        chosen_state = screen.textinput(title='Guess the State', prompt='Whats another state?').title()
    else:
        chosen_state = screen.textinput(title='Guess the State', prompt=f'{score}/50 states discovered').title()

        if chosen_state in exclusion_list:
            chosen_state = screen.textinput(title='Guess the State', prompt='State already chosen!').title()

    for all_states in data['state']:
        not_guessed.append(all_states)
        if chosen_state == all_states:
            state = data[data['state'] == chosen_state]
            exclusion_list.append(chosen_state)
            state_x = int(state['x'].values[0])
            state_y = int(state['y'].values[0])
            new_turtle(chosen_state)
            score += 1

    if chosen_state == 'Exit':
        is_playing = False
        final_list = list(set(not_guessed) - set(exclusion_list))
        with open('guessed_states.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for element in final_list:
                writer.writerow([element])



