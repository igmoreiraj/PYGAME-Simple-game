import pygame
import time
import random

pygame.init()


display_width = 900
display_height = 600

black = (0,0,0)
white = (255,255,255)
red=(129,0,56)
wall = (201,198,206)

#Button Colors
btn=(100,149,237)
gold=(255,215,0)
#Hoover colors
bright_red=(155,0,56)
bright_gold=(255,255,0)


cav_width=73
cav_height=90

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dragons and Dungeons')

bg = pygame.image.load("dungeon2.jpg")



clock = pygame.time.Clock()
carImg = pygame.image.load('cav2.jpg')


def exit_game():
    pygame.quit()
    quit()


def button(msg,x,y,w,h,i,a,action=None):
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    #Buttons for start menu
    
    if (x+w)>mouse[0]>x and (y+h)>mouse[1]>y:
        pygame.draw.rect(gameDisplay,a,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()

##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
                
    else:
        pygame.draw.rect(gameDisplay,i,(x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf',20)

    #Texto Botão Start
    TextSurf,TextRect = text_objects(msg,smallText,black)
    TextRect.center=((x+(w/2),y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)






def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def crash():
    message_display('Game Over',black)

    game_loop()

#Menu inicial
def game_intro():

    intro=True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(bg, (0, 0))
        largeText=pygame.font.SysFont('app850.fon',80)
        TextSurf,TextRect = text_objects("Dragons & Dungeons",largeText,white)
        TextRect.center=((display_width*0.5,display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        #Chama a função que cria os botões
        button("Start",display_width*0.25,display_height*0.7,100,50,gold,bright_gold,game_loop)
        button("Exit",display_width*0.65,display_height*0.7,100,50,red,bright_red,exit_game)
        

        pygame.display.update()
        clock.tick(15)

def message_display(text,color):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText,color)
    TextRect.center=((display_width*0.5,display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    
    time.sleep(2)

    


def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def game_loop():
    
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change=0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    thing_count=2
    dodged=0

    gameExit=False
        
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key==pygame.K_UP:
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    y_change=5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                   
        

        x+=x_change
        y+=y_change

        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,wall)
        things(thing_startx+random.randrange(0,display_width-thing_startx),thing_starty,thing_width,thing_height,wall)
        thing_starty+=thing_speed
        car(x,y)
        things_dodged(dodged)

        if x>display_width-cav_width or x<0:
            crash()
        elif y>display_height-cav_height or y<0:
            crash()

        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            thing_speed+=1
            thing_width+=(dodged*1.3)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+cav_width > thing_startx and x + cav_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()


