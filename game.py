import turtle
import random
import math

screen = turtle.Screen()
screen.title("My game by python code")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Making the user 'bubble'
bubble = turtle.Turtle()
bubble.color("red")
bubble.shape("circle")
bubble.penup()
speed = 3

# Making the collection balls
collection_ball = turtle.Turtle()
collection_ball.color("red")
collection_ball.penup()
collection_ball.shape("circle")
collection_ball.shapesize(0.5, 0.5, 0.5)
ball_cor1 = random.randint(30, 280)
ball_cor2 = random.randint(30, 280)
collection_ball.setposition(ball_cor1, ball_cor2)
collection_ball.color("yellow")

# Scoring
points = turtle.Turtle()
points.color("yellow")
style = ('Courier', 30, 'italic')
points.penup()
points.goto(-200, 250)
points.write("Points: 0", font=style)
points.hideturtle()

# Turning
def turn_left():
    bubble.left(90)


def turn_right():
    bubble.right(90)


# Collection of the balls
def collection(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 20


def collection_ball_restart():
    collection_ball.color("black")
    ball_cor1 = random.randint(30, 280)
    ball_cor2 = random.randint(30, 280)
    collection_ball.goto(ball_cor1, ball_cor2)
    collection_ball.color("yellow")
    bubble.forward(speed)
    screen.ontimer(play_game, 10)


def play_game():
    if collection(bubble, collection_ball):
        score = 0
        score += 2
        points.clear()
        points.write("Points: " + str(score), font=style)
        collection_ball_restart()
        bubble.forward(speed)

    else:
        bubble.forward(speed)
        screen.ontimer(play_game, 10)


turtle.onkeypress(turn_left, "Left")
turtle.onkeypress(turn_right, "Right")

screen.listen()

play_game()

screen.mainloop()