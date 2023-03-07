
from pygame import *
from random import randint
mixer.init()
font.init()

WND_SIZE = (700, 500)
PURPLE = (100, 0, 175)
wnd = display.set_mode(WND_SIZE)
shoot_cd = 0

bang_sound = mixer.Sound('fire.ogg')
bang_sound.set_volume(0.01)

bullets = sprite.Group()

SPR_SIZE = (75, 75)
enemies_missed = 0
enemies_hit = 0
counters_values = [enemies_missed, enemies_hit]
font1 = font.Font(None, 24)
font2 = font.Font(None, 62)

class gamesprite(sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), SPR_SIZE)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))

class plr(gamesprite):
    def control(self):
        keyss = key.get_pressed()

        if keyss[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keyss[K_RIGHT] and self.rect.x < WND_SIZE[0] - SPR_SIZE[0]:
            self.rect.x += self.speed
    def bang(self):
        global shoot_cd
        keyss = key.get_pressed()
        if keyss[K_SPACE] and shoot_cd <= 0:
            bang_sound.play()
            bang_thing = bullet('bullet.png', 3, self.rect.x, self.rect.y)
            bullets.add(bang_thing)
            shoot_cd = 30
        elif shoot_cd > 0:
            shoot_cd -= 1

class enm(gamesprite):
    def __init__(self, plr_image, speed, x, y, is_destroy):
        super().__init__(plr_image, speed, x, y)
        self.is_destroy = is_destroy
    def update(self):
        global enemies_missed
        self.rect.y += self.speed
        if self.rect.y > WND_SIZE[1] - SPR_SIZE[1]:
            self.rect.y = randint(-100, 0)
            self.rect.x = randint(0, WND_SIZE[0] - SPR_SIZE[0])
            self.speed = randint(1,3)
            if self.is_destroy:
                enemies_missed += 1
                counters_values[0] = enemies_missed
class counter():
    def counter_update(self):
        lost_enemies_text = font1.render('Пропущено: ' + str(counters_values[0]), 1, PURPLE)
        kill_enemies_text = font1.render('Пробито: ' + str(counters_values[1]), 1, PURPLE)
        wnd.blit(lost_enemies_text, (0,0))
        wnd.blit(kill_enemies_text, (WND_SIZE[0]- 100, 0))

class bullet(gamesprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

