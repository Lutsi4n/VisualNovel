#
# # Our imports(libraries)
# import turtle
# import time
# import random
# import pygame
#
# # Music
#
# pygame.mixer.init()
#
# pygame.mixer.music.load("Ryu_music.mp3")
# pygame.mixer.music.play(loops=0)
#
# screen = turtle.Screen()
# screen.setup(1280, 540)
# screen.bgpic("bg.png")
#
# # Players
#
# # Player 1
# Ryu = "Ryu.gif"
# Player1 = turtle.Turtle()
# screen.addshape(Ryu)
# Player1.shape(Ryu)
# print(Player1.shapesize())
# Player1.penup()
# Player1.speed(8000)
# Player1.goto(800,-100)
#
# # Player 2
#
# Guile = "Guile.gif"
# Player2 = turtle.Turtle()
# screen.addshape(Guile)
# Player2.shape(Guile)
# print(Player1.shapesize())
# Player2.penup()
# Player2.speed(8000)
# Player2.goto(-800,-100)
#
# # 2 variables: First for Guile and second for Ryu
#
# # Heart variables
#
# Health_Bar1 = 100
# Health_Bar2 = 100
#
# # Health_Bar1
#
# Health_Bar1_turtle = turtle.Turtle()
# Health_Bar1_turtle.ht()
# Health_Bar1_turtle.speed(0)
# Health_Bar1_turtle.color("yellow")
# Health_Bar1_turtle.penup()
# Health_Bar1_turtle.goto(50,220)
# Health_Bar1_turtle.pendown()
#
#
# # Health_Bar2
#
# Health_Bar2_turtle = turtle.Turtle()
# Health_Bar2_turtle.ht()
# Health_Bar2_turtle.speed(0)
# Health_Bar2_turtle.color("yellow")
# Health_Bar2_turtle.penup()
# Health_Bar2_turtle.goto(-50,220)
# Health_Bar2_turtle.left(180)
# Health_Bar2_turtle.pendown()
#
# # x value is 290 for the starting point. y value is 80.
# Bg_Health_Bar = turtle.Turtle()
# Bg_Health_Bar.color("#f01717")
# Bg_Health_Bar.ht()
# Bg_Health_Bar.speed(9000)
# Bg_Health_Bar.penup()
# Bg_Health_Bar.goto(-600,220)
# Bg_Health_Bar.pendown()
# Bg_Health_Bar.pensize(3)
# Bg_Health_Bar.begin_fill()
#
# for i in range(2):
#     Bg_Health_Bar.forward(1200)
#     Bg_Health_Bar.left(90)
#     Bg_Health_Bar.forward(30)
#     Bg_Health_Bar.left(90)
# Bg_Health_Bar.end_fill()
#
# # Functions for moving and health loss
#
# # Heart loss when enemy attacks
# def perform_action():
#     # код действий, которые нужно выполнить при нажатии клавиши "Enter"
#     # turtle.Screen().clearscreen()
#     screen.bgpic("bg2.png")
#     # screen.bgpic("StreetFighterBg.gif")
#     Player1.goto(400, -100)
#     Player2.goto(-400, -100)
#
# # Ryu
# def drawHeart1():
#     # If Ryu is dead
#     if Health_Bar1 <= 0:
#         screen.clear()
#         screen.bgpic("win2.png")
#     else:
#         Health_Bar1_turtle.clear()
#         # Health_Bar1_turtle
#         size = 550 * Health_Bar1 / 100
#         Health_Bar1_turtle.begin_fill()
#         for i in range(2):
#             Health_Bar1_turtle.forward(size)
#             Health_Bar1_turtle.left(90)
#             Health_Bar1_turtle.forward(30)
#             Health_Bar1_turtle.left(90)
#         Health_Bar1_turtle.end_fill()
#
# # Guile
# def drawHeart2():
#     # If Guile is dead
#     if Health_Bar2 <= 0:
#         screen.clear()
#         screen.bgpic("win1.png")
#     else:
#         Health_Bar2_turtle.clear()
#         # Health_Bar2_turtle
#         size = 550 * Health_Bar2 / 100
#         Health_Bar2_turtle.begin_fill()
#         for i in range(2):
#             Health_Bar2_turtle.forward(size)
#             Health_Bar2_turtle.right(90)
#             Health_Bar2_turtle.forward(30)
#             Health_Bar2_turtle.right(90)
#         Health_Bar2_turtle.end_fill()
#
# # Movement functions
# def leftArrow():
#     Player1.backward(30)
#
# def Space():
#     global Health_Bar2
#     Ryu_punch = "Ryu_punch.gif"
#     screen.addshape(Ryu_punch)
#     Player1.shape(Ryu_punch)
#     time.sleep(0.2)
#     Ryu = "Ryu.gif"
#     Player1.shape(Ryu)
#     if Player1.distance(Player2) < 240:
#         Health_Bar2 -= 5
#         drawHeart2()
#         Player2.backward(12)
#     time.sleep(.1)
#
# def rightArrow():
#     Player1.forward(30)
#
# def K():
#     global Health_Bar2
#     Ryu_kick = "Ryu_kick.gif"
#     screen.addshape(Ryu_kick)
#     Player1.shape(Ryu_kick)
#     time.sleep(0.2)
#     Ryu = "Ryu.gif"
#     Player1.shape(Ryu)
#     if Player1.distance(Player2) < 220:
#         Health_Bar2 -= 10
#         drawHeart2()
#         Player2.backward(20)
#     time.sleep(.1)
#
# def P():
#     global Health_Bar2
#     Ryu_fight = "Ryu_fighting.gif"
#     screen.addshape(Ryu_fight)
#     Player1.shape(Ryu_fight)
#     time.sleep(0.2)
#     Ryu = "Ryu.gif"
#     Player1.shape(Ryu)
#     if Player1.distance(Player2) < 250:
#         Health_Bar2 -= 15
#         drawHeart2()
#         Player2.backward(40)
#     time.sleep(.1)
#
# def upArrow():
#     Ryu_Jump = "Ryu_Jump.gif"
#     screen.addshape(Ryu_Jump)
#     Player1.shape(Ryu_Jump)
#     Player1.left(90)
#     Player1.forward(200)
#     Player1.left(180)
#     time.sleep(0.5)
#     Player1.forward(200)
#     Player1.right(270)
#     Ryu = "Ryu.gif"
#     Player1.shape(Ryu)
#
# screen.listen()
# screen.onkey(leftArrow,"Left")
# screen.onkey(Space,"space")
# screen.onkey(rightArrow, "Right")
# screen.onkey(K,"k")
# screen.onkey(P,"p")
# screen.onkey(upArrow,"Up")
# screen.onkey(perform_action, "Return")
#
# # Player 2
#
# def A():
#     Player2.backward(30)
#
# def D():
#     Player2.forward(30)
#
# def Q():
#     global Health_Bar1
#     Guile_kick = "Guile_kick.gif"
#     screen.addshape(Guile_kick)
#     Player2.shape(Guile_kick)
#     time.sleep(0.2)
#     Guile = "Guile.gif"
#     Player2.shape(Guile)
#     if Player2.distance(Player1) < 235:
#         Health_Bar1 -= 10
#         drawHeart1()
#         Player1.forward(20)
#     time.sleep(.1)
#
# def P2():
#     global Health_Bar1
#     Guile_Bam = "Guile-punch.gif"
#     screen.addshape(Guile_Bam)
#     Player2.shape(Guile_Bam)
#     time.sleep(0.2)
#     Guile = "Guile.gif"
#     Player2.shape(Guile)
#     if Player2.distance(Player1) < 235:
#         Health_Bar1 -= 5
#         drawHeart1()
#         Player1.forward(12)
#     time.sleep(.1)
#
# def G():
#     global Health_Bar1
#     Guile_rkick = "Guile_flashkick.gif"
#     screen.addshape(Guile_rkick)
#     Player2.shape(Guile_rkick)
#     time.sleep(0.2)
#     Guile = "Guile.gif"
#     Player2.shape(Guile)
#     if Player2.distance(Player1) < 250:
#         Health_Bar1 -= 15
#         drawHeart1()
#         Player1.forward(40)
#     time.sleep(.1)
#
# def W():
#     Guile_Jump = "Guile_jump.gif"
#     screen.addshape(Guile_Jump)
#     Player2.shape(Guile_Jump)
#     Player2.left(90)
#     Player2.forward(200)
#     Player2.left(180)
#     time.sleep(0.5)
#     Player2.forward(200)
#     Player2.right(270)
#     Guile = "Guile.gif"
#     Player2.shape(Guile)
#
# screen.listen()
# screen.onkey(A,"a")
# screen.onkey(D,"d")
# screen.onkey(Q,"q")
# screen.onkey(P2,"e")
# screen.onkey(G,"g")
# screen.onkey(W,"w")
#
# drawHeart1()
# drawHeart2()
# turtle.mainloop()
#
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Create the game window
screen_width = 1280
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Street Fighter")

# Load background image
bg_image = pygame.image.load("bg.png").convert()

# Load player images
ryu_image = pygame.image.load("Ryu.gif").convert_alpha()
guile_image = pygame.image.load("Guile.gif").convert_alpha()

# Load attack images
ryu_punch_image = pygame.image.load("Ryu_punch.gif")
ryu_kick_image = pygame.image.load("Ryu_kick.gif")
ryu_fighting_image = pygame.image.load("Ryu_fighting.gif")
guile_kick_image = pygame.image.load("Guile_kick.gif")
guile_punch_image = pygame.image.load("Guile-punch.gif")
guile_flashkick_image = pygame.image.load("Guile_flashkick.gif")

# Set initial player positions
ryu_x = 800
ryu_y = 300
guile_x = 400
guile_y = 300

# Set initial health values
health_bar1 = 100
health_bar2 = 100

# Load music
pygame.mixer.init()
pygame.mixer.music.load("Ryu_music.mp3")
pygame.mixer.music.play(loops=-1)

# Flag for performing action
perform_action = False

# Initialize player actions
ryu_attacking = False
guile_attacking = False

# Initialize player directions
ryu_direction = "right"
guile_direction = "left"

# Function for drawing health bars
def draw_health_bars():
    pygame.draw.rect(screen, (255, 255, 0), (50, 20, int(550 * health_bar1 / 100), 30))
    pygame.draw.rect(screen, (255, 255, 0), (screen_width - 600, 20, int(550 * health_bar2 / 100), 30))

# Function for resetting players and health bars
def reset_players():
    global ryu_x, guile_x, health_bar1, health_bar2
    ryu_x = 800
    guile_x = 400
    health_bar1 = 100
    health_bar2 = 100

# Function for checking game over conditions
def check_game_over():
    if health_bar1 <= 0:
        screen.blit(pygame.image.load("win2.png").convert(), (0, 0))
        pygame.display.flip()
        time.sleep(3)
        return True
    elif health_bar2 <= 0:
        screen.blit(pygame.image.load("win1.png").convert(), (0, 0))
        pygame.display.flip()
        time.sleep(3)
        return True
    return False
def change():
    screen.blit(pygame.image.load("bg2.png").convert(), (0, 0))
    reset_players()


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    guile_direction = "right"
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                perform_action = True
                change()

            elif event.key == pygame.K_SPACE:
                ryu_attacking = True
            elif event.key == pygame.K_k:
                ryu_attacking = True
            elif event.key == pygame.K_p:
                ryu_attacking = True
            # elif event.key == pygame.K_a:
            #     # guile_direction = "left"
            # elif event.key == pygame.K_d:
            #     guile_direction = "right"
            elif event.key == pygame.K_q:
                guile_attacking = True
            elif event.key == pygame.K_e:
                guile_attacking = True
            elif event.key == pygame.K_g:
                guile_attacking = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                ryu_attacking = False
            elif event.key == pygame.K_k:
                ryu_attacking = False
            elif event.key == pygame.K_p:
                ryu_attacking = False
            elif event.key == pygame.K_q:
                guile_attacking = False
            elif event.key == pygame.K_e:
                guile_attacking = False
            elif event.key == pygame.K_g:
                guile_attacking = False

    # Perform action if flagged
    if perform_action:
        screen.blit(pygame.image.load("bg2.png").convert(), (0, 0))
        reset_players()
        perform_action = False

    # Update player positions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if ryu_x - 30 > 0:
            ryu_x -= 30
            # ryu_direction = "left"
    if keys[pygame.K_RIGHT]:
        if ryu_x + ryu_image.get_width() + 30 < screen_width:
            ryu_x += 30
            # ryu_direction = "right"
    if keys[pygame.K_SPACE]:
        if abs(ryu_x - guile_x) < 240:
            health_bar2 -= 5
            guile_x -= 12
    if keys[pygame.K_k]:
        if abs(ryu_x - guile_x) < 220:
            health_bar2 -= 10
            guile_x -= 20
    if keys[pygame.K_p]:
        if abs(ryu_x - guile_x) < 250:
            health_bar2 -= 15
            guile_x -= 40
    if keys[pygame.K_a]:
        if guile_x - 30 > 0:
            guile_x -= 30
    if keys[pygame.K_d]:
        if guile_x + guile_image.get_width() + 30 < screen_width:
            guile_x += 30
    if keys[pygame.K_q]:
        if abs(ryu_x - guile_x) < 235:
            health_bar1 -= 10
            ryu_x += 20
            guile_attacking = True
    if keys[pygame.K_e]:
        if abs(ryu_x - guile_x) < 235:
            health_bar1 -= 5
            ryu_x += 12
            guile_attacking = True
    if keys[pygame.K_g]:
        if abs(ryu_x - guile_x) < 250:
            health_bar1 -= 15
            ryu_x += 40
            guile_attacking = True

    # Clear the screen
    screen.blit(bg_image, (0, 0))

    # Draw the players
    if ryu_attacking:
        # Replace Ryu's sprite with attack sprite based on the current action
        if keys[pygame.K_SPACE]:
            screen.blit(ryu_punch_image, (ryu_x, ryu_y))
        elif keys[pygame.K_k]:
            screen.blit(ryu_kick_image, (ryu_x, ryu_y))
        elif keys[pygame.K_p]:
            screen.blit(ryu_fighting_image, (ryu_x, ryu_y))
    else:
        # Draw Ryu's normal sprite based on the current direction
        if ryu_direction == "right":
            screen.blit(ryu_image, (ryu_x, ryu_y))
        elif ryu_direction == "left":
            screen.blit(pygame.transform.flip(ryu_image, True, False), (ryu_x, ryu_y))

    if guile_attacking:
        # Replace Guile's sprite with attack sprite based on the current action
        if keys[pygame.K_q]:
            screen.blit(guile_kick_image, (guile_x, guile_y))
        elif keys[pygame.K_e]:
            screen.blit(guile_punch_image, (guile_x, guile_y))
        elif keys[pygame.K_g]:
            screen.blit(guile_flashkick_image, (guile_x, guile_y))
    else:
        # Draw Guile's normal sprite based on the current direction
        if guile_direction == "right":
            screen.blit(guile_image, (guile_x, guile_y))
        elif guile_direction == "left":
            screen.blit(pygame.transform.flip(guile_image, True, False), (guile_x, guile_y))

    # Draw health bars
    draw_health_bars()

    # Check game over conditions
    if check_game_over():
        break

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

