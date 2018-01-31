from turtle import Turtle
import turtle
import random
from ball import Ball
import time
import math

turtle.tracer(0)
turtle.hideturtle()
RUNNING= True
SLEEP= 0.05
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

MY_BALL=Ball(0,0,0,0,30,"red")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range (NUMBER_OF_BALLS):
    x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH-MAXIMUM_BALL_RADIUS) 
    y=(random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
    dx=(random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX))
    dy=(random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY))
    radius=(random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS))
    color=(random.random(),random.random(),random.random())
    b2=Ball(x,y,dx,dy,radius,color)
    BALLS.append(b2)


def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)


def collide(ball_a,ball_b):
    if ball_a == ball_b:
       return False
    D = math.sqrt(math.pow(ball_b.xcor()-ball_a.xcor(),2)+ math.pow(ball_b.ycor()-ball_a.ycor(),2))+10

    if D <= ball_a.r +ball_b.r:
        return True
    else:
        return False
 

def check_all_balls_collisions():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a , ball_b):
                r1= ball_a.r
                r2= ball_b.r
                x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)   
                y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
                color=(random.random(),random.random(),random.random())
                if r2>r1:
                    ball_b.r+=1
                    ball_b.shapesize (ball_b.r/10)
                    ball_a.goto(x,y)
                    ball_a.dx = dx
                    ball_a.dy= dy
                    ball_a.r = radius
                    ball_a.shapesize (ball_a.r/10)
                    ball_a.color(color)

                else:
                    ball_a.r+=1
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.goto(x,y)
                    ball_b.dx = dx
                    ball_b.dy = dy
                    ball_b.r= radius
                    ball_b.shapesize(ball_b.r/10)
                    ball_b.color(color)

def check_myball_collision():
    for ball in BALLS:
        if collide(ball,MY_BALL):

            if ball.r>MY_BALL.r:
                return False
            else:
                x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)   
                y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
                color=(random.random(),random.random(),random.random())
                MY_BALL.r+=1
                MY_BALL.shapesize(MY_BALL.r/10)
                ball.goto(x,y)
                ball.dx = dx
                ball.dy = dy
                ball.r= radius
                ball.shapesize(ball.r/10)
                ball.color(color)



    return True



def movearound (event):
    mouse_X = event.x - SCREEN_WIDTH
    mouse_Y = SCREEN_HEIGHT - event.y
    MY_BALL.goto(mouse_X,mouse_Y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


while RUNNING == True:
    if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
         SCREEN_WIDTH == turtle.getcanvas().winfo_width()/2 
         SCREEN_HEIGHT == turtle.getcanvas().winfo_width()/2

    move_all_balls()
    check_all_balls_collisions()
    # MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING = check_myball_collision()

    turtle.getscreen().update()
    time.sleep(SLEEP)

turtle.mainloop()
         
         
   
        
    




                
            






