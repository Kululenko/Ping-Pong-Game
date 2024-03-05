from turtle import Turtle, Screen



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.setheading(90)
        self.penup()
        self.goto(350,0)
        


    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move()


    def move(self):
        move_on = True
        y_achse = 0
        x_achse = 0
        while move_on:
            self.goto(y=y_achse,x=x_achse)
            y_achse += 10
            x_achse += 10