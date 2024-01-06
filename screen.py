# Example file showing a circle moving on screen
import pygame
import sys
import os
import time
import random
# pygame setup
pygame.init()
pygame.font.init()
pygame.collidepoin

screen = pygame.display.set_mode((1280, 720))

score = 0
score_increment = 10

font = pygame.font.Font(None,32)

clock = pygame.time.Clock()
running = True
dt = 0
obstacle = pygame.Rect(200, 200, 50, 50)
bublle_collect = pygame.Rect(20,20,20,20)



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
obstacle_pos = pygame.Vector2(screen.get_width()/2+156,screen.get_height()/2+123)

def GameOver():
    screen.fill("red")
    pygame.draw.circle(screen, "red", player_pos, 0)
    score_text = font.render(f'Score: {score}',True,(255,255,255))
    screen.blit(score_text, (0, 0))
    time.sleep(5)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen,"blue",obstacle_pos,20)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        
    
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
        
        
    score_text = font.render(f'Score: {score}',True,(255,255,255))
    screen.blit(score_text, (10, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
GameOver()
pygame.quit()