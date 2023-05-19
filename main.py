from pygame import * 
from random import randint 
clock = time.Clock() 
image1 = image.load('мячик для пинпонга.png') 
image2 = image.load('бабайка.jpg') 
image3 = image.load('ракетка.png') 
image4 = image.load('ракетка.png') 
image4 = transform.rotate(image4,180) 
win = display.set_mode((1100,700)) 
bk = transform.scale(image2,(1100,700)) 
display.set_caption("pin pong") #?   название программы 
font.init() 
text = font.SysFont('Arial',36) 
speed_x = 20 
speed_y = 20 
text  = font.SysFont('arial',40) 
lose = text.render('игрок 1 проиграл',1,(255,255,255)) 
lose1 = text.render('игрок 2 проиграл',1,(255,255,255)) 
game = False 
finish = False 
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image,player_x, player_y,size_x,size_y,player_speed): 
        super().__init__() 
        self.image = transform.scale(player_image,(size_x,size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        win.blit(self.image,(self.rect.x, self.rect.y)) 
class Player(GameSprite): 
    def update_left(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y >0: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 700: 
            self.rect.y += self.speed 
    def update_right(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y >0: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 700: 
            self.rect.y += self.speed 
platform_left = Player(image3,1,300,70,220,20) 
platform_rigth = Player(image4,1000,300,70,220,20) 
ball = GameSprite(image1,400,250,100,100,0) 
while not game: 
    for i in event.get(): 
        if i.type == QUIT: 
            game = True
    if not finish: 
        win.blit(bk,(0,0)) 
        platform_left.update_right() 
        platform_rigth.update_left() 
        platform_left.reset() 
        platform_rigth.reset() 
        ball.reset() 
        if finish != 1: 
            ball.rect.x +=speed_x 
            ball.rect.y +=speed_y      
        if ball.rect.y <0 or ball.rect.y >= 600: 
            speed_y *= -1 
        if sprite.collide_rect(platform_left,ball) or sprite.collide_rect(platform_rigth,ball): 
            speed_x *= -1 
        if ball.rect.x <0: 
            win.blit(lose,(225,325)) 
            finish = True 
        if ball.rect.x > 1100: 
            win.blit(lose1,(225,325)) 
            finish = True 
    display.update() 
    time.delay(20)