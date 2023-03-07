from classes import *



mixer.music.load('space.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()


enms_sprites = ['asteroid.png', 'ufo.png']

win_msg = font2.render('epic win!!!', 1, (200, 255, 255))
lose_msg = font2.render('epic lose!!!', 1, (200, 255, 255))


counters = counter()

player = plr('rocket.png', 12, 250, WND_SIZE[1] - SPR_SIZE[1])

game = True
game_over = False
display.set_caption('Пиф Паф')
bg = transform.scale(
    image.load('galaxy.jpg'), WND_SIZE)
clock = time.Clock()
enemies = sprite.Group()
asteroids = sprite.Group()
for i in range(5):
    enemy1 = enm(enms_sprites[1], randint(1,3), randint(0, WND_SIZE[0] - SPR_SIZE[0]), randint(-100, 0), True)
    enemies.add(enemy1)
for i in range(3):
    enemy1 = enm(enms_sprites[0], randint(1,3), randint(0, WND_SIZE[0] - SPR_SIZE[0]), randint(-100, 0), False)
    asteroids.add(enemy1)




while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    if not game_over:

        wnd.blit(bg, (0,0))
        player.control()
        player.bang()
        player.reset()
        enemies.draw(wnd)
        asteroids.draw(wnd)
        bullets.draw(wnd)
        enemies.update()
        bullets.update()
        asteroids.update()



        for bullet in bullets:
            for monster in enemies:
                if sprite.collide_rect(bullet, monster):
                    counters_values[1] += 1
                    bullet.kill()
                    monster.kill()
                    enemies.add(enm(enms_sprites[1], randint(1,3), randint(0, WND_SIZE[0] - SPR_SIZE[0]), randint(-100, 0), False) )
            for aster in asteroids:
                if sprite.collide_rect(bullet, aster):
                    bullet.kill()

        if counters_values[1] >= 10:
            game_over = True
            wnd.blit(win_msg, (250, 250))
        elif counters_values[0] >= 3 or sprite.spritecollide(player, enemies, False) or sprite.spritecollide(player, asteroids, False):
            game_over = True
            wnd.blit(lose_msg, (250, 250))




        counters.counter_update()


        clock.tick(60)
        display.update()
