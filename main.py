from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle2 = Paddle()
paddle1 = Paddle()
paddle1.goto(-350,0)

ball = Ball()


screen.listen()
screen.onkey(paddle2.move_up,"Up")
screen.onkey(paddle2.move_down,"Down")
screen.onkey(paddle1.move_up,"w")
screen.onkey(paddle1.move_down,"s")


game_is_on = True


while game_is_on:
    screen.update()
    ball.move()





screen.exitonclick()