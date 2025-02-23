import turtle

window  = turtle.Screen()
window.setup(800,600)
window.bgcolor("lightgreen")

# Left Paddle
lp = turtle.Turtle()  # create turtule object
lp.speed(0)
lp.shape("square")
lp.color("black")
lp.shapesize(stretch_len=1,stretch_wid=5)
lp.penup()
lp.goto(-390,0)

# Right paddle
rp = turtle.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("black")
rp.shapesize(stretch_len=1,stretch_wid=5)
rp.penup()
rp.goto(380,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(1)
ball.penup()
ball.dx = 10
ball.dy = 2

# score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player A: 0      player B: 0",align="center",font=("Ariel",24,"normal"))

# Paddle Move method
def lp_up():
    lp.sety(lp.ycor()+20)
def lp_down():
    lp.sety(lp.ycor()-20)
def rp_up():
    rp.sety(rp.ycor()+20)
def rp_down():
    rp.sety(rp.ycor()-20)

# paddle Move keys
window.listen()
if lp.ycor()-50 <= 300 : window.onkeypress(lp_up,'w')
window.onkeypress(lp_down,'s')
window.onkeypress(rp_up,'Up')
window.onkeypress(rp_down,'Down')

winner = turtle.Turtle()
winner.speed(0)
winner.penup()
winner.hideturtle()
winner.goto(0,0)

# screen stop
score_a = 0
score_b = 0
while True :
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1;
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 385:
        ball.setx(385)
        ball.dx *= -1;
        if score_a <= 5 : score_a += 1
        score.clear()
        score.write("player A: {}      player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
    #
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        if score_b <= 5 : score_b += 1
        score.clear()
        score.write("player A: {}      player B: {}".format(score_a,score_b) , align="center",font=("Ariel",24,"normal"))
    if ball.xcor() > 360 and ball.ycor() < (rp.ycor()+50) and ball.ycor() > (rp.ycor()-50):
        #ball.setx(380)
        ball.dx *= -1
    if ball.xcor() < -365 and ball.ycor() < (lp.ycor()+50) and ball.ycor() > (lp.ycor()-50):
        #ball.setx(-385)
        ball.dx *= -1
    if score_b == 5:
        winner.write("player B Won ..." , align ="center",font=("Arial",24,"normal"))
    elif score_a == 5:
        winner.write("player A Won ...",align ="center",font=("Arial",24,"normal"))



