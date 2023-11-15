import pygame

import random

pygame.init()
screen = pygame.display.set_mode((2100, 1100))
running = True


def asteroidMove(astroid, speed):
    if astroid.y > 1100:
        astroid.y = 0
        astroid.x = random.randint(0, 2000)
    astroid.move_ip(0, speed)


red = (245, 0, 0)
black = (0, 0, 0)
font = pygame.font.Font('praetoria.regular.otf', 62)
inv = False
deathPause = 0
lives = 3

w = (255, 255, 255)


def death(astroid, player):
    global inv
    global w
    global deathPause
    global lives
    if astroid.x - player.width <= player.x <= astroid.x + astroid.width and inv == False:
        if astroid.y - player.height <= player.y <= astroid.y + astroid.height:
            player.x = 900
            player.y = 1000
            lives -= 1
            inv = True
            w = red
            deathPause = score


b = (46, 35, 31)
score = 0

player = pygame.rect.Rect((900, 1000, 80, 80))
astroid1 = pygame.rect.Rect((random.randint(0, 2000), 0, 100, 100))
astroid2 = pygame.rect.Rect((random.randint(0, 2000), -909, 100, 100))
astroid3 = pygame.rect.Rect((random.randint(0, 2000), -682, 100, 100))
astroid4 = pygame.rect.Rect((random.randint(0, 2000), -278, 100, 100))
astroid5 = pygame.rect.Rect((random.randint(0, 2000), -154, 100, 100))
astroid6 = pygame.rect.Rect((random.randint(0, 2000), -1234, 100, 100))
astroid7 = pygame.rect.Rect((random.randint(0, 2000), -234, 100, 100))

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill((0, 0, 0))
    clock.tick(100)

    text = font.render("score: " + str(score), True, red, black)
    screen.blit(text, (1000, 1))

    if lives == 0:
        running = False

    score += 1

    if score == deathPause + 50 and inv == True:
        w = (46, 44, 44)
    if score == deathPause + 180 and inv == True:
        inv = False
        w = (255, 255, 255)

    pygame.draw.rect(screen, w, player)
    pygame.draw.rect(screen, b, astroid1)
    pygame.draw.rect(screen, b, astroid2)
    pygame.draw.rect(screen, b, astroid3)
    pygame.draw.rect(screen, b, astroid4)
    pygame.draw.rect(screen, b, astroid5)
    pygame.draw.rect(screen, b, astroid6)
    pygame.draw.rect(screen, b, astroid7)

    # controls

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and player.x > 0:
        player.x -= 5

    if key[pygame.K_RIGHT] and player.x < 2020:
        player.x += 5

    asteroidMove(astroid1, 5)
    asteroidMove(astroid2, 6)
    asteroidMove(astroid3, 7)
    asteroidMove(astroid4, 8)
    asteroidMove(astroid5, 9)
    asteroidMove(astroid6, 10)
    asteroidMove(astroid7, 11)

    death(astroid1, player)
    death(astroid2, player)
    death(astroid3, player)
    death(astroid4, player)
    death(astroid5, player)
    death(astroid6, player)
    death(astroid7, player)

    pygame.display.update()
