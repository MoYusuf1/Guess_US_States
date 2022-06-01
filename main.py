import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S Title Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title="Guess the State", prompt="Name a state").title()

    if answer_state == "Quit":
        break

    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(t)
    else:
        choice = screen.textinput(title="WRONG", prompt="Wrong! You probably misspelled...\n\n Would you like to start "
                                                        "over? \n\n Yes or No?")
        if choice == "Yes":
            guessed_states = []
        elif choice == "No":
            pass

