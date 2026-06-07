from turtle import Screen,Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)


# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

#OR check the snake.py
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#DETECT COLLISION WITH WALL
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 18:
            scoreboard.reset()
            snake.reset()


    #OR
    # #using slicing method
    # for segment in snake.segments[1:]:
    #     if segment == snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
#if head collides with any segment in the tail:
     #trigger game_over

screen.exitonclick()