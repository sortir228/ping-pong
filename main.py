import pygame
pygame.init()
win_widht = 700
win_height =  500
back = pygame.transform.scale(pygame.image.load('бабайка.jpg'),(win_widht,win_height))
main_win = pygame.display.set_mode((win_widht,win_height))

clock = pygame.time.Clock()
game_finished = False
while not game_finished:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            game_finished = True
    
    main_win.blit(back,(0,0))
    pygame.display.update()
    clock.tick(60)