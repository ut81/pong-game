
from turtle import Screen,Turtle
import turtle
import time

from paddle import Paddle
from scoreboard import Scoreboard
from winner import Winner
from ball import Ball
    

    

s=Screen()
s.setup(width=800,height=600)
s.bgcolor("black")

s.tracer(0)



paddle_r=Paddle((350,0))   
paddle_l=Paddle((-350,0))   
ball=Ball() 
score=Scoreboard()
win=Winner()





s.listen()
s.onkey(paddle_r.go_up,"Up")
s.onkey(paddle_r.go_down,"Down")
s.onkey(paddle_l.go_up,"w")
s.onkey(paddle_l.go_down,"s")
game_on=True
while game_on:

    
    s.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()



    if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()<-320:

        ball.bounce_x()


    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()


    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

    if score.l_score==10 or score.r_score==10:
        game_on=False
        if score.l_score>score.r_score:
            win.winner_1()
            s.exitonclick()
        else:
            win.winner_2()
            s.exitonclick()







