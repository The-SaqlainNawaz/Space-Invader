# importing  Libararies
import pygame
import random
import math

# initializing pygame
pygame.init()

# setting Screen Width and Height
screen = pygame.display.set_mode((800, 600))

# setting thr title of the screen
pygame.display.set_caption("Space Inavaders")

# Loading the logo icon for Screen and setting into Screen Left corner
pygame.display.set_icon(pygame.image.load("spaceship.png"))

# Background image
back_image = pygame.image.load("2293.jpg")

# Player
playerX = 370
playerY = 480
player_Image = pygame.image.load("arcade-game.png")
player_Change = 0

# Game Over
gamer_over_Style = pygame.font.Font("freesansbold.ttf", 64)
game_textX = 200
game_textY = 250


def game_Over_text():
    over_text = gamer_over_Style.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (game_textX, game_textY))


# scores
score = 0
font = pygame.font.Font("freesansbold.ttf", 16)
textX = 10
textY = 10


def show_score(x, y):
    scores = font.render("Scores :" + str(score), True, (255, 255, 255))
    screen.blit(scores, (x, y))


# start text
start = 1
start_text = pygame.font.Font("freesansbold.ttf", 16)
s_textX = 736
s_textY = 10


def start_text():
    scores = font.render("Press any to Start" + str(score), True, (255, 255, 255))
    screen.blit(scores, (s_textX, s_textY))


# Enemy
EnemyX = []
EnemyY = []
Enemy_Image = []
Enemy_ChangeX = []
Enemy_ChangeY = []
numbers_ofEnemies = 20

for i in range(numbers_ofEnemies):
    EnemyX.append(random.randint(0, 735))
    EnemyY.append(random.randint(50, 100))
    Enemy_Image.append(pygame.image.load("alien.png"))
    Enemy_ChangeX.append(1)
    Enemy_ChangeY.append(70)

# Bullet
bulletX = 0
bulletY = 480
bullet_Image = pygame.image.load("bullet.png")
billet_ChangeX = 0
bullet_ChangeY = 3
bullet_State = 0


# player def
def player(x, y):
    # drawing player picture on screen
    screen.blit(player_Image, (x, y))


# Enemy def
def Enemy(x, y, i):
    # drawing Enemy picture on screen
    screen.blit(Enemy_Image[i], (x, y))


# bullet
def bullet_fire(x, y):
    screen.blit(bullet_Image, (x + 16, y + 10))


# kill the enemy
def Enemy_killed(enemyX, enemyY, playerX, playerY):
    killed = math.sqrt((math.pow((enemyX - playerX), 2)) + (math.pow((enemyY - playerY), 2)))
    if killed < 20:
        return True
    else:
        return False


# Game loop until the Screen Not exit
running = True
while running:

    # Background screen color
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(back_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checking the keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Change -= 2
            if event.key == pygame.K_RIGHT:
                player_Change += 2
            if event.key == pygame.K_SPACE:
                bullet_State = 1
                bulletX = playerX
                bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                player_Change = 0

    # incrementing the X axis when the key pressed
    # Player Movement
    playerX += player_Change
    # making Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736



    # Buulet
    if bulletY == 0:
        bulletY = 480
        bullet_State = 0

    if bullet_State == 1:
        bullet_fire(bulletX, bulletY)
        bulletY -= bullet_ChangeY

    # Enemy Killed or not
    # Enemy Movement
    for i in range(numbers_ofEnemies):
        if EnemyY[i] >= 439:
            for j in range(numbers_ofEnemies):
                EnemyY[j] = 2000
            game_Over_text()
            break
        EnemyX[i] += Enemy_ChangeX[i]
        if EnemyX[i] <= 0:
            Enemy_ChangeX[i] = 1
            EnemyY[i] += Enemy_ChangeY[i]
        elif EnemyX[i] >= 736:
            Enemy_ChangeX[i] = -1
            EnemyY[i] += Enemy_ChangeY[i]
        if Enemy_killed(bulletX, bulletY, EnemyX[i], EnemyY[i]):
            bullet_State = 0
            bulletY = 480
            score += 1
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = random.randint(50, 100)
        Enemy(EnemyX[i], EnemyY[i], i)

    # calling player function
    player(playerX, playerY)
    # calling show_score
    show_score(textX, textY)
    # updating the game screen
    pygame.display.update()
