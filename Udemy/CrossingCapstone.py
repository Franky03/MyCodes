from turtle import Turtle, Screen
import time
import random

COLORS= ['red', 'darkred', 'blue', 'darkblue', 'green', 'darkgreen', 'black']
START= (0,-280)
STARTING_MOVE= 5
MOVE_INCREMENT=10
LEVEL=1

screen= Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)

#PLAYER

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start()
        self.shape('turtle')
        self.setheading(90)
    
    def move_up(self):
        new_y= self.ycor()+20
        self.goto(self.xcor(), new_y)
    
    def move_left(self):
        new_x= self.xcor()-20
        self.goto(new_x, self.ycor())
    
    def move_right(self):
        new_x= self.xcor()+20
        self.goto(new_x, self.ycor())
    
    def go_to_start(self):
        self.goto(START)

    def finish(self):
        if self.ycor()> 280:
            return True
        else:
            return False

turtle= Player()

screen.listen()
screen.onkey(turtle.move_up, 'Up')
screen.onkey(turtle.move_left, 'Left')
screen.onkey(turtle.move_right, 'Right')

#SCORE
class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        global LEVEL
        self.clear()
        self.goto(-260, 270)
        self.write(f'Level: {LEVEL}', align='center', font= ("candara", 16, "bold"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=("candara", 22, "bold"))
    

score= Pen()

#CAR
class Car(Turtle):
    def __init__(self):
        self.all_cars= []
        # super().__init__()
        # self.refresh()
    
    def create(self):
        chance= random.randint(1,6)
        if chance==1 or chance==2:
            new_car= Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y= random.randint(-250, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    
    def move(self):
        for cars in self.all_cars:
            new_x= cars.xcor()- STARTING_MOVE
            cars.goto(new_x, cars.ycor())

car= Car()

#GAME

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    if turtle.finish():
        LEVEL+=1
        score.refresh()
        STARTING_MOVE += 5
        turtle.go_to_start()
    for c in car.all_cars:
        if c.distance(turtle)<20:
            score.game_over()
            game_is_on=False
screen.exitonclick()