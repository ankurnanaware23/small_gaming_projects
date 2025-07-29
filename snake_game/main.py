from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True  # Control variable

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def game_loop():
    global game_is_on

    if not game_is_on:
        return  # Stop the loop

    snake.move()
    screen.update()
    screen.ontimer(game_loop, 100)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()



    # Detect collision with wall
    if (
        snake.head.xcor() > 280 or
        snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or
        snake.head.ycor() < -280
    ):
        game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            game_over()


def game_over():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()


game_loop()
screen.mainloop()
