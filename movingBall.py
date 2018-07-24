import pygame as pygame

size = [320, 240]
location = [size[0]//2, size[1]//2]
black = 0, 0, 0
white = 255, 255, 255
speed = [1, 1]

fps = 60

timer = pygame.time.Clock()
window = pygame.display.set_mode(size)

def moveCircle():
    global location, size, speed

    if location[0]+10 >= size[0]:
        speed[0] = -1
    if location[0]<= 10:
        speed[0] = 1
    if location[1] + 10 >= size[1]:
        speed[1] = -1
    if location[1] <= 10:
        speed[1] = 1
    
    location[0] = location[0]+speed[0]
    location[1] = location[1] + speed[1]
    window.fill(black)
    pygame.draw.circle(window, white, location, 10, 0) 
    pygame.display.flip()

while True:
    moveCircle()
    timer.tick(fps)


