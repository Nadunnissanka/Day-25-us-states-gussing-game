import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(725, 491)
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
count = 0
guessed_states = []
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{count}/50 Guess the state", prompt="What's another state's name?").title()
    if count >= 50:
        game_is_on = False
    else:
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = Turtle()
            t.hideturtle()
            t.penup()
            selected_state = data[data.state == answer_state]
            t.goto(int(selected_state.x), int(selected_state.y))
            t.write(answer_state)
            count += 1
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        data_dict = {
            "missing state name": missing_states
        }
        df = pandas.DataFrame(data_dict)
        df.to_csv("learn.csv")
        game_is_on = False

# states to learn.csv

screen.exitonclick()



