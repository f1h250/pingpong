from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,p_img,p_x,p_y,p_s,w,h):
        super().__init__()
        self.image = transform.scale(image.load(p_img), (w,h))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.y = p_y
        self.rect.x = p_x

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
  
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (255,200,100)
win_height = 500
win_width = 600
window = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

p1 = Player('racket.png', 30, 200, 4, 50, 150)
p2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('P1 LOSE!', True, (180,0,0))
lose2 = font.render('P2 LOSE!', True, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        p1.update_l()
        p2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0 :
            speed_y *= -1

        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width :
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        p1.reset()
        p2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)