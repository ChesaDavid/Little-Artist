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
player2_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2+123)

player1X = screen.get_width()/2
player1Y = screen.get_height()/2
player2X = screen.get_width()/2+156
player2Y = screen.get_width()/2 +123
rects = [player1,player2,prise]
def RedWins():
    global Redscore
    score_text = font.render(f'Red win with a score of : {Redscore}',True,(255,255,255))    
    screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2))
    GameOver()

def BlueWins():
    score_text = font.render(f'Blue win with a score of : {BlueScore}',True,(255,255,255))
    screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2))
    GameOver()
    
def collisions():
    global running
    if redMase > blueMase:
        score_text = font.render(f'Red win with a score of : {Redscore}',True,(255,255,255))    
        screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2))
        running = False
    
    elif blueMase > redMase:
        score_text = font.render(f'Blue win with a score of : {BlueScore}',True,(255,255,255))
        screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2))  
        running = False
    
def collections1():
    global Redscore
    global redMase
    Redscore = Redscore + Redscore_increment
    redMase = redMase + Redscore_increment*massToScoreRATIO
    
    
def collections2():
    global BlueScore
    global blueMase
    blueMase = blueMase + BlueScore_increment*massToScoreRATIO
    BlueScore = BlueScore + BlueScore_increment
    
def ReplacePries():
    global prise_pos
    global priseX
    global priseY
    priseX = random.randrange(10,1200)
    priseY = random.randrange(10,710)
    prise_pos= pygame.Vector2(priseX,priseY)
    pygame.draw.circle(screen,"yellow",prise_pos,10)

def GameOver():
    global keys
    global running
    global status
    time.sleep(4)
    while True:
        screen.fill("red")
        score_text = font.render(f'Press Q to exit game',True,(255,255,255))
        screen.blit(score_text, (screen.get_width() / 2, screen.get_height() / 2)-100)
        score_text1 = font.render(f'Press R to restart game',True,"white")
        screen.blit(score_text1,(screen.get_width() / 2, screen.get_height() / 2)+100)
        if keys[pygame.K_q]:
            running = False
            status = False
        if keys[pygame.K_r]:
            running = True
            status = False
            break

status = True
def UpdatePositions():
    global prise
    global player1
    global player2
    
    player2.update(player2_pos.x,player2_pos.y,blueMase,blueMase)
    player1.update(player_pos.x,player_pos.y,redMase,redMase)
    prise.update(prise_pos.x,prise_pos.y,10,10)
    
    if player1.collidepoint(prise_pos.x,prise_pos.y):
        ReplacePries()
        collections1()
    if player2.collidepoint(prise_pos.x,prise_pos.y):
        ReplacePries()
        collections2()
    if player1.collidepoint(player2_pos.x,player2_pos.y):
        ReplacePries()
        collisions()
    
    
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    width1 = player_pos.x-redMase/2
    width2 = player2_pos.x-blueMase/2
    heaight1 = player_pos.y+redMase/2
    heaight2 = player2_pos.y+blueMase/2
    widthPrise = prise_pos.x+5
    heaightPrise = prise_pos.y+5
    
    player2 = pygame.Rect(width1,heaight1,blueMase,blueMase)
    player1= pygame.Rect(width2,heaight2,redMase,redMase)
    prise = pygame.Rect(widthPrise,heaightPrise,10,10)

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
        player1Y -= 300 * dt
        UpdatePositions()
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
        player1Y += 300 * dt
        UpdatePositions()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
        player1X -= 300 * dt
        UpdatePositions()
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        player1X += 300 * dt
        UpdatePositions()
    
    if keys[pygame.K_w]:
        player2_pos.y -= 300 * dt
        player2Y -= 300 * dt
        UpdatePositions()
    if keys[pygame.K_s]:
        player2_pos.y += 300 * dt
        player2Y += 300 * dt
        UpdatePositions()
    if keys[pygame.K_a]:
        player2_pos.x -= 300 * dt
        player2X -= 300 * dt
        UpdatePositions()
    if keys[pygame.K_d]:
        player2_pos.x += 300 * dt
        player2X += 300 * dt
        UpdatePositions()
    
    if player_pos.x > 1280:
        BlueWins()
        running = False
    if player_pos.x < -1280:
        BlueWins()
        running = False
    if player_pos.y > 720:
        BlueWins()
        running = False
    if player_pos.x < 0:
        BlueWins()
        running = False
    if player_pos.y <0:
        BlueWins()
        running = False
        
    if player2_pos.x > 1280:
        RedWins()
        running = False
    if player2_pos.x < -1280:
        RedWins()
        running = False
    if player2_pos.y > 720:
        RedWins()
        running = False
    if player2_pos.x < 0:
        RedWins()
        running = False
    if player2_pos.y <0:
        RedWins()
        
        

    score_text = font.render(f'Score red: {Redscore}',True,(255,255,255))
    screen.blit(score_text, (10, 10))
    
    score_text = font.render(f'Score blue: {BlueScore}',True,(255,255,255))
    screen.blit(score_text, (600, 10))

    # flip() the display to put your work on screen
    player2 = pygame.Rect(blueMase,blueMase,blueMase,blueMase)
    player1= pygame.Rect(redMase,redMase,redMase,redMase)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
        
time.sleep(10)
GameOver()
time.sleep(10)
if running == False:
    pygame.quit()