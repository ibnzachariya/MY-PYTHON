import turtle

# Create the turtle and screen
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Turtle Drawing App")

# Movement functions
def move_up():
    t.setheading(90)   # North
    t.forward(20)

def move_down():
    t.setheading(270)  # South
    t.forward(20)

def move_left():
    t.setheading(180)  # West
    t.forward(20)

def move_right():
    t.setheading(0)    # East
    t.forward(20)

# Pen control
def pen_up():
    t.penup()

def pen_down():
    t.pendown()

# Clear screen
def clear_screen():
    t.clear()
    t.home()  # Reset turtle to center

# Color controls
def set_red():
    t.pencolor("red")

def set_blue():
    t.pencolor("blue")

def set_green():
    t.pencolor("green")

def set_black():
    t.pencolor("black")

# Key bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(clear_screen, "c")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")

# Color bindings
screen.onkey(set_red, "r")
screen.onkey(set_blue, "b")
screen.onkey(set_green, "g")
screen.onkey(set_black, "k")  # 'k' for black

# Keep window open
screen.mainloop()
