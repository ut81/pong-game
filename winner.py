from turtle import Turtle


class Winner(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
    def winner_1(self):
        self.goto(0,0)
        self.write("player 1 wins!!",align="center",font=("Courier",60,"normal"))
        
    def winner_2(self):
        
        self.goto(0,0)
        self.write("player 2 wins!!",align="center",font=("Courier",60,"normal"))
              
