import os.path
import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

#окно игры
bottom_panel = 150
screen_width = 800
screen_height = 390 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle")

#определяем шрифт
# font = pygame.font.SysFont('Times New Roman', 26)
# font = pygame.font.Font("fonts/timesnewromanpsmt.ttf", 26)

#определяем цвета
red = (255, 0, 0)
green = (0, 255, 0)
grey = (128, 128, 128)

#загружаем картинки
#фон
current_path = os.path.dirname(__file__)
# backgroind_img_path = os.path.join(current_path, "imgs/background")
background_img = pygame.image.load(os.path.join(current_path, "imgs/background/1.png")).convert_alpha()
panel_img = pygame.image.load(os.path.join(current_path, "imgs/icons/2.jpg")).convert_alpha()
sword_img = pygame.image.load(os.path.join(current_path, "imgs/icons/sword.png")).convert_alpha()
heal_img = pygame.image.load(os.path.join(current_path, "imgs/icons/heal.png")).convert_alpha()
end_img = pygame.image.load(os.path.join(current_path, "imgs/icons/end.png")).convert_alpha()


# #игровые константы
# current_fighter = 1
# total_fighters = 3
# action_cooldown = 0
# action_wait_time = 90
# attack = False
# potion = False
# clicked = False
# finnish = False
# game_over = 0

# отрисовка урона
# class DamageText(pygame.sprite.Sprite):
#     def __init__(self, x, y, damage, colour):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = font.render(damage, True, colour)
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.counter = 0
#
#     def update(self):
#         self.rect.y -= 1
#         self.counter += 1
#         if self.counter > 30:
#             self.kill()

damage_text_group = pygame.sprite.Group()

#функция для вывода текста
# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x, y))


#функция для фона
def draw_bg():
    screen.blit(background_img, (0, 0))
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    #статы рыцаря вывод
    # draw_text(f'{knight.name} HP: {knight.hp}', red, 100, screen_height - bottom_panel + 10)
    # #статы бандитов
    # for count, i in enumerate(bandit_list):
    #     draw_text(f'{i.name} HP: {i.hp}', red, 550, (screen_height - bottom_panel + 10) + count * 60)


#класс война
class Fighter():
    def __init__(self, x, y, name, maxhp, strength, potions):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        #загружаем анимации афк
        temp_list = []
        for i in range(8):
            img = pygame.image.load(os.path.join(os.path.join(current_path, f'imgs/{self.name}/Idle/{i}.png')))
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #загр анимации атаки
        temp_list = []
        for i in range(8):
            img = pygame.image.load(os.path.join(current_path, f'imgs/{self.name}/Attack/{i}.png'))
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #загр анимации получения урона
        temp_list = []
        for i in range(3):
            img = pygame.image.load(os.path.join(current_path, f'imgs/{self.name}/Hurt/{i}.png'))
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #загр анимации смерти
        temp_list = []
        for i in range(10):
            img = pygame.image.load(os.path.join(current_path, f'imgs/{self.name}/Death/{i}.png'))
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        # обновляем анимации
        self.image = self.animation_list[self.action][self.frame_index]
        # проверяем время сколько прошло
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #петля для анимаций
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        #возвращение анимаций в афк
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        #урон
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        #анимация урона
        target.hurt()
        #проверка на смерть
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        # damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        # damage_text_group.add(damage_text)
        #анимация атаки
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        #анимация получения урона отрисовка
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # анимация смерти
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        #обновляет хп
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150* ratio, 20))

class Button():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.height = height
        # self.width = width
        # self.potions = potions
        self.image = pygame.image.load(os.path.join(current_path, 'imgs/icons/potion.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

    def death(self):
        pass



knight = Fighter(200, 260, "Knight", 30, 10, 3)
bandit1 = Fighter(550, 270, "bandit", 20, 6, 1)
bandit2 = Fighter(700, 270, "bandit", 20, 6, 1)
potion_button1 = Button(110, screen_height - bottom_panel + 90)
potion_button2 = Button(145, screen_height - bottom_panel + 90)
potion_button3 = Button(178, screen_height - bottom_panel + 90)


potion_list = []
potion_list.append(potion_button1)
potion_list.append(potion_button2)
potion_list.append(potion_button3)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.maxhp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.maxhp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.maxhp)

def run_RPG():
    run = True
    # игровые константы
    current_fighter = 1
    total_fighters = 3
    action_cooldown = 0
    action_wait_time = 90
    attack = False
    potion = False
    clicked = False
    finnish = False
    game_over = 0
    while run:

        clock.tick(fps)

        #отрисовка
        draw_bg()
        draw_panel()
        knight_health_bar.draw(knight.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)
        knight.update()
        knight.draw()
        for Button in potion_list:
            Button.draw()
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()

        #текст урона
        damage_text_group.update()
        damage_text_group.draw(screen)

        #контроль действий игрока
        attack = False
        potion = False
        target = None
        #удостоверяемся что мышка видна
        # pygame.mouse.set_visible(True)
        pos = pygame.mouse.get_pos()
        for count, bandit in enumerate(bandit_list):
            if bandit.rect.collidepoint(pos):
                #работа с курсором
                # pygame.mouse.set_visible(False)
                screen.blit(sword_img, pos)
                if clicked == True and bandit.alive == True:
                    attack = True
                    target = bandit_list[count]

        #кнопка для зелий
        for count, Button in enumerate(potion_list):
            if Button.rect.collidepoint(pos):
                # pygame.mouse.set_visible(False)
                screen.blit(heal_img, pos)
                if clicked == True:
                    if  knight.alive:
                        if knight.hp < knight.maxhp:
                            for i in range(10):
                                knight.hp += 1
                                if knight.hp >= knight.maxhp:
                                    break
                        potion_list.pop(count)

        if game_over == 0:
            #ход игрока
            if knight.alive == True:
                if current_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #действие
                        if attack == True and target != None:
                            knight.attack(target)
                            current_fighter += 1
                            action_cooldown = 0
            else:
                game_over = -1

            #ход врага
            for count, bandit in enumerate(bandit_list):
                if current_fighter == 2 + count:
                    if bandit.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            #атака
                            bandit.attack(knight)
                            current_fighter += 1
                            action_cooldown = 0
                    else:
                        current_fighter += 1

            #если все походили то ресет
            if current_fighter > total_fighters:
                current_fighter = 1

        #проверка на смерть всех бандитов
        alive_bandits = 0
        for bandit in bandit_list:
            if bandit.alive == True:
                alive_bandits += 1
        if alive_bandits == 0:
            game_over = 1

        if game_over != 0:
            screen.blit(end_img, (200, 150))
            if finnish == True:
                run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False
            if event.type == pygame.MOUSEWHEEL:
                finnish = True

        pygame.display.update()

    pygame.quit()
run_RPG()
