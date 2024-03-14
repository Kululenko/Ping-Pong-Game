from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle2 = Paddle()
paddle1 = Paddle()
paddle1.goto(-350,0)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle2.move_up,"Up")
screen.onkey(paddle2.move_down,"Down")
screen.onkey(paddle1.move_up,"w")
screen.onkey(paddle1.move_down,"s")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #collision with paddle
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    #right misses
    if ball.xcor() > 400:
        ball.x_bounce()
        ball.home()
        scoreboard.l_score += 1
        scoreboard.score()
        


    #left misses
    if ball.xcor() < -400:
        ball.x_bounce()
        ball.home()
        scoreboard.r_score += 1
        scoreboard.score()




screen.exitonclick()