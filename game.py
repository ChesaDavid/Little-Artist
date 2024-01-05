
from turtle import *
score = 0
highscore = 0

screen = Screen()
screenMinx = -screen.window_width()/2
screenMiny = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

player = Turtle()
player.goto(0, 0)
player.speed(10)
screen.mainloop()