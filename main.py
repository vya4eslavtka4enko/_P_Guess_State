import csv
import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(width=700, height= 500)
turtle.shape(image)
guess_states = []

while len(guess_states) < 50:
    data = pandas.read_csv('50_states.csv')
    all_state = data.state.to_list()
    answer_state = screen.textinput(title = f'{len(guess_states)}/50 states correct', prompt = "What's another state's name ? ").title()
    # print(answer_state)
    if answer_state == 'Exit':
        with open('score.csv', 'w') as score:
            score.write(f'{len(guess_states)}')
            print(len(guess_states))
        break
    if answer_state in all_state:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()