# Example file showing a circle moving on screen
import pygame
import sys
import os
import time
import random
# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))

Redscore = 0
Redscore_increment = 10

BlueScore = 0
BlueScore_increment = 10

massToScoreRATIO = 0.2

font = pygame.font.Font(None,32)

redMase = 20
blueMase = 20


clock = pygame.time.Clock()
running = True
dt = 0

player2 = pygame.Rect(blueMase,blueMase,blueMase,blueMase)
player1= pygame.Rect(redMase,redMase,redMase,redMase)
prise = pygame.Rect(10,10,10,10)


priseX = random.randrange(10,1200)
priseY = random.randrange(10,710)
prise_pos=pygame.Vector2(priseX,priseY)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width()/2+156,screen.get_height()/2+123)


def collisions():
    if redMase > blueMase:
        score_text = font.render(f'Red win with a score of : {Redscore}',True,(255,255,255))
        screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2))
    else:
        score_text = font.render(f'Blue win with a score of : {BlueScore}',True,(255,255,255))
        screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2))  
    time.sleep(4)   
    
    
def collections1():
    global Redscore
    global redMase
    Redscore = Redscore + Redscore_increment
    redMase = redMase + Redscore_increment*massToScoreRATIO
    
    
def collections2():
    global BlueScore
    global blueMase
    blueMase = blueMase + BlueScore_increment
    BlueScore = BlueScore + BlueScore_increment*massToScoreRATIO
    
def ReplacePris():
    global prise_pos
    global priseX
    global priseY
    priseX = random.randrange(10,1200)
    priseY = random.randrange(10,710)
    prise_pos= pygame.Vector2(priseX,priseY)
    pygame.draw.circle(screen,"yellow",prise_pos,10)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    pygame.draw.circle(screen,"yellow",prise_pos,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    player2 = pygame.Rect(blueMase,blueMase,blueMase,blueMase)
    player1= pygame.Rect(redMase,redMase,redMase,redMase)
    prise = pygame.Rect(10,10,10,10)

    pygame.draw.circle(screen,"yellow",prise_pos,10)
    
    
    # if pygame.Rect.collidepoint(player1,prise):
    #     collections1()
    # elif pygame.Rect.collidepoint(player2,prise):
    #     collections2()
    
    if redMase > blueMase:
        pygame.draw.circle(screen,"blue",player2_pos,blueMase)
        pygame.draw.circle(screen, "red", player_pos, redMase)
    elif blueMase > redMase:    
        pygame.draw.circle(screen, "red", player_pos, redMase)
        pygame.draw.circle(screen,"blue",player2_pos,blueMase)
    else:
        pygame.draw.circle(screen, "red", player_pos, redMase)
        pygame.draw.circle(screen,"blue",player2_pos,blueMase)
        
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        
        
    
    if keys[pygame.K_w]:
        player2_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player2_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player2_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player2_pos.x += 300 * dt
    
    if player_pos.x > 1280:
        running = False
    if player_pos.x < -1280:
        running = False
    if player_pos.y > 720:
        running = False
    if player_pos.x < 0:
        running = False
    if player_pos.y <0:
        running = False
        
    if player2_pos.x > 1280:
        running = False
    if player2_pos.x < -1280:
        running = False
    if player2_pos.y > 720:
        running = False
    if player2_pos.x < 0:
        running = False
    if player2_pos.y <0:
        running = False
        
    if prise_pos.x is player_pos.x+redMase/2 and player_pos.y is prise_pos.y:
        collections1()
    if prise_pos.x is player2_pos.x+redMase/2 and player2_pos.y is prise_pos.y:
        collections2()
        
    score_text = font.render(f'Score red: {Redscore}',True,(255,255,255))
    screen.blit(score_text, (10, 10))
    
    score_text = font.render(f'Score blue: {BlueScore}',True,(255,255,255))
    screen.blit(score_text, (600, 10))

    # flip() the display to put your work on screen
    player2 = pygame.Rect(blueMase,blueMase,blueMase,blueMase)
    player1= pygame.Rect(redMase,redMase,redMase,redMase)

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()