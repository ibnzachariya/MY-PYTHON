import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("lightblue")

# Create turtles with different colors
colors = ["red", "green", "blue", "purple", "orange"]
turtles = []

start_y = -100
for color in colors:
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-200, start_y)
    turtles.append(racer)
    start_y += 50

# Ask user to guess
user_guess = screen.textinput("Make your bet!",
                              f"Which turtle will win? Choose from: {', '.join(colors)}")

# Draw finish line
finish_line = 200
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(finish_line, -150)
line.pendown()
line.left(90)
line.forward(300)

# Race simulation
winner = None
while not winner:
    for racer in turtles:
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= finish_line:
            winner = racer
            break

# Show result
time.sleep(1)
screen.clear()
screen.bgcolor("lightyellow")

winner_color = winner.color()[0]
if user_guess and user_guess.lower() == winner_color.lower():
    message = f"You guessed right! The {winner_color} turtle wins!"
else:
    message = f"Sorry, you guessed {user_guess}. The {winner_color} turtle wins!"

turtle.write(message, align="center", font=("Arial", 24, "bold"))

screen.mainloop()
