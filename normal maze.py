# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 400
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)
TITLE = "Trippy Maze - Ryan Woods"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

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
screen.fill(BLUE)

# Make a player
player1 =  [30, 20, 10, 10]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

# make walls
wall1 =  [0, 0, 20, 300]
wall2 =  [0, 0, 400, 20]
wall3 =  [380, 0, 20, 300]
wall4 =  [0, 280, 400, 20]
wall5 =  [0, 40, 60, 20]
wall6 =  [60, 0, 20, 30]
wall7 =  [60, 50, 20, 30]
wall8 =  [30, 70, 20, 50]
wall9 =  [50, 90, 50, 20]
wall10 =  [90, 0, 20, 90]
wall11 =  [30, 150, 20, 60]
wall12 =  [20, 190, 30, 20]
wall13 =  [30, 120, 70, 20]
wall14 =  [110, 90, 30, 50]
wall15 =  [120, 30, 20, 60]
wall16 =  [150, 40, 20, 160]
wall17 =  [180, 0, 20, 180]
wall18 =  [60, 150, 40, 20]
wall19 =  [50, 180, 60, 20]
wall20 =  [110, 150, 20, 50]
wall21 =  [130, 180, 20, 20]
wall22 =  [30, 220, 290, 20]
wall23 =  [30, 250, 10, 30]
wall24 =  [50, 250, 10, 30]
wall25 =  [70, 250, 10, 30]
wall26 =  [90, 250, 10, 30]
wall27 =  [110, 250, 10, 30]
wall28 =  [130, 250, 10, 30]
wall29 =  [150, 250, 10, 30]
wall30 =  [170, 250, 10, 30]
wall31 =  [190, 250, 10, 30]
wall32 =  [210, 250, 10, 30]
wall33 =  [230, 250, 10, 30]
wall34 =  [250, 250, 10, 30]
wall35 =  [270, 250, 10, 30]
wall36 =  [290, 250, 10, 30]
wall37 =  [310, 250, 10, 30]
wall38 =  [330, 250, 10, 30]
wall39 =  [350, 250, 10, 30]
wall40 =  [370, 250, 10, 30]
wall41 =  [170, 190, 110, 10]
wall42 =  [210, 50, 70, 10]
wall43 =  [210, 70, 70, 10]
wall44 =  [210, 90, 70, 10]
wall45 =  [210, 110, 70, 10]
wall46 =  [210, 130, 70, 10]
wall47 =  [210, 150, 70, 10]
wall48 =  [210, 170, 70, 10]
wall49 =  [210, 80, 10, 10]
wall50 =  [210, 120, 10, 10]
wall51 =  [210, 160, 10, 10]
wall52 =  [270, 60, 10, 10]
wall53 =  [270, 100, 10, 10]
wall54 =  [270, 140, 10, 10]
wall55 =  [270, 180, 10, 10]
wall56 =  [300, 20, 10, 30]
wall57 =  [290, 50, 10, 30]
wall58 =  [290, 90, 10, 30]
wall59 =  [290, 130, 10, 30]
wall60 =  [290, 170, 10, 50]
wall61 =  [310, 50, 10, 170]
wall62 =  [330, 130, 10, 110]
wall63 =  [350, 130, 10, 110]
wall64 =  [320, 130, 10, 10]
wall65 =  [340, 230, 10, 10]
wall66 =  [200, 20, 20, 10]
wall67 =  [230, 20, 30, 10]
wall68 =  [270, 20, 30, 10]
wall69 =  [200, 30, 10, 10]
wall70 =  [240, 30, 10, 10]
wall71 =  [280, 30, 10, 10]
wall72 =  [60, 200, 10, 10]
wall73 =  [100, 200, 10, 10]
wall74 =  [140, 200, 10, 10]
wall75 =  [180, 200, 10, 10]
wall76 =  [220, 200, 10, 10]
wall77 =  [260, 200, 10, 10]
wall78 =  [80, 210, 10, 10]
wall79 =  [120, 210, 10, 10]
wall80 =  [160, 210, 10, 10]
wall81 =  [200, 210, 10, 10]
wall82 =  [240, 210, 10, 10]
wall83 =  [280, 210, 10, 10]
wall84 =  [330, 110, 50, 10]
wall85 =  [320, 90, 50, 10]
wall86 =  [330, 70, 50, 10]
wall87 =  [320, 50, 50, 10]
wall88 =  [330, 30, 30, 10]
wall89 =  [360, 39, 20, 1]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
         wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39,
         wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58,
         wall59, wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73, wall74, wall75, wall76, wall77,
         wall78, wall79, wall80, wall81, wall82, wall83, wall84, wall85, wall86, wall87, wall88, wall89]

# Make coins
coin1 = [70, 140, 10, 10]
coin2 = [280, 100, 10, 10]
coin3 = [220, 240, 10, 10]
coin4 = [360, 20, 20, 19]


coins = [coin1, coin2, coin3, coin4]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up1 = pressed[pygame.K_UP]
    down1 = pressed[pygame.K_DOWN]
    left1 = pressed[pygame.K_LEFT]
    right1 = pressed[pygame.K_RIGHT]

    if left1:
        vel1[0] = -player1_speed
    elif right1:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

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
    hit_list = []
    '''

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
    '''
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coinsound.play()
        
    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLUE)

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        end.play()
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, WHITE)
        screen.blit(text, [200, 150])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
