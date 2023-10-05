from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
snake=Snake()
food = Food()
scoreboard=Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    #detecting collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()
    #detecting collisons with wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].xcor()<-280:
        scoreboard.game_over()
        game_is_on=False
    #detecting collisions with self
    for i in range(2,len(snake.segments)):
        if snake.segments[0].distance(snake.segments[i])<20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
