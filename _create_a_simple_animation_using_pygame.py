# -*- coding: utf-8 -*-
""". Create a Simple Animation Using Pygame.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J9-deS1hH3GgHdNWy69qAWydH1FJXgKO
"""

import pygame

def animate_circle():
    pygame.init()
    window = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Circle Animation")

    x = 50
    y = 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill((255, 255, 255))
        pygame.draw.circle(window, (0, 0, 255), (x, y), 30)
        x += 5  # Move circle to the right
        if x > 400:
            x = 0  # Reset position once it goes out of screen
        pygame.display.flip()
        pygame.time.delay(30)  # Delay to control speed

    pygame.quit()

if __name__ == "__main__":
    animate_circle()