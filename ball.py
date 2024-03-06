from turtle import Turtle




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move()
        self.x_move = 10
        self.y_move = 10


    def move(self):

        y_achse = self.ycor() + self.x_move
        x_achse = self.xcor() + self.y_move
        self.goto(x=x_achse,y=y_achse)
        
        

    def bounce(self):
        self.y_move *= -1
    

    
