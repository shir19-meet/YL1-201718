#import turtle

#turtle.forward(100)
#turtle.left(10)
#turtle.goto(25,-50)
#turtle.right(10)
#turtle.goto(50,50)
#turtle.left(10)
#turtle.goto(75,-50)
#turtle.right(10)
#turtle.goto(0,0)

import turtle

turtle.register_shape("shape_name",((50,0),(100,0),(100,-50),(75,-70),(50,-50)))
turtle.shape("shape_name")
turtle.left(90)



