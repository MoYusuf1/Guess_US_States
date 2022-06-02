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
    answered = len(guessed_states)
    answer_state = screen.textinput(title=f"{answered}/50 States", prompt="Name a state").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    else:
        # I did wrote the prompt that way so it would center properly.
        choice = screen.textinput(title="WRONG", prompt="Would you like to start over? \n         "
                                                        "       Yes or No").title()
        if choice == "Yes":
            guessed_states.clear()
        elif choice == "No":
            break

# collects the missed states from the for loop below
missed_states = []

for state in all_states:
    if state in guessed_states:
        pass
    else:
        missed_states.append(state)

# converts the list into a dictionary
missed_states_dict = {"Missed States": missed_states}
# converts that dictionary to a pandas dataframe
missed_states_df = pandas.DataFrame(missed_states_dict)
# converts that data frame to a csv file
missed_states_df.to_csv("states_missed.csv")
