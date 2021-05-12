import pygame
from pygame.locals import *
import traceback
import Me
import enemy
import bullets
import os
print(os.getcwd())
import supplies
import random
from sys import exit


# from goto import with_goto

def add_enemy1(group1, group2, num, bg_size):
    for i in range(num):
        e1 = enemy.monster1(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_enemy2(group1, group2, num, bg_size):
    for i in range(num):
        e2 = enemy.monster2(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_enemy3(group1, group2, num, bg_size):
    for i in range(num):
        e3 = enemy.monster3(bg_size)
        group1.add(e3)
        group2.add(e3)


def inc_speed(group, speed):
    for each in group:
        each.speed += speed


def main():
    pygame.init()
    pygame.mixer.init()
    bg_size = width, height = 1280, 720
    pygame.display.set_caption('                                                                                                                      刘雨臻打怪兽 --- By Lyz')
    screen = pygame.display.set_mode(bg_size)
    img = pygame.image.load(r"images\123.ico").convert_alpha()
    pygame.display.set_icon(img)

    background = pygame.image.load(r'.\images\5.jpg').convert()

    over_normal_image = pygame.image.load(r'.\images\gameover.png').convert_alpha()
    again_normal_image = pygame.image.load(r'.\images\again.png').convert_alpha()
    over_big_image = pygame.image.load(r'.\images\gameover_big.png').convert_alpha()
    again_big_image = pygame.image.load(r'.\images\again_big.png').convert_alpha()

    over_image = pygame.image.load(r'.\images\gameover.png').convert_alpha()
    again_image = pygame.image.load(r'.\images\again.png').convert_alpha()
    again_rect = again_normal_image.get_rect()
    again_rect[0], again_rect[1] = width // 2 - again_rect.width // 2, height // 2 - again_rect.height - 6
    over_rect = over_normal_image.get_rect()
    over_rect[0], over_rect[1] = width // 2 - over_rect.width // 2, height // 2 + 6

    pause_image_1 = pygame.image.load(r'.\images\pause_nor.png').convert_alpha()
    pause_image_2 = pygame.image.load(r'.\images\pause_pressed.png').convert_alpha()
    pause_image_rect = pause_image_1.get_rect()
    pause_image_rect[0], pause_image_rect[1] = width - pause_image_rect.width, 0
    resume_image_1 = pygame.image.load(r'.\images\resume_nor.png').convert_alpha()
    resume_image_2 = pygame.image.load(r'.\images\resume_pressed.png').convert_alpha()
    resume_image_rect = resume_image_1.get_rect()
    resume_image_rect[0], pause_image_rect[1] = width - resume_image_rect.width, 0
    # load music
    pygame.mixer.music.load(r'.\sound\dnf.wav')
    pygame.mixer.music.set_volume(0.4)
    click_sound = pygame.mixer.Sound(r'sound\click.wav')
    move_sound = pygame.mixer.Sound(r'.\sound\move.wav')
    bullet_sound = pygame.mixer.Sound(r'.\sound\bullet.wav')
    bullet_sound.set_volume(0.3)
    bomb_sound = pygame.mixer.Sound(r'.\sound\use_bomb.wav')
    bomb_sound.set_volume(0.2)
    supply_sound = pygame.mixer.Sound(r'.\sound\supply.wav')
    supply_sound.set_volume(0.4)
    get_bomb_sound = pygame.mixer.Sound(r'.\sound\get_bomb.wav')
    get_bomb_sound.set_volume(0.5)
    get_bullet_sound = pygame.mixer.Sound(r'.\sound\get_bullet.wav')
    get_bullet_sound.set_volume(0.5)
    upgrade_sound = pygame.mixer.Sound(r'.\sound\upgrade.wav')
    upgrade_sound.set_volume(0.2)
    enemy3_fly_sound = pygame.mixer.Sound(r'.\sound\enemy3_flying.wav')
    enemy3_fly_sound.set_volume(0.25)
    enemy1_down_sound = pygame.mixer.Sound(r'.\sound\enemy1_down.wav')
    enemy1_down_sound.set_volume(0.6)
    enemy2_down_sound = pygame.mixer.Sound(r'.\sound\enemy2_down.wav')
    enemy2_down_sound.set_volume(0.7)
    enemy3_down_sound = pygame.mixer.Sound(r'.\sound\enemy3_down.wav')
    enemy3_down_sound.set_volume(0.8)
    me_down_sound = pygame.mixer.Sound(r'.\sound\me_down.wav')
    me_down_sound.set_volume(1)

    pygame.mixer.music.play(-1)

    running = True
    clock = pygame.time.Clock()

    # generate Me
    me = Me.Me(bg_size)

    # generate bullet
    bullet1_list = []
    bullet1_num = 13
    bullets_index = 0

    # badbullet_list = []
    # badbullet_num = 20
    # badbullets_index = 0

    level = 1

    for i in range(0, bullet1_num):
        bullet = bullets.Bullet1((me.rect.center[0] + 70, me.rect.center[1] - 20))
        bullet1_list.append(bullet)

    # generate enemy(s)
    enemies_group = pygame.sprite.Group()

    # supply
    supply_time = USEREVENT
    pygame.time.set_timer(supply_time, 20 * 1000)

    bomb_num = 0
    bomb_num_max = 5
    bomb_supply = supplies.Bomb(bg_size)
    bomb_white = False
    bomb_white_count = 0

    sup_supply = supplies.superman(bg_size)


    # bomb image
    bomb_image = pygame.image.load(r'.\images\bomb.png').convert_alpha()
    bomb_font = pygame.font.Font(r'.\font\font.ttf', 48)

    bomb_tip_font = pygame.font.SysFont(r'arial', 25)
    bomb_tip_text = bomb_tip_font.render(' <- Type [SPACE]', True, (255, 0, 0))
    bomb_tip_text_rect = bomb_tip_text.get_rect()
    bomb_tip_text_rect.top = height - bomb_tip_text_rect.height - 12
    bomb_tip_text_rect.left = bomb_image.get_rect().width * 2
    need_tip = False
    is_first = True
    tip_count = 0

    # monster 1
    enemy1_group = pygame.sprite.Group()
    add_enemy1(enemies_group, enemy1_group, 6, bg_size)

    # monster 2
    enemy2_group = pygame.sprite.Group()
    add_enemy2(enemies_group, enemy2_group, 3, bg_size)

    # monster 3
    enemy3_group = pygame.sprite.Group()
    add_enemy3(enemies_group, enemy3_group, 1, bg_size)

    # get shot index
    me_destroy_index = 0

    switch_count = 0
    switch_seq = True
    switch_pic = True
    delay = 100
    new_record = False
    # ------------------------ upgrade text -------------------------------
    dis_level_time = 0
    upgrade_font = pygame.font.Font(r'.\font\font.ttf', 70)
    dis_level = False


    # *************************************** set scores ***************************************
    score = 0
    enemy1_score = 10
    enemy2_score = 150
    enemy3_score = 300
    score_font = pygame.font.Font(r'.\font\font.ttf', 30)
    level_font = pygame.font.Font(r'.\font\font.ttf', 35)

    pause = False
    pause_image = pause_image_1

    harm_max = 40
    harm_interval = 2

    is_on = False
    is_over_display = False

    frames = 60
    # ------------------------------------------------------------------------------------------------------------
    while running:
        # set frames
        clock.tick(frames)
        # ---------------------------------
        if not (delay % 2):
            if switch_seq and switch_count < 3:
                switch_count += 1
            elif not switch_seq and switch_count > 0:
                switch_count -= 1
            elif switch_count == 3:
                switch_seq = False
                switch_count -= 1
            elif switch_count == 0:
                switch_seq = True
                switch_count += 1

        delay -= 1
        if delay == 0:
            delay = 100

        # -------- monster change rate ---------------------
        if not (delay % 28):
            switch_pic = not switch_pic

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and pause_image_rect.collidepoint(event.pos):
                    pause = not pause
                    if pause:
                        pause_image = resume_image_2
                        pygame.time.set_timer(supply_time, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pause_image = pause_image_2
                        pygame.time.set_timer(supply_time, 20 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

                if event.button == 1 and me.live == False:
                    if again_rect.collidepoint(event.pos):
                        enemy.monster1.HP = 1
                        enemy.monster2.HP = 10
                        enemy.monster3.HP = 30
                        main()
                    elif over_rect.collidepoint(event.pos):
                        exit()
                if is_over_display:
                    click_sound.play()

            if event.type == MOUSEMOTION:
                if not is_over_display:
                    if pause_image_rect.collidepoint(event.pos):
                        if pause:
                            pause_image = resume_image_2
                        else:
                            pause_image = pause_image_2
                    else:
                        if pause:
                            pause_image = resume_image_1
                        else:
                            pause_image = pause_image_1
                else:
                    if again_rect.collidepoint(event.pos):
                        if not is_on:
                            move_sound.play()
                            is_on = True
                        again_image = again_big_image
                        again_rect = again_big_image.get_rect()
                        again_rect[0], again_rect[1] = width // 2 - again_big_image.get_rect().width // 2, height // 2 - again_big_image.get_rect().height - 6
                    elif over_rect.collidepoint(event.pos):
                        if not is_on:
                            move_sound.play()
                            is_on = True
                        over_image = over_big_image
                        over_rect = over_big_image.get_rect()
                        over_rect[0], over_rect[1] = width // 2 - over_big_image.get_rect().width // 2, height // 2 + 6
                    else:
                        is_on = False
                        again_image = again_normal_image
                        over_image = over_normal_image
                        again_rect[0], again_rect[
                            1] = width // 2 - again_normal_image.get_rect().width // 2, height // 2 - again_normal_image.get_rect().height - 6
                        over_rect[0], over_rect[1] = width // 2 - again_normal_image.get_rect().width // 2, height // 2 + 6

            if event.type == supply_time:
                if me.live:
                    if not pause:
                        supply_sound.play()
                        if level < 5:
                            if random.choice([True, False]):
                                bomb_supply.reset()
                            else:
                                sup_supply.reset()
                        else:
                            bomb_supply.reset()


            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause = not pause
                    if pause:
                        pause_image = resume_image_1
                        pygame.time.set_timer(supply_time, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pause_image = pause_image_1
                        pygame.time.set_timer(supply_time, 20 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                elif event.key == K_SPACE:
                    if bomb_num:
                        bomb_white = True
                        bomb_white_count = 0
                        for each_enemy in enemies_group:
                            if each_enemy.rect.left < width * 1.8:
                                if each_enemy in enemy1_group:
                                    score += enemy1_score
                                elif each_enemy in enemy2_group:
                                    score += enemy2_score
                                else:
                                    score += enemy3_score
                                each_enemy.live = False
                        bomb_num -= 1
                    else:
                        pass
                    ################################################

        # if me_live:
        screen.blit(background, (0, 0))
        screen.blit(pause_image, pause_image_rect)

        if not pause:

            if me.live:
                # check keyboard
                key_pressed = pygame.key.get_pressed()
                if key_pressed[K_w] or key_pressed[K_UP]:
                    me.move_up()
                if key_pressed[K_s] or key_pressed[K_DOWN]:
                    me.move_down()
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    me.move_left()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    me.move_right()

                # ------------------- check if me hit ------------------------------
                enemies_hit = pygame.sprite.spritecollide(me, enemies_group, False, pygame.sprite.collide_mask)
                if enemies_hit:
                    for each_hit in enemies_hit:
                        if each_hit.live:
                            me.live = False
                            break
                            # -------------- 无敌模式 --------------------
                            # me.live = True
                            #
                            # each.live = False
                            # -------------------------------------------

                # ----------------------- draw enemy --------------------------
                for each in enemy3_group:
                    if each.live:
                        each.move()
                        flag = switch_count
                        if flag == 0:
                            screen.blit(each.image1, each.rect)
                        elif flag == 1:
                            screen.blit(each.image2, each.rect)
                        elif flag == 2:
                            screen.blit(each.image3, each.rect)
                        else:
                            screen.blit(each.image4, each.rect)
                        if each.rect.bottom == -50:
                            enemy3_fly_sound.play(-1)

                        # **************************** draw HP ****************************
                        # blood
                        pygame.draw.rect(screen, (int((1 - each.HP / enemy.monster3.HP) * 255), int(255 * each.HP / enemy.monster3.HP), int(255 * each.HP / enemy.monster3.HP)), (each.rect.left, each.rect.top - 8, int(each.HP / enemy.monster3.HP * each.rect.width), 10))
                        # border
                        pygame.draw.rect(screen, (0, 0, 0), (each.rect.left, each.rect.top - 8, each.rect.width, 10), 2)
                        #
                        # if each.HP / enemy.monster3.HP > 0.2:
                        #     pygame.draw.rect(screen, (0, 255, 255), (
                        #         each.rect.left, each.rect.top - 8, int(each.HP / enemy.monster3.HP * each.rect.width),
                        #         8))
                        # else:
                        #     pygame.draw.rect(screen, (255, 0, 0), (
                        #         each.rect.left, each.rect.top - 8, int(each.HP / enemy.monster3.HP * each.rect.width),
                        #         8))
                        # pygame.draw.rect(screen, (0, 0, 0), (each.rect.left, each.rect.top - 8, each.rect.width, 8), 2)
                        # ************************* end draw HP ******************************

                    else:
                        # die
                        if each.destroy_index == 0:
                            enemy3_fly_sound.stop()
                            enemy3_down_sound.play()
                        if each.destroy_index < 18:
                            screen.blit(each.destroy_images[each.destroy_index // 3], each.rect)
                        each.destroy_index += 1
                        if each.destroy_index >= 18:
                            each.add_score_count += 1
                            if each.add_score_count < 32:
                                each.add_score_text = each.add_score_font.render('+' + str(enemy3_score), True,
                                                                                 (255, 255, 255))
                                screen.blit(each.add_score_text, each.rect)
                            else:
                                each.reset()

                # draw enemy2
                for each in enemy2_group:
                    if each.live:
                        if switch_pic:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                        each.move()
                        # draw HP
                        if each.HP / enemy.monster2.HP > 0.2:
                            pygame.draw.rect(screen, (200, 100, 255), (
                                each.rect.left, each.rect.top - 8, int(each.HP / enemy.monster2.HP * each.rect.width),
                                8))
                        else:
                            pygame.draw.rect(screen, (255, 0, 0), (
                                each.rect.left, each.rect.top - 8, int(each.HP / enemy.monster2.HP * each.rect.width),
                                6))
                        # pygame.draw.rect(screen, (0, 0, 0), (each.rect.left, each.rect.top - 8, each.rect.width, 8), 1)

                    else:
                        # die

                        if each.destroy_index == 0:
                            enemy2_down_sound.play()

                        if each.destroy_index < 12:
                            screen.blit(each.destroy_images[each.destroy_index // 3], each.rect)
                        each.destroy_index += 1

                        if each.destroy_index >= 12:
                            each.add_score_count += 1
                            if each.add_score_count < 30:
                                each.add_score_text = each.add_score_font.render('+' + str(enemy2_score), True,
                                                                                 (255, 255, 255))
                                screen.blit(each.add_score_text, each.rect)
                            else:
                                each.reset()

                    # draw enemy1
                # draw enemy1d
                for each in enemy1_group:
                    if each.live:
                        screen.blit(pygame.transform.rotate(each.image, each.angle), each.rect)
                        each.move()
                    else:
                        # die
                        if each.destroy_index == 1:
                            enemy1_down_sound.play()

                        if each.destroy_index < 12:
                            screen.blit(each.destroy_images[each.destroy_index // 3], each.rect)
                        each.destroy_index += 1

                        if each.destroy_index >= 12:
                            each.add_score_count += 1
                            if each.add_score_count < 30:
                                each.add_score_text = each.add_score_font.render('+' + str(enemy1_score), True, (255, 255, 255))
                                screen.blit(each.add_score_text, each.rect)
                            else:
                                each.reset()
                # ----------------------------------------------------------------
                # --------------- get supply -------------------------
                if bomb_supply.active:
                    bomb_supply.move()
                    screen.blit(bomb_supply.image, bomb_supply.rect)
                    if pygame.sprite.collide_mask(bomb_supply, me):
                        if is_first:
                            need_tip = True
                            is_first = False
                        get_bomb_sound.play()
                        if bomb_num < bomb_num_max:
                            bomb_num += 1
                        bomb_supply.active = False

                if sup_supply.active:
                    sup_supply.move()
                    screen.blit(sup_supply.image, sup_supply.rect)
                    if pygame.sprite.collide_mask(sup_supply, me):
                        get_bullet_sound.play()
                        sup_supply.active = False
                        # if bullets.Bullet1.form == 1:
                        for each_bullet in bullet1_list:
                            each_bullet.change2()
                        if bullets.Bullet1.harm < harm_max:
                            bullets.Bullet1.harm += harm_interval
                # -------------------------------------
                # ------------------------ draw me ------------------------------
                if switch_pic:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
                # ----------------------------------------------------------------

                #  ------------- reset bullets ---------------------------
                if delay % 10 == 0:
                    if level == 6:
                        bullet1_list[bullets_index].reset((me.rect.center[0] + 70, me.rect.center[1] - 20))
                    else:
                        bullet1_list[bullets_index].reset((me.rect.center[0] + 30, me.rect.center[1]))
                    bullets_index = (bullets_index + 1) % bullet1_num
                    bullet_sound.play()

                # draw bullets
                for each in bullet1_list:
                    if each.active:
                        screen.blit(each.image, each.rect)
                        each.move()

                        # check bullet hit
                        enemies_shot = pygame.sprite.spritecollide(each, enemies_group, False, pygame.sprite.collide_mask)

                        # if any monseter got shot
                        if enemies_shot:
                            for each_enemy in enemies_shot:

                                if each_enemy.live:
                                    each_enemy.HP -= bullets.Bullet1.harm
                                    screen.blit(each_enemy.image_hit, each_enemy.rect)
                                    # set bullet died
                                    each.active = False
                                if each_enemy.HP <= 0:
                                    # enemy2 add score!
                                    if each_enemy.live:
                                        if each_enemy in enemy1_group:
                                            score += enemy1_score
                                        elif each_enemy in enemy2_group:
                                            score += enemy2_score
                                        else:
                                            score += enemy3_score
                                        each_enemy.live = False

                    # if bullet shot some one then it regenerates
                    else:
                        pass
                        # each.reset(me.rect.center)
                        # screen.blit(each.image, each.rect)

                # ------------------------------- upgrade game level ----------------------------------
                if score >= 500 and level == 1:
                    level = 2
                    dis_level = True
                    enemy.monster1.HP = 2
                    enemy.monster2.HP = 25
                    enemy.monster3.HP = 75
                    enemy1_score = 20
                    enemy2_score = 300
                    enemy3_score = 900
                    add_enemy1(enemy1_group, enemies_group, 2, bg_size)
                    add_enemy2(enemy2_group, enemies_group, 2, bg_size)
                    add_enemy3(enemy3_group, enemies_group, 0, bg_size)
                    upgrade_sound.play()
                elif score >= 5000 and level == 2:
                    dis_level = True
                    level = 3
                    add_enemy1(enemy1_group, enemies_group, 2, bg_size)
                    add_enemy2(enemy2_group, enemies_group, 1, bg_size)
                    add_enemy3(enemy3_group, enemies_group, 1, bg_size)
                    enemy.monster1.HP = 5
                    enemy.monster2.HP = 50
                    enemy.monster3.HP = 150
                    enemy1_score = 100
                    enemy2_score = 750
                    enemy3_score = 3000
                    inc_speed(enemy1_group, 1)
                    upgrade_sound.play()
                elif score >= 50000 and level == 3:
                    bomb_white = True
                    bomb_white_count = 0
                    for eve in enemies_group:
                        if eve.rect.left < width:
                            eve.live = False
                    dis_level = True
                    level = 4
                    add_enemy1(enemy1_group, enemies_group, 2, bg_size)
                    add_enemy2(enemy2_group, enemies_group, 1, bg_size)
                    add_enemy3(enemy3_group, enemies_group, 1, bg_size)
                    enemy1_score = 300
                    enemy2_score = 1500
                    enemy3_score = 7500
                    enemy.monster1.HP = 16
                    enemy.monster2.HP = 80
                    enemy.monster3.HP = 240
                    upgrade_sound.play()
                    background = pygame.image.load(r'.\images\3.jpg').convert()
                elif score >= 200000 and level == 4:
                    dis_level = True
                    level = 5
                    upgrade_text = upgrade_font.render('LEVEL UP TO 5!', True, (255, 140, 0))
                    screen.blit(upgrade_text, (
                        width // 2 - upgrade_text.get_rect().width // 2,
                        height // 2 - upgrade_text.get_rect().height // 2))
                    add_enemy1(enemy1_group, enemies_group, 1, bg_size)
                    add_enemy2(enemy2_group, enemies_group, 1, bg_size)
                    add_enemy3(enemy3_group, enemies_group, 1, bg_size)
                    enemy.monster1.HP = 50
                    enemy.monster2.HP = 160
                    enemy.monster3.HP = 480
                    enemy1_score = 800
                    enemy2_score = 4000
                    enemy3_score = 20000
                    for each in bullet1_list:
                        each.change4()
                    inc_speed(enemy1_group, 1)
                    upgrade_sound.play()
                elif score >= 500000 and level == 5:
                    bomb_white = True
                    bomb_white_count = 0
                    for eve in enemies_group:
                        if eve.rect.left < width:
                            eve.live = False
                    dis_level = True
                    level = 6
                    upgrade_text = upgrade_font.render('LEVEL UP TO 6!', True, (255, 140, 0))
                    screen.blit(upgrade_text, (
                        width // 2 - upgrade_text.get_rect().width // 2,
                        height // 2 - upgrade_text.get_rect().height // 2))
                    add_enemy1(enemy1_group, enemies_group, 0, bg_size)
                    add_enemy2(enemy2_group, enemies_group, 2, bg_size)
                    add_enemy3(enemy3_group, enemies_group, 1, bg_size)
                    enemy.monster1.HP = 100
                    enemy.monster2.HP = 330
                    enemy.monster3.HP = 1000
                    enemy1_score = 1000
                    enemy2_score = 5000
                    enemy3_score = 30000
                    frames = 80
                    background = pygame.image.load(r'.\images\3-4.jpg').convert()
                    me.image1 = pygame.image.load(r'.\images\chao1.png').convert_alpha()
                    me.image2 = pygame.image.load(r'.\images\chao2.png').convert_alpha()

                    bullets.Bullet1.harm = harm_max
                    me.mask = pygame.mask.from_surface(me.image2)
                    for each in bullet1_list:
                        each.change6()
                    upgrade_sound.play()
                # upgrade -----------------------------------------------------------

            # -------------------------  ******* ME DIE ***********  ---------------------------
            else:
                # die
                # if not (delay % 3):
                if me_destroy_index == 0:
                    me_down_sound.play()
                if me_destroy_index < 20:
                    screen.blit(me.destroy_images[me_destroy_index // 5], me.rect)
                    me_destroy_index += 1
                elif me_destroy_index == 20:
                    me_live = False
                    me_destroy_index += 1
                elif me_destroy_index < 40:
                    me_destroy_index += 1
                elif me_destroy_index == 40:
                    me_destroy_index += 1
                    is_over_display = True
                    result = os.path.exists('Records.txt')

                    # ----------------- recored scores --------------------------
                    if not result:
                        with open('Records.txt', 'wb') as f:
                            f.write(('#排名1: ' + str(score) + '\r\n').encode('utf-8'))
                        new_record = True
                    if result:
                        with open('Records.txt', 'rb') as f:
                            lines = f.readlines()
                            n = len(lines)
                        # 1 - 10 record(s)
                        if n < 100:
                            records = []
                            for eve in lines:
                                k = eve.decode('utf-8').split(sep=': ')[1]
                                records.append(int(str.replace(k, '\r\n', '')))
                            records.append(score)
                            records = sorted(records)
                            if score == records[len(records) - 1]:
                                new_record = True
                            with open('Records.txt', 'wb') as f:
                                for i in range(0, len(records)):
                                    f.write(('#排名' + str(i + 1) + ': ' + str(records[n - i]) + '\r\n').encode('utf-8'))
                        # 100 records
                        else:
                            records = []
                            with open('Records.txt', 'rb') as f:
                                for eve in lines:
                                    k = eve.decode('utf-8').split(sep=': ')[1]
                                    records.append(int(str.replace(k, '\r\n', '')))
                            with open('Records.txt', 'wb') as f:
                                records = sorted(records)
                                if score == records[len(records) - 1]:
                                    new_record = True
                                if records[0] >= score:
                                    break
                                else:
                                    records[0] = score
                                records = sorted(records)
                                for i in range(100):
                                    f.write(('#排名' + str(i + 1) + ': ' + str(records[99 - i]) + '\r\n').encode('utf-8'))
                else:
                    if new_record:
                        new_rec_font = pygame.font.Font(r'.\font\font.ttf', 50)
                        new_rec_text = new_rec_font.render('New Record', True, (255, 100, 100))
                        screen.blit(new_rec_text, ((width - new_rec_text.get_rect().width) // 2, 180))

                    # screen.blit(over_image, over_rect)
                    # screen.blit(again_image, again_rect)
                    # ----------------------------------------------------------------------------
                    enemy3_fly_sound.stop()
                    pygame.mixer.music.stop()


        # -------------------- set score image ------------------
        if score < 5000:
            score_text = score_font.render(' Score:' + str(score), True, (255, 255, 255))
        elif score < 50000:
            score_text = score_font.render(' Score:' + str(score), True, (210, 147, 65))
        else:
            score_text = score_font.render(' Score:' + str(score), True, (255, 0, 0))

        # -------------------- set levelup image ------------------
        level_text = level_font.render('Level:' + str(level), True, (255, 255, 255))

        # ----------------------- set bomb image  -----------------
        if bomb_num < bomb_num_max:
            bomb_text = bomb_font.render('×' + str(bomb_num), True, (255, 255, 255))
        else:
            bomb_text = bomb_font.render('×' + str(bomb_num), True, (255, 0, 0))

        # -------------- display bomb and scores images ---------------------------
        if dis_level and dis_level_time < 80:
            upgrade_text = upgrade_font.render('LEVEL UP TO ' + str(level) + '!', True, (255, 255, 255))
            screen.blit(upgrade_text, (
                width // 2 - upgrade_text.get_rect().width // 2, height // 2 - upgrade_text.get_rect().height // 2))
            dis_level_time += 1
        else:
            dis_level_time = 0
            dis_level = False

        # ------------------------- full white ------------------------------------

        if bomb_white:
            if bomb_white_count < 85:
                bomb_white_count += 1
                s = pygame.Surface((width, height)).convert_alpha()
                s.fill((255, 255, 170 + bomb_white_count, bomb_white_count * 3))
                screen.blit(s, (0, 0))
            elif bomb_white_count < 170:
                bomb_white_count += 1
                s = pygame.Surface((width, height)).convert_alpha()
                s.fill((255, 255, 341 - bomb_white_count,  255 - (bomb_white_count - 85) * 3))
                screen.blit(s, (0, 0))
            else:
                bomb_white = False

        # ----------------------- set off bomb tip --------------------------------

        if need_tip:
            if tip_count < 120:
                tip_count += 1
                bomb_tip_text_rect.left = bomb_image.get_rect().width + bomb_text.get_rect().width
                screen.blit(bomb_tip_text, bomb_tip_text_rect)
            elif bomb_tip_text_rect.left < width:
                tip_count += 1
                bomb_tip_text_rect.left = bomb_image.get_rect().width + bomb_text.get_rect().width + bomb_tip_text_rect.width + (tip_count - 120) * 12
                screen.blit(bomb_tip_text, bomb_tip_text_rect)
            elif bomb_tip_text.get_rect().left > width:
                need_tip = False

        # ------------------- game over display --------------------
        if is_over_display:
            screen.blit(over_image, over_rect)
            screen.blit(again_image, again_rect)

        screen.blit(score_text, (0, 0))
        screen.blit(level_text, (width // 2 - level_text.get_rect().width // 2, 0))
        screen.blit(bomb_image, (0, height - bomb_image.get_rect().height))
        screen.blit(bomb_text, (bomb_image.get_rect().width, height - bomb_image.get_rect().height))

        pygame.display.update()



if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except Exception as e:
        traceback.print_exc()
        pygame.quit()
        print(e)
        input()
