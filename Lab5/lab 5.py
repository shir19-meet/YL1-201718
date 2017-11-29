from turtle import Turtle
import turtle

class Square(Turtle):
    def __init__(self,size, shape,):
        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(size)
       

##    def random_color(self):
##        red = randon.randint(0,256)
##        green = random.randint(0,256)
##        blue = random.randint(0,256)
##        
        
##
##s1 = Square("square",10,)
class Hexagon(Turtle):
    def __init__(self,size,speed,color):
        Turtle.__init__(self)
        self.speed(speed)
        self.color(color)
        
        self.home()
        self.penup()
        self.begin_poly()
        self.fd(100)
        self.left(-300)
        self.fd(100)
        self.right(300)
        self.fd(100)
        self.right(300)
        self.fd(100)
        self.left(-300)
        self.fd(100)
        self.left(-300)
        self.fd(100)
        self.end_poly()
        p = self.get_poly()
        turtle.register_shape("hexagon",p)
        self.shape("hexagon")

    def draw_triangle(self,size):
        self.pendown()
        self.forward(size)
        self.right(120)
        self.forward(size)
        self.right(120)
        self.forward(size)

    
    
        

h1=Hexagon(10,0,"blue")
h1.draw_triangle(100)


##
##
##    def __init__ (self,size):
##        turtle.__init__(self)
##        self.shapesize(size)
##        self.shape("hexagon")
##
##
#h1= (10)

