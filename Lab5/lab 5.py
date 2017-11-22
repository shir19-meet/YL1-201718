from turtle import Turtle
import turtle

##class Square(Turtle):
##    def __init__(self,size, shape,):
##        Turtle.__init__(self)
##        self.shape("square")
##        self.shapesize(size)
       

##    def random_color(self):
##        red = randon.randint(0,256)
##        green = random.randint(0,256)
##        blue = random.randint(0,256)
##        
        
##
##s1 = Square("square",10,)
turtle.register_shape("hexagon",((0,0),(50,0),(75,-25),(50,-50),(0,-50),(-25,-25),(0,0)))

class Hexagon(Turtle):
    def __init__ (self,size):
        turtle.__init__(self)
        self.shapesize(size)
        self.shape("hexagon")


h1= (10)
    
