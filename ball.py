from turtle import Turtle




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):

        y_achse = self.ycor() + self.y_move
        x_achse = self.xcor() + self.x_move
        self.goto(x=x_achse,y=y_achse)
        
        

    def y_bounce(self):
        self.y_move *= -1
    

    def x_bounce(self):
        self.x_move *= -1
