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