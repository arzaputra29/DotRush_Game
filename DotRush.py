import pygame
import random
import time
import os
pygame.init()

# Display
width = 500
height = 300
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('DotRush')

# Colors
white = (255,255,255)
black = (0, 0, 0)
green = (27, 179, 98)
red = (200, 50, 50)

# Font
font = pygame.font.SysFont("Segoe UI", 14, bold=True)
game_over_font = pygame.font.SysFont("Segoe UI", 30, bold=True)

# Text positions
x_text_1, y_text_1 = 10, 10
x_text_2, y_text_2 = 10, 30
x_text_3, y_text_3 = 400, 10
x_text_4, y_text_4 = 150, 100

# Line position
y_line_start = 60

# Square
x_rect, y_rect = 250, 150
width_rect, height_rect = 50, 50

# Speed
speed = 1.5

# Lingkaran
radius = 3
falling_circles = []
falling_speed = 1.2

# Clock
clock = pygame.time.Clock()
# heart
heart = 5

# Run
run = True
while run:
    clock.tick(60)  # Batasi ke 60 FPS
    display.fill(white)

    # Text koordinat
    text_1 = font.render(f"X : {int(x_rect)}", True, black)
    text_2 = font.render(f"Y : {int(y_rect)}", True, black)
    text_3 = font.render(f"Heart : {int(heart)}", True, black)
    text_4 = game_over_font.render(f"Game Over", True, black)
    display.blit(text_1, (x_text_1, y_text_1))
    display.blit(text_2, (x_text_2, y_text_2))
    display.blit(text_3, (x_text_3, y_text_3))

    # Garis dan kotak
    pygame.draw.line(display, black, (0, y_line_start), (width, y_line_start), width=1)
    kotak_rect = pygame.draw.rect(display, green, (x_rect, y_rect, width_rect, height_rect))

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Generate lingkaran baru
    if random.randint(0, 25) < 2:
        x_circle = random.randint(0, width - radius * 2)
        falling_circles.append([x_circle, y_line_start])

    # Update dan gambar lingkaran
    for circle in falling_circles[:]:
        circle[1] += falling_speed
        pygame.draw.circle(display, red, (circle[0], int(circle[1])), radius)

        # Deteksi tabrakan
        lingkaran_rect = pygame.Rect(circle[0] - radius, circle[1] - radius, radius * 2, radius * 2)
        if kotak_rect.colliderect(lingkaran_rect):
            heart -= 1
            falling_circles.remove(circle)

        # Hapus lingkaran jika keluar layar
        if circle[1] > height:
            falling_circles.remove(circle)
    

    # Kontrol
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and y_rect > y_line_start + 2:
        y_rect -= speed
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y_rect + height_rect < height:
        y_rect += speed
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x_rect + width_rect < width:
        x_rect += speed
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x_rect > 0:
        x_rect -= speed
    
    if heart <= 0:
        display.blit(text_4, (x_text_4, y_text_4))
        time.sleep(1.5)
        run = False
        

    # update
    pygame.display.flip()

pygame.quit()
print("Arza © 2025 Present")