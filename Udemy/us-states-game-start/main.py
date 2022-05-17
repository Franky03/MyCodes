import pandas as pd
import turtle
from turtle import Turtle, Screen


#Criar DataFrame e adicionar os estados em uma lista para conferir depois
data= pd.read_csv('./Udemy/us-states-game-start/50_states.csv')
states= data['state'].to_list()
states.sort()

# Criar a tela com o mapa dos eua
screen= Screen()
screen.title('US States Game')
imagem= './Udemy/us-states-game-start/blank_states_img.gif'
screen.addshape(imagem)
turtle.shape(imagem)

#Take the x and y in screen(map)
# def get_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_click)

#Criar uma lista para comparar com a lista dos estados
check_states=[]
missing_states= states.copy()
while check_states!= states:
    answer_state = screen.textinput(title=f'{len(check_states)}/50 States Correct', prompt="What's another state's name?").title()
    if answer_state in states:
        missing_states.remove(answer_state)
        check_states.append(answer_state)
        answer_row= data[data['state']== answer_state]
        pen= Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(int(answer_row['x']), int(answer_row['y']))
        pen.write(answer_state)
    check_states.sort()
    if answer_state=='Exit':
        break

new_data= pd.DataFrame(missing_states)
new_data.to_csv('./Udemy/us-states-game-start/states_to_learn.csv')

screen.exitonclick()