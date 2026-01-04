import pygame
import random
pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")
clock = pygame.time.Clock()
player = pygame.Rect(200, 350, 80, 20)
ball = pygame.Rect(random.randint(0, 480), 0, 20, 20)
score = 0
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    ball.y += 4
    if ball.colliderect(player):
        score += 1
        ball.y = 0
        ball.x = random.randint(0, 480)
    if ball.y > HEIGHT:
        running = False
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

