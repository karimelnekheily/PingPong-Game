# imported turtle  module
import turtle
import time

# screen
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
# tahdis el shasha
wind.tracer(0)
# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()  # mesh hayersem ay khetoyt 3ala shasha
madrab1.goto(-350, 0)
madrab1.shapesize(stretch_wid=5, stretch_len=1)

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()  # mesh hayersem ay khetoyt 3ala shasha
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  # mesh hayersem ay khetoyt 3ala shasha
ball.goto(0, 0)
ball.dx = 0.06
ball.dy = -0.06

# score
score = turtle.Turtle()
score1 = 0
score2 = 0
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player1: 0 player2: 0 ", align="center", font=("Courier", 24, "normal"))


# functions

def madrab1_UP():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)


def madrab1_Down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_UP():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_Down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard
def setup_keyboard():
    wind.listen()
    wind.onkeypress(madrab1_UP, "w")
    wind.onkeypress(madrab1_Down, "s")
    wind.onkeypress(madrab2_UP, "Up")
    wind.onkeypress(madrab2_Down, "Down")


setup_keyboard()

# game loop
while True:
    # update the screen
    wind.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player1: {} player2: {} ".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player1: {} player2: {} ".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # collision detection
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score1 == 3:
        display = turtle.Turtle()
        madrab1.hideturtle()
        madrab2.hideturtle()
        ball.hideturtle()
        display.speed(0)
        display.color("blue")
        score.penup()
        display.hideturtle()
        display.goto(0, 0)
        display.write("player1 WON!", align="center", font=("Courier", 24, "normal"))
        time.sleep(5)
        restart = wind.textinput("Restart", "Do you want to restart the game? (yes/no):")

        if restart and restart.lower() == "yes":
            score1 = 0
            score2 = 0
            madrab1.goto(-350, 0)
            madrab2.goto(350, 0)
            ball.goto(0, 0)
            ball.dx = 0.06
            ball.dy = -0.06
            madrab1.showturtle()
            madrab2.showturtle()
            ball.showturtle()
            display.hideturtle()
            display.clear()
            score.clear()
            score.write("player1: 0 player2: 0 ", align="center", font=("Courier", 24, "normal"))
            setup_keyboard()  # Reinitialize controls
            continue
        else:
            # Exit the game
            wind.bye()
            break
        # quit()





