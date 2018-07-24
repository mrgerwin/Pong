import pygame as pygame

screenSize = [320, 240]
ballLocation = [screenSize[0]//2, screenSize[1]//2]
black = 0, 0, 0
white = 255, 255, 255
ballSpeed = [1, 1]
ballRect = pygame.Rect(ballLocation[0]-5, ballLocation[1]-5, 10, 10)
padSpeed = 4
padRect= pygame.Rect((0,0), (10, 50))
score = 0
fps = 60
quit = False

timer = pygame.time.Clock()
window = pygame.display.set_mode(screenSize)
pygame.joystick.init()
print("There are ", pygame.joystick.get_count(), " joysticks connected.")
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

def collide():
    if pygame.Rect.colliderect(ballRect, padRect):
        print("Paddle and Ball Collide")

def paddleMove():
    global gamepad, padRect, padSpeed, screenSize
    
    if gamepad.get_axis(1) > 0:
        if padRect.bottom >= screenSize[1]:
            padSpeed = 0
        else:
            padSpeed = 4
    if gamepad.get_axis(1) < 0:
        if padRect.top <= 0:
            padSpeed = 0
        else:    
            padSpeed = -4
    if gamepad.get_axis(1) == 0:
        padSpeed = 0
        
    padRect = padRect.move(0,padSpeed)
    print(padRect.top)
    pygame.draw.rect(window, white, padRect)
    
    print(gamepad.get_axis(1))

def moveCircle():
    global ballLocation, screenSize, ballSpeed, ballRect

    if ballLocation[0]+10 >= screenSize[0]:
        ballSpeed[0] = -ballSpeed[0]
    if ballLocation[0]<= 10:
        ballSpeed[0] = -ballSpeed[0]
    if ballLocation[1] + 10 >= screenSize[1]:
        ballSpeed[1] = -ballSpeed[1]
    if ballLocation[1] <= 10:
        ballSpeed[1] = -ballSpeed[1]
    
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
        if event.type == pygame.JOYAXISMOTION:
            print("D-Pad was used")
    paddleMove()
    moveCircle()
    collide()
    timer.tick(fps)
    window.fill(black)


