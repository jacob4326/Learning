import pygame
import random
pygame.init()
pygame.display.set_caption("KSP")
icon = pygame.image.load('Screenshot 2026-02-11 191744 - Copy.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1500, 1000))
fps = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
x, y = 320, 240
speed = 10
running = True
SPACE_pressed = False
c_pressed = False
v_pressed = False
q_pressed = False
o_pressed = False
r_pressed = False
lava_timer = pygame.USEREVENT + 1
try:
    image = pygame.image.load('Screenshot 2026-02-11 191744 - Copy.png')
except pygame.error as e:
    print(f"Error loading image: {e}")
    image = None
pygame.mixer.music.load('Fluffing-a-Duck(chosic.com).mp3')
pygame.mixer.music.play(-1)  # start background music once
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.time.set_timer(lava_timer, 32000)  
            pygame.mixer.Sound('jack-black-steves-lava-chicken.mp3').play()
            image = pygame.image.load("Screenshot 2025-04-21 213434.png")
        if event.type == lava_timer:
            image = pygame.image.load('Screenshot 2026-02-11 191744 - Copy.png')
            pygame.time.set_timer(lava_timer, 0)  # Stop the timer
    screen.fill((30,30,30))#background color
    text_surface = font.render(f'Speed: {speed}', True, (255, 255, 255))  # creates text
    screen.blit(text_surface, (10, 10))  # draws text on screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_q]:
        if not q_pressed:
            pygame.mixer.Sound('morse (1).wav').play()
            q_pressed = True
    else:
        q_pressed = False
    if x>1450 or x<-50 or y>800 or y<-50:
        running = False
    if keys[pygame.K_k]:
        pygame.display.set_mode((640, 480))
    if keys[pygame.K_l]:
        pygame.display.set_mode((1500, 1000))
    if keys[pygame.K_SPACE]:
        if not SPACE_pressed:
            x = random.randint(-50, 1450)
            y = random.randint(-50, 800)
            SPACE_pressed = True
    else:
        SPACE_pressed = False
    if keys[pygame.K_c]:
        if not c_pressed:  # c_pressed = False before the loop
            speed += 1
            c_pressed = True
    else:
        c_pressed = False
    if keys[pygame.K_v]:
        if not v_pressed:  # v_pressed = False before the loop
            speed -= 1
            v_pressed = True
    else:
        v_pressed = False
    if keys[pygame.K_o]:
        if not o_pressed:
            pygame.mixer.Sound("steve-old-hurt-sound_XKZxUk4.mp3").play()
            o_pressed = True
    else:
        o_pressed = False
    if keys[pygame.K_r]:
        if not r_pressed:
            pygame.mixer.Sound("no-no-wait-wait-101soundboards.mp3").play()
            r_pressed = True
    else:
        r_pressed = False
    if image:
        screen.blit(image, (x + 50, y + 50))
    pygame.display.flip()#updates display
    fps.tick(120)#fps
pygame.quit()