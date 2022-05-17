from turtle import Turtle, Screen, shape
import random

screen= Screen()
screen.bgcolor('gray')
screen.setup(width=500,height=400)
bet= screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
y_pos=[180,120,60,2,-60,-120]
colors= ['purple', 'blue','green', 'yellow', 'orange', 'red']
turtles=[]

line= Turtle()
line.pensize(3)
line.hideturtle()
line.penup()
line.goto(x=230, y=200)
line.pendown()
line.goto(x=230, y=-200)


is_race_on= False

for c in range(0,6):
    new_turtle= Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[c])
    new_turtle.goto(x=-230, y= y_pos[c])
    turtles.append(new_turtle)
    

if bet:
    is_race_on= True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            wining= turtle.pencolor()
            if wining== bet:
                print(f"You've won! The {wining} turtle is winner!")
            else:
                print(f"You've lost! The {wining} turtle is winner!")
        
        rand= random.randint(0,10)
        turtle.forward(rand)



screen.exitonclick()

