#TASK 1:
import pygame
pygame.init()

screen=pygame.display.set_mode((1000,700))
pygame.display.set_caption("Intern game window")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    screen.fill((100,200,150))
    pygame.display.update()
pygame.quit()


#TASK 2:
import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Shapes")

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(WHITE)
    #rectangle
    pygame.draw.rect(screen,RED,(100,200,200,100))
    #square
    pygame.draw.rect(screen,GREEN,(400,200,100,100))
    #circle
    pygame.draw.circle(screen,BLUE,(650,250),60)
    pygame.display.update()
pygame.quit()


#TASK 3:
import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Key detection")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("Moving backward")
            elif event.key==pygame.K_RIGHT:
                print("Moving forward")
            elif event.key==pygame.K_UP:
                print("jump")
            elif event.key==pygame.K_DOWN:
                print("crouch")
pygame.quit()



#TASK 4:
import pygame
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Sound player")

sound = pygame.mixer.Sound("game_over.wav")
sound.play()

GRAY=(150,150,150)
WHITE=(255,255,255)
font=pygame.font.SysFont("arial",50)
text=font.render("Playing",True,WHITE)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(GRAY)
    screen.blit(text,(250,250))
    pygame.display.update()
pygame.quit()



#TASK 5:
import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Display")

WHITE=(255,255,255)
GREEN=(0,255,0)
font=pygame.font.SysFont("arial",40)

name=font.render("Name: Prajwal",True,GREEN)
course=font.render("Course: Computer Science",True,GREEN)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(WHITE)
    screen.blit(name,(200,250))
    screen.blit(course,(200,300))
    pygame.display.update()
pygame.quit()


#TASK 6:
import pygame
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Multi sound player")

WHITE=(255,255,255)
RED=(255,0,0)

audio1=pygame.mixer.Sound("glass_breaking.mp3.mpeg")
game_over=pygame.mixer.Sound("game_over.wav")

pygame.mixer.music.load("subway_surfers.mp3.mpeg")

audio1.play(loops=4)
pygame.mixer.music.play(-1)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over.play()  
            pygame.time.delay(1000)
            running=False

    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(400,300),60)
    pygame.display.update()
pygame.quit()



#TASK 7:
import pygame
import random
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Simple mini game")

WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)

player_x=50
player_y=150
size=40
speed=5

target_x=random.randint(100,550)
target_y=random.randint(50,350)

score=0
font=pygame.font.SysFont("arial",30)

pygame.mixer.music.load("subway_surfers.mp3.mpeg")
pygame.mixer.music.play(-1)   

hit_sound=pygame.mixer.Sound("glass_breaking.mp3.mpeg")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    if (player_x < target_x + size and
        player_x + size > target_x and
        player_y < target_y + size and
        player_y + size > target_y):

        score+=1
        hit_sound.play()
        target_x=random.randint(100,550)
        target_y=random.randint(50,350)
        
    screen.fill(WHITE)

    pygame.draw.rect(screen,BLUE,(player_x,player_y,size,size))
    pygame.draw.rect(screen,RED,(target_x,target_y,size,size))

    text=font.render("Score: "+str(score),True,BLACK)
    screen.blit(text,(10,10))
    pygame.display.update()
pygame.quit()


