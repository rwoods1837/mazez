# Imports
import pygame
import intersects
import random
from walls import *

# Initialize game engine
pygame.init()


# Window
WIDTH = 400
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)
TITLE = "The MAZE game - Ryan Woods"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
playing = False

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RANDCOLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
coinsound = pygame.mixer.Sound("sounds/error.WAV")
end = pygame.mixer.Sound("sounds/start.WAV")
startgame = pygame.mixer.Sound("sounds/begin.WAV")
pygame.mixer.music.load("sounds/theme.ogg")
startscreen = pygame.image.load('imgs/ssc.PNG')
screen.fill(BLUE)

# Make a player
player1 =  [30, 20, 10, 10]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

# Make coins
coin1 = [70, 140, 10, 10]
coin2 = [280, 100, 10, 10]
coin3 = [220, 240, 10, 10]
coin4 = [360, 20, 20, 19]


coins = [coin1, coin2, coin3, coin4]

def setup():
    global player1, vel1, player1_speed, score1, coins
    player1 =  [30, 20, 10, 10]
    vel1 = [0, 0]
    player1_speed = 5
    score1 = 0
    win = False
    coins = [coin1, coin2, coin3, coin4]

def splash():
    screen.blit(startscreen, [0, 0])

def gameplay():    
    pygame.draw.rect(screen, WHITE, player1)
        
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    font = pygame.font.Font(None, 24)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, [1, 285])
 
def winx():
    end.play()
    screen.fill(BLACK)
    for w in walls:
        pygame.draw.rect(screen, BLACK, w)
    font = pygame.font.Font(None, 48)
    text = font.render("You Win!", 1, WHITE)
    screen.blit(text, [200, 150])

    font1 = pygame.font.Font(None, 32)
    text1 = font1.render("Score: " + str(score1), 1, WHITE)
    screen.blit(text1, [250, 200])

    font2 = pygame.font.Font(None, 20)
    text2 = font2.render("Press (R) to Restart", 1, WHITE)
    screen.blit(text2, [200, 250])
    
# Game loop
win = False
done = False
setup()
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = True
                startgame.play()
                pygame.mixer.music.play(-1)

            elif event.key == pygame.K_r:
                playing = False
                win = False
                setup()
                

    pressed = pygame.key.get_pressed()

    up1 = pressed[pygame.K_UP]
    down1 = pressed[pygame.K_DOWN]
    left1 = pressed[pygame.K_LEFT]
    right1 = pressed[pygame.K_RIGHT]
    skey = pressed[pygame.K_s]

    if left1:
        vel1[0] = -player1_speed
    elif right1:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if skey:
        score1 += 1
        coinsound.play()

    if up1:
        vel1[1] = -player1_speed
    elif down1:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0

    

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''




    ''' get the coins '''
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coinsound.play()
        
    if len(coins) == 0:
        win = True

    screen.fill(BLUE)

    if playing == False:
        splash()

    if playing == True:
        gameplay()

    if win == True:
        winx()

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
