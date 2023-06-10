import pygame
import time
import random
from pygame import mixer

pygame.init()

mixer.init()
crash_sound = pygame.mixer.Sound("data/music/crash.mp3")
pygame.mixer.music.load("data/music/music.mp3")

display_width = 800
display_height = 600

black = (0,0,0)
white = (225,225,225)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,225,0)

block_color = (53,115,255)

car_width = 62



name = input("Enter Your Name: ")
if name == "super":
    print("Welcome Back, Dev")
else:
    print("Welcome Back, " + name)



gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Let's Race")

clock = pygame.time.Clock()

tgreencarImg = pygame.image.load('data/Images/Car_image/racecar transparent.png')
carImg = pygame.image.load('data/Images/Car_image/race_car transparent.png')
tredcarImg = pygame.image.load('data/Images/Car_image/Red racecar_transparent.png')
tbluecarImg = pygame.image.load('data/Images/Car_image/Blue racecar_transparent.png')
carlogo = pygame.image.load('data/Images/Car_image/Red racecar_transparent.png')
carloop = carImg


pygame.display.set_icon(carlogo)

pause = False
#crash = True

def things_dodged(count):
    font = pygame.font.SysFont("Segoe Print", 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text, (400,0))

def Level(count):
    font = pygame.font.SysFont("Segoe Print", 25)
    text = font.render("Level: "+str(count), True, black)
    gameDisplay.blit(text, (250,0))
    #print(count)

def Name(Text):
    font = pygame.font.SysFont("Segoe Print", 25)
    text = font.render("Name: "+str(Text), True, black)
    gameDisplay.blit(text, (0,0))

def Things(thingx, thingy, image):
    gameDisplay.blit(image, (thingx, thingy))
    #pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("Segoe Print",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
                     
def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print(event)
                pygame.quit()
                quitgame()
                
        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("Segoe Print",115)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

            
            
        


        
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quitgame()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.SysFont("Segoe Print", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    
    pygame.mixer.music.pause()
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print(event)
                pygame.quit()
                quitgame()
                
        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("Segoe Print",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

            
            
        


        
        pygame.display.update()
        clock.tick(15)
def game_won():
    
    pygame.mixer.music.pause()
    
    while game_won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print(event)
                pygame.quit()
                quitgame()
                
        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("Segoe Print",115)
        TextSurf, TextRect = text_objects("You have Won", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play again",150,450,100,50,green,bright_green,game_loop)
        button("Home",350,450,100,50,green,bright_green,game_intro)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

            
            
        


        
        pygame.display.update()
        clock.tick(15)



def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print(event)
                pygame.quit()
                quitgame()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("Segoe Print",115)
        TextSurf, TextRect = text_objects("Let's Race", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        #button("Settings",350,450,100,50,green,bright_green,settings)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

            
            
        


        
        pygame.display.update()
        clock.tick(15)


        

    

def game_loop():
    global pause
    pygame.mixer.music.play(-1)

    
    x = (display_width * 0.45)
    y = (display_height * 0.7)
    
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 82
    thing_height = 73

    dodged = 0
    level = 1
    

    gameExit = False

    tgreencarImg = pygame.image.load('data/Images/Car_image/racecar transparent.png')
    carImg = pygame.image.load('data/Images/Car_image/race_car transparent.png')
    tredcarImg = pygame.image.load('data/Images/Car_image/Red racecar_transparent.png')
    tbluecarImg = pygame.image.load('data/Images/Car_image/Blue racecar_transparent.png')
    carloop = tgreencarImg

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_s:
                    thing_speed += 1
                if name == "super" and event.key == pygame.K_w:
                    carloop = tredcarImg
                    dodged = 29
                    level = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
        x += x_change
        gameDisplay.fill(white)

        #Things(thingx, thingy, thingw, thingh, color)
        Things(thing_startx, thing_starty, carloop)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        Level(level)
        Name(name)

        if x > display_width - car_width or x < 0:
            if x >= 735:
                x = 0
            elif x <= 0:
                x = 734
                
            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if dodged == 10:
                level = 2
                thing_speed += 5
                carloop = tredcarImg
                thing_width = 73
                thing_height = 82
            elif dodged == 20:
                level = 3
                thing_speed += 5
                carloop = tbluecarImg
                thing_width = 73
                thing_height = 82
            elif dodged == 30:
                game_won()
            #thing_width += (dodged * 1.2)
            #thing_height += 10

        if y < thing_starty + thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                    #print('x crossover')
                    crash()
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quitgame()
