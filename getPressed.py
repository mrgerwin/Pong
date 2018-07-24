import pygame as pygame
pygame.init()
clock = pygame.time.Clock()
i = 0
gameDisplay = pygame.display.set_mode((200, 200))
color = [0,0,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                gameDisplay.fill((0, 255, 0))
                color=[0,255,0]
            elif event.key == pygame.K_r:
                color = [255, 0, 0]
                gameDisplay.fill(color)
            elif event.key == pygame.K_b:
                color = [0, 0, 255]
                gameDisplay.fill(color)
            elif event.key == pygame.K_UP:
                if color[0]<255:
                    color[0] = color[0]+1
                if color[1] < 255:
                    color[1] = color[1] + 1
                if color[2] < 255:
                    color[2] = color[2] + 1
                gameDisplay.fill(color)
                
            

    #pressed = pygame.key.get_pressed()
    #for index in pressed:
        #if index == True:
            #print( str(i) + " was pressed ")
            #i = i +1
    pygame.display.update()
    clock.tick(10)