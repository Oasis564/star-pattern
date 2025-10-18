import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a circle
def draw_circle(color, x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw head
draw_circle("yellow", 0, 0, 100)

# Draw left eye
draw_circle("white", -35, 35, 15)
draw_circle("black", -35, 35, 5)

# Draw right eye
draw_circle("white", 35, 35, 15)
draw_circle("black", 35, 35, 5)

# Draw smile
pen.penup()
pen.goto(-40, -20)
pen.setheading(-60)
pen.width(5)
pen.color("black")
pen.pendown()
pen.circle(50, 120)  # Draw smile arc

# Hide turtle and finish
pen.hideturtle()
turtle.done()
