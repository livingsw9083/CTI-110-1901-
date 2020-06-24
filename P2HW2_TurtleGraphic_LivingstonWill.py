# For this project, I have use the turtle graphics library to write programs that displays a shape.
# June 24, 2020
# CTI-110 P2HW2 - Turtle Graphic
# Will Livingston


# Start of the code.
import turtle # Displays python turtle graphics window.
turtle.bgcolor('gray') # Changes the background color.
turtle.speed(0) # Displays the speed of the turtle(0 displays instantly).
turtle.fillcolor('white') # Fill color of shape.
turtle.begin_fill() # Begins the fill for the inside of the shape.
turtle.hideturtle() # Hides the turtle.
# Start shape by drawing lines in the correct direction.
turtle.left(45) # Draws line to designated spots and directions.
turtle.forward(100)
turtle.right(90) 
turtle.forward(100)
turtle.right(90) 
turtle.forward(100)
turtle.right(90)
# Start of the second half of the shape.
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()# Ending fill so the shape can have color on the inside.

# End of the code

            







