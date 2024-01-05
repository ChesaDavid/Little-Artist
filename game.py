
from turtle import *
from keyboard import *
score = 0
highscore = 0

add_hotkey("left",lambda:Left())
add_hotkey("right",lambda:Right())
add_hotkey("up",lambda:Up())
add_hotkey("down",lambda:Down())

screen = Screen()
screenMinx = -screen.window_width()/2
screenMiny = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

player = Turtle()
player.goto(0, 0)
player.speed(10)

def Right():
    while is_pressed("left"):
        
def Left():
def Up():
def Down():

screen.mainloop()