import pygame
import time
import random

pygame.init() #initialize pygame

width = 700
height = 700 #size parameters for starting wondow

black = 0, 0, 0
white = 255,255,255
blue = 0,0,255
green = 0,255,0
red = 255,0,0 #color coordinates (r,g,b)

car_width=90 #width of the car

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Racing car hurdle cross')
clock = pygame.time.Clock() #Mandatory commands to start the screen and enable gameplay

car = pygame.image.load("C:\Users\Rishabh\Downloads\download1.png") #Image loading


def obstacle(obx,oby,obw,obh,color): #Function defintion for the structure of obstacle
    pygame.draw.rect(screen,color,[obx,oby,obw,obh])

def racecar(x,y): #Function to show car
    screen.blit(car,(x,y))

def text_objects(text,font): #Function used in message display
    textsurface=font.render(text,True,blue)
    return textsurface,textsurface.get_rect()

def message_display(text): #Generalized function to display any message
    largeText=pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((width/2),(height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game()

def crash():
    message_display('Game Over')

def block_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(count),True,red)
    screen.blit(text,(0,0))

def button(msg,x,y,w,h,c,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] >y:
        pygame.draw.rect(screen,c,(x,y,w,h))
        if click[0] == 1 and action!=None:
            action()
    else:
        pygame.draw.rect(screen,c,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",15)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textSurf,textRect)


def game_intro():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',55)
        TextSurf,TextRect = text_objects("Racing car Hurdle cross",largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf,TextRect)

        button("GO!",150,450,100,50,green,game)
        button("Quit",450,450,100,50,red,quitgame)
        pygame.display.update()
        clock.tick(30)


def game():
    x = (width*0.5)
    y = (height*0.5)
    x_change=0

    ob_startx = random.randrange(0,width)
    ob_starty = -600
    ob_speed = 5
    ob_width = 80
    ob_height = 80

    dodged = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x+=x_change

        screen.fill(white)

        obstacle(ob_startx,ob_starty,ob_width,ob_height,black)
        ob_starty+=ob_speed
        
        racecar(x,y)

        block_dodged(dodged)

        if x > width - car_width or x < 0:
            crash()

        if ob_starty > height:
            ob_starty = 0 - ob_height
            ob_startx = random.randrange(0,width)
            dodged+=1
            ob_speed+=1
            ob_width+=(dodged*1.1)

        if y < ob_starty+ob_height:
            print "y crossover"

            if x > ob_startx and x < ob_startx + ob_width or x+car_width > ob_startx and x + car_width < ob_startx+ob_width:
                print "x crossover"
                crash()
                
        pygame.display.update()
        clock.tick(60)

def quitgame():
    pygame.quit()
    quit()

game_intro()
game()
pygame.quit()
quit()
