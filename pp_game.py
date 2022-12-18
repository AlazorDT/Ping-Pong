from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)
        '''спрайты хранят картинку'''
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        '''спрайты - прямоугольники "rectangle" '''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        '''отрисовка героя на окне'''
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    '''класс игрока'''
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.x += self.speed


'''игровая сцена'''
back = (49, 90, 1) #цвет фона
win_width = 600
win_height = 500
win = display.set_mode((win_width, win_height))
win.fill(back)


'''флаги, отвечаюшие за состояние игры'''
game = True
finish = False
clock = time.Clock()
FPS = 60


'''объекты'''
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)


font.init()
font2 = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYET 2 LOSE!', True, (180, 0, 0)))
winner1 = font.render('PLAYER 1 WIN!'), True, (0, 0, 180)
winner2 = font.render('PLAYER 2 WIN!'), True, (0, 0, 180)

speed_x = 3
speed_y = 3

while game:
    for e in event.get()
        if e type == QUIT:
            game = False

    if finish != True:
        win.fill(back)
        racket1.update_r()
        racket2.update_l()
        ball.rect.x +=

