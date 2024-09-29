import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)
score = 0
game_is_on = True


def get_input():
    return screen.textinput(title=f"{score}/50States Guessed", prompt="What's another state's name?")


def show_on_map(state):
    write_state = df[df.state.str.lower() == state]
    turtle.penup()
    turtle.goto(int(write_state.x), int(write_state.y))
    turtle.write(f"{state.title()}", font=('Arial', 8, 'normal'))
    turtle.goto(0, 0)


df = pandas.read_csv("50_states.csv")
all_states = df.state.str.lower().to_list()
guessed_states = []

while game_is_on:
    screen.update()
    user_answer = get_input().lower()
    for state in df.state:
        if user_answer.lower() in all_states and user_answer.lower() not in guessed_states:
            score += 1
            guessed_states.append(user_answer.lower())
            show_on_map(user_answer)
    if len(guessed_states) == 50:
        game_is_on = False

turtle.mainloop()
