import turtle as t

tim= t.Turtle()
screen= t.Screen()

def move_forward():
    tim.forward(10)
def move_left():
    new_heading= tim.heading() + 10
    tim.setheading(new_heading)
def move_right():
    new_heading= tim.heading() - 10
    tim.setheading(new_heading)
def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def curve():
    for i in range(180):
        tim.right(1)
        tim.forward(1)
def move_back():
    tim.backward(10)
        

#W= forwards
#S= backwards
#A= Counter-Clockwise
#D= Clockwise
#C= Clear drawing

screen.listen()

screen.onkey(key='w', fun= move_forward)
screen.onkey(key='s', fun= move_back)
screen.onkey(key='d', fun= move_right)
screen.onkey(key='a', fun= move_left)


screen.onkey(key='c', fun=screen_clear)
screen.onkey(key='f', fun= curve)
print(tim.pos())

screen.exitonclick()