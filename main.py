from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(fun=snake.move_up,key="Up")
screen.onkey(fun=snake.move_down,key="Down")
screen.onkey(fun=snake.move_forward,key="Right")
screen.onkey(fun=snake.move_backward,key="Left")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

#     Detect collision with food
    if food.distance(snake.snake_list[0]) < 20:
        food.new_food()
        snake.snake_increment()
        scoreboard.score_increase()


#     Detect Collision with wall
    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() > 280 or snake.snake_list[0].ycor() < -280:
        game_is_on=False
        scoreboard.game_over()
    for segment in snake.snake_list[1:]:
        if segment.distance(snake.snake_list[0]) < 10:
            game_is_on=False
            scoreboard.game_over()








screen.exitonclick()
