#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pygame
import threading
import time

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Missile Attack")

# Load the background image
background = pygame.image.load("F:\\istockphoto-498309616-170667a.webp")
background = pygame.transform.scale(background, (800, 600))

# Load the missile image
missile_image = pygame.image.load("C:\\Users\\HP\\Downloads\\bomb (1).png")
missile_rect = missile_image.get_rect()
missile_rect.center = (700, 200)

# Load the explosion image
explosion_image = pygame.image.load("C:\\Users\\HP\\Downloads\\explosion.png")
explosion_rect = explosion_image.get_rect()

# Load the explosion sound
explosion_sound = pygame.mixer.Sound("C:\\Users\\HP\\Downloads\\tie-fighter-explodemp3-14597.mp3")

# Define the animation functions
def missile_animation():
    global missile_rect
    for _ in range(100):
        missile_rect.y += 3
        time.sleep(0.03)

def explosion_animation():
    global explosion_rect
    explosion_rect.center = missile_rect.center
    explosion_sound.play()
    for i in range(700, 460):
        explosion_rect.size = (i*20, i*20)
        time.sleep(0.03)

# Start the missile animation thread
missile_thread = threading.Thread(target=missile_animation)
missile_thread.start()

# Run the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    if missile_thread.is_alive():
        screen.blit(missile_image, missile_rect)
    else:
        screen.blit(explosion_image, (550,400))

    pygame.display.flip()

# Clean up and exit
pygame.quit()


# In[ ]:




