from turtle import Turtle




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move()


    def move(self):
        
        y_achse = self.ycor() + 10
        x_achse = self.xcor() + 10
        self.goto(x=x_achse,y=y_achse)
        