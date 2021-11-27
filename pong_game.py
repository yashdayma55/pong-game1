import turtle
import os
win_main=turtle.Screen()
win_main.title("pong_game by @YashDayma")
win_main.bgcolor("yellow")
win_main.setup(width=900,height=600)
win_main.tracer(0)


#score couter
score_a=0
score_b=0
#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)    
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)    
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
paddle_ball=turtle.Turtle()
paddle_ball.speed(0)    
paddle_ball.shape("circle")
paddle_ball.color("black")
paddle_ball.penup()
paddle_ball.goto(0,0)
paddle_ball.dx=0.55
paddle_ball.dy=0.55
#paddle_a func
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0  player B: 0",align="center",font=("courier",22,"normal"))
#keyboard binding for paddle a
win_main.listen()
win_main.onkeypress(paddle_a_up,"w")
win_main.onkeypress(paddle_a_down,"s")
win_main.onkeypress(paddle_b_up,"Up")
win_main.onkeypress(paddle_b_down,"Down")

#main loop
while True:
    win_main.update()

    paddle_ball.setx(paddle_ball.xcor()+paddle_ball.dx)
    paddle_ball.sety(paddle_ball.ycor()+paddle_ball.dy)

    if paddle_ball.ycor()>290:
        paddle_ball.sety(290)
        paddle_ball.dy*=-1
        os.system("play beep.mp3&")
    
    if paddle_ball.ycor()<-290:
        paddle_ball.sety(-290)
        paddle_ball.dy*=-1

    if paddle_ball.xcor()>390:
        paddle_ball.goto(0,0)
        paddle_ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("courier",22,"normal"))
    
    if paddle_ball.xcor()<-390:
        paddle_ball.goto(0,0)
        paddle_ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("courier",22,"normal"))
    #paddle and ball collision
    if (paddle_ball.xcor()>340 and paddle_ball.xcor()<350) and (paddle_ball.ycor()<paddle_b.ycor()+50 and paddle_ball.ycor()>paddle_b.ycor()-50):
        paddle_ball.setx(340)
        paddle_ball.dx*=-1
    
    if (paddle_ball.xcor()<-340 and paddle_ball.xcor()>-350) and (paddle_ball.ycor()<paddle_a.ycor()+50 and paddle_ball.ycor()>paddle_a.ycor()-50):
        paddle_ball.setx(-340)
        paddle_ball.dx*=-1
        
