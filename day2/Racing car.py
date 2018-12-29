import sys, pygame
import time
import random
pygame.init()

size = width, height = 400, 400
speed = [0, 1]
black = 0, 0, 0
white = 255,255,255
blue = 0,0,255
green = 0,255,0
car_width=90

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Racing car')

car = pygame.image.load("C:\Users\Rishabh\Downloads\download1.png")
carrect = car.get_rect()

def obstacle(obx,oby,obw,obh,color):
    pygame.draw.rect(screen,color,[obx,oby,obw,oby])

def racecar(x,y):
    screen.blit(car,(x,y))

def text_objects(text,font):
    textsurface=font.render(text,True,blue)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',20)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((width/2),(height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game()

def crash():
    message_display('Game Over')



def game():
    x = (width*0.5)
    y = (height*0.5)
    x_change=0

    ob_startx = random.randrange(0,width)
    ob_starty = -600
    ob_speed = 2
    ob_width = 20
    ob_height = 20
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x+=x_change

        '''carrect = carrect.move(speed)
        if carrect.left < 0 or carrect.right > width:
            speed[0] = -speed[0]
        if carrect.top < 0 or carrect.bottom > height:
            speed[1] = -speed[1]'''

        screen.fill(white)

        obstacle(ob_startx,ob_starty,ob_width,ob_height,black)
        ob_starty+=ob_speed
        
        racecar(x,y)

        if x>(width-car_width) or x<0:
            crash()
    #screen.blit(car, carrect)

        if ob_starty > height:
            ob_starty = 0-height
            ob_startx = random.randrange(0,width)

        if y<(ob_starty+ob_height):
            print "y crossover"

            if x>ob_startx and x<ob_startx+ob_width or x+car_width > ob_startx and x+car_width < ob_startx+ob_width:
                print "x crossover"
                crash()

        pygame.display.flip()

game()
pygame.quit()
quit()
