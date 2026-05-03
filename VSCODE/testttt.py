import pygame
import random
pygame.init()
pygame.display.set_caption("Simulation")
icon = pygame.image.load("Screenshot 2025-04-21 213434.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1500, 1000))
fps = pygame.time.Clock()
running = True
x = 1700
y = 1400
font = pygame.font.SysFont(None, 36)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30,30,30))
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False


    button_rect = pygame.Rect(400, 600, 200, 150)
    pygame.draw.rect(screen, (125, 0, 0), button_rect)
    button_text = font.render("Play", True, (255, 255, 255))
    screen.blit(button_text, (button_rect.x + (button_rect.width//2) - (button_text.get_width()//2), button_rect.y + (button_rect.height//2) - (button_text.get_height()//2)))

    if button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        print("Button clicked!")

    pygame.display.flip()
    fps.tick(60)
pygame.quit()