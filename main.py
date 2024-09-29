import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

#TODO 1 get user input
turtle.shape(image)
score = 0
game_is_on = True

def get_input():
    return screen.textinput(title=f"{score}/50States Guessed",prompt="What's another state's name?")


#TODO 2 get data frame
df = pandas.read_csv("50_states.csv")
all_states = df.state.str.lower().to_list()
guessed_states = []

#TODO 3 compare user input to data frame
while game_is_on:
    user_answer = get_input().lower()
    for state in df.state:
        if user_answer.lower() in all_states and user_answer not in guessed_states:
            print("Yay")
            get_input()
            score +=1
            guessed_states.append(user_answer)

#TODO 4 if correct show on map
#TODO 5 update title on input box
#TODO 1 get user input


turtle.mainloop()