from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
        self.shape("circle")

Ball_1 = Ball(100,"blue",3)
Ball_2 = Ball(50,"green",2)


def check_collision(Ball_1,Ball_2):
    D = math.sqrt(math.pow((Ball_2.xcor()-Ball_1.xcor()),2)+ math.pow((Ball_2.ycor()-Ball_1.ycor()),2))
    sum1= Ball_1.radius + Ball_2.radius
    if D <= sum1:
        print("there is a collision")

check_collision(Ball_1,Ball_2)
