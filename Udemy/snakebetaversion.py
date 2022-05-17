from turtle import Turtle, Screen
import random
import time

is_on= True
score=0
highscore=0
sp= 1

UP= 90
DOWN= 270
LEFT= 180
RIGHT= 0

screen= Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

#Create The Snake's Food

food= Turtle()
food.penup()
colors= ["blue", "red", "green", "yellow"]
shapes= ["square", "triangle", "circle"]
food.color(random.choice(colors))
food.shape(random.choice(shapes))
x= random.randint(-280, 280)
y= random.randint(-280, 280)
food.goto(x, y)
food.shapesize(0.8)

x= random.randint(-280, 280)
y= random.randint(-280, 280)
food.goto(x, y)


#Create Snake 

start_pos=[(0, 0), (-20, 0), (-40, 0)]
segments=[]

for position in start_pos:
    snake= Turtle()
    snake.penup()
    snake.color('white')
    snake.shape('square')
    snake.goto(position)
    snake.speed(1)
    segments.append(snake)

head= segments[0]

#Put the Score in screen
pen= Turtle()
pen.pencolor("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)

#Functions to move the snake

def move_forward():
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x= segments[seg_num-1].xcor()
        new_y= segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    head.forward(20)


def mlef():
    if head.heading() != RIGHT:
        head.setheading(LEFT)

def mrig():
    if head.heading() != LEFT:
        head.setheading(RIGHT)

def mup():
    if head.heading() != DOWN:
        head.setheading(UP)
def mdown():
    if head.heading() != UP:
        head.setheading(DOWN)

#Keys move

screen.listen()
screen.onkey(key= 'Up', fun= mup)
screen.onkey(key='Down', fun= mdown)
screen.onkey(key='Right', fun= mrig)
screen.onkey(key='Left', fun= mlef)



# Create the Game

while is_on:
    pen.write(f"Score : {score}  High Score : {highscore}", align= "center", font= ("candara", 12, "bold"))
    # segments[0].speed(sp)
    move_forward()
    if snake.xcor()>= 288 or snake.xcor() <= -288:
        is_on=False
        # for segment in segments:
        #     segment.goto(1000,1000)
        # segments.clear()
    elif snake.ycor() >=298 or snake.ycor() <=-298:
        is_on= False
        # for segment in segments:
        #     segment.goto(1000,1000)
        # segments.clear()
    for segment in segments:
        if segment== head:
            pass
        elif head.distance(segment)<10:
            is_on= False

    if snake.distance(food)< 20:
        x= random.randint(-280, 280)
        y= random.randint(-280, 280)
        food.goto(x, y)
        food.color(random.choice(colors))
        food.shape(random.choice(shapes))
        new_seg= Turtle()
        new_seg.speed(sp)
        new_seg.shape("square")
        new_seg.color('orange')
        new_seg.penup()
        segments.append(new_seg)
        score+=1
        sp += 2

        if score>highscore:
            highscore= score

        pen.clear()
        pen.write(f"Score : {score}  High Score : {highscore}", align= "center", font= ("candara", 12, "bold"))
        
        head.speed(sp)


        

screen.exitonclick()
