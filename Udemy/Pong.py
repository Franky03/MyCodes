from turtle import Turtle, Screen
import time

r_score=0
l_score=0

#SCREEN
screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0) #Quando desativa a animação vai ter que fazer vc mesmo

#PADDLE
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.shape('square')
        self.goto(position)
    
    def move_up(self):
        new_y= self.ycor()+50
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y= self.ycor()-50
        self.goto(self.xcor(), new_y)

r_paddle= Paddle((350,0))
l_paddle= Paddle((-350,0))


screen.listen()
screen.onkey(key='Up', fun= r_paddle.move_up)
screen.onkey(key='Down', fun= r_paddle.move_down)
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

#BALL
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.xmove=15
        self.ymove=15
        self.move_speed=0.1
    def move(self):
        new_x= self.xcor() + self.xmove
        new_y= self.ycor() + self.ymove
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.ymove *= -1
    
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
        
    def reset(self):
        self.goto(0,0)
        self.move_speed= 0.1
        self.bounce_x()

ball= Ball()

#SCORE

class Pen(Turtle):
    def __init__(self):
        super().__init__()
        global l_score, r_score
        self.pencolor('white')
        self.penup()
        self.hideturtle()
        self.refresh()

    def draw_line(self):
        self.goto(0,300)
        self.setheading(270)
        self.pendown()
        for _ in range(60):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()

        
    def refresh(self):
        self.clear()    
        self.goto(0,260)
        self.write(f"{l_score}          {r_score}", align= "center", font= ("candara", 25, "bold"))
        self.draw_line()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=("candara", 22, "bold"))

score= Pen()


#GAME
game_is_on= True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    elif ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()-320:
        ball.bounce_x()
    
    if ball.xcor()>390:
        l_score+=1
        ball.reset()
        score.refresh()
    elif ball.xcor()<-390:
        r_score +=1
        ball.reset()
        score.refresh()
        
screen.exitonclick()  