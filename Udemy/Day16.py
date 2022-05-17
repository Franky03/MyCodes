import turtle as tl
import random

timmy= tl.Turtle()
timmy.shape("arrow")
timmy.hideturtle()

#Dashed Line

# for c in range(4):
#     for _ in range(10):
#         timmy.forward(5)
#         timmy.penup()
#         timmy.forward(5)
#         timmy.pendown()
#     timmy.right(90)
# timmy.speed(1)
# colors=['darkred', 'darkblue', 'chartreuse', 'yellow', 'purple', 'pink', 'deep sky blue', 'magenta', 'blue']
# def shap(numS):
#     for i in range(numS):
#         timmy.forward(100)
#         timmy.left(360/numS)



# for _ in range(3, 11):
#     col= random.choice(colors)
#     shap(_)
#     timmy.color(col)
#     colors.remove(col)

# Random Walk and Random color

tl.colormode(255)
def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color= (r, g ,b)
    return random_color

# directions= [0, 90, 180, 270]
# timmy.pensize(5)
# while True:
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

#Square
# for c in range(4):
#     timmy.forward(100)
#     timmy.left(90)

#SpiroGraph
tl.bgcolor("white")
timmy.pensize(2)
timmy.speed(0)
# for i in range(6):
#     for c in range(7):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.left(10)
def draw_spi(size):
    for _ in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)

draw_spi(5)


screen= tl.Screen()
screen.exitonclick()

