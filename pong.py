import pygame as pygame

screenSize = [320, 240]
ballLocation = [screenSize[0]//2, screenSize[1]//2]
black = 0, 0, 0
white = 255, 255, 255
green = 0, 128, 0
ballSpeed = [1, 1]
ballRect = pygame.Rect(ballLocation[0]-5, ballLocation[1]-5, 10, 10)
padSpeed = 4
left_padRect= pygame.Rect((0,0), (10, 50))
right_padRect = pygame.Rect((screenSize[0]-10, 0), (10, 50))
score = 0
score2=0
fps = 60
quit = False
keyboard_1 = False
keyboard_2 = False

timer = pygame.time.Clock()
window = pygame.display.set_mode(screenSize)
pygame.joystick.init()
joystickNum = int(pygame.joystick.get_count())
if joystickNum>=1:
    left_gamepad = pygame.joystick.Joystick(0)
    left_gamepad.init()

else:
    keyboard_1 = True
    print("Please Connect Two Game Controllers")

if joystickNum>=2:
    right_gamepad = pygame.joystick.Joystick(1)
    right_gamepad.init()
    #print(right_gamepad.get_name())
else:
    keyboard_2 = True
    print("Please Connect the Second Game Controller")
#print(pygame.font.get_default_font())
theFont = pygame.font.init()
theFont = pygame.font.Font(None, 24)

def reset():
    global score, ballLocation, ballSpeed, ballRect
    
    ballLocation = [screenSize[0]//2, screenSize[1]//2]
    if score < score2:
        ballSpeed = [1, 1]
    else:
        ballSpeed = [-1, 1]
    ballRect = pygame.Rect(ballLocation[0]-5, ballLocation[1]-5, 10, 10)
    
'''
def left_keyboardMap():
    global left_padRect
    for key in pygame.KEYDOWN():
        if key.name == 'K_s':
            if left_padRect.bottom >= screenSize[1]:
                padSpeed = 0
            else:
                padSpeed = 4
        if  key.name == 'K_w':
            if left_padRect.top <= 0:
                padSpeed = 0
            else:    
                padSpeed = -4
    else:
        padSpeed = 0
    return padSpeed

def right_keyboardMap():
    padSpeed =0
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_DOWN:
                if right_padRect.bottom >= screenSize[1]:
                    padSpeed = 0
                else:
                    padSpeed = 4
            if event.key == pygame.K_UP:
                if right_padRect.top <= 0:
                    padSpeed = 0
                else:    
                    padSpeed = -4
            else:
                padSpeed = 0
    return padSpeed    
'''
def drawCenterLine():
    global screenSize
    pygame.draw.line(window, green, (screenSize[0]//2,0), (screenSize[0]//2, screenSize[1])) 
def displayScore(font):
    global score, green, screenSize, score2
    
    text = font.render("Score: " + str(score), True, green)
    print(text.get_width())
    window.blit(text, (screenSize[0]//4-text.get_width()//2, text.get_height()))
    text = font.render("Score: " + str(score2), True, green)
    window.blit(text, (screenSize[0]//4*3-text.get_width()//2, text.get_height()))
                
                
def collide():
    global ballRect, left_padRect, right_padRect
    if ballRect.colliderect(right_padRect) or ballRect.colliderect(left_padRect):
        #print("Paddle and Ball Collide")
        return True
    else:
        return False

def left_paddleMove():
    global left_gamepad, left_padRect, screenSize
    
    if keyboard_1 == True:
        #padSpeed = left_keyboardMap()
        return
    else:
    
        if left_gamepad.get_axis(1) > 0:
            if left_padRect.bottom >= screenSize[1]:
                padSpeed = 0
            else:
                padSpeed = 4
        if left_gamepad.get_axis(1) < 0:
            if left_padRect.top <= 0:
                padSpeed = 0
            else:    
                padSpeed = -4
        if left_gamepad.get_axis(1) == 0:
            padSpeed = 0
        
    left_padRect = left_padRect.move(0,padSpeed)
    #print(padRect.top)
    pygame.draw.rect(window, white, left_padRect)
    
    #print(gamepad.get_axis(1))
def right_paddleMove():
    global right_gamepad, right_padRect, screenSize
    
    #print(right_gamepad.get_axis(1))
    
    if keyboard_2 == True:
        #padSpeed = right_keyboardMap()
        return
    else:
    
        if right_gamepad.get_axis(1) > 0:
            if right_padRect.bottom >= screenSize[1]:
                padSpeed = 0
            else:
                padSpeed = 4
        if right_gamepad.get_axis(1) < 0:
            if right_padRect.top <= 0:
                padSpeed = 0
            else:    
                padSpeed = -4
        if right_gamepad.get_axis(1) == 0:
            padSpeed = 0
        
    right_padRect = right_padRect.move(0,padSpeed)
    #print(padRect.top)
    pygame.draw.rect(window, white, right_padRect)
    
    #print(gamepad.get_axis(1))
def moveCircle():
    global ballLocation, screenSize, ballSpeed, ballRect, score, quit, score2

    if ballLocation[0]+10 >= screenSize[0]:
        ballSpeed[0] = -ballSpeed[0]
        score = score +1
        reset()
    if collide():
        ballSpeed[0] = -ballSpeed[0]
    if ballLocation[1] + 10 >= screenSize[1]:
        ballSpeed[1] = -ballSpeed[1]
    if ballLocation[1] <= 10:
        ballSpeed[1] = -ballSpeed[1]
    if ballLocation[0] <= 10:
        score2 = score2+1
        reset()
    
    ballLocation[0] = ballLocation[0]+ballSpeed[0]
    ballLocation[1] = ballLocation[1] + ballSpeed[1]
    ballRect = ballRect.move(ballSpeed)
    pygame.draw.circle(window, white, ballLocation, 10, 0) 
    pygame.display.flip()

while quit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            print("Key was pressed")
        #if event.type == pygame.JOYAXISMOTION:
            #print("D-Pad was used")
    displayScore(theFont)
    drawCenterLine()
    left_paddleMove()
    right_paddleMove()
    moveCircle()
    timer.tick(fps)
    window.fill(black)


