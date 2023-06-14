import pygame
import sys
from title_page import title_page

def learn():
    pygame.init()
    white = (255, 255, 255)
    window_width = 800
    window_height = 600
    black = (0, 0, 0)
    font = pygame.font.SysFont("Comic Sans", 30)
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Learn Page")
    clock = pygame.time.Clock()

    background_image = pygame.image.load("images_/waste_image.jpg")
    background_image = pygame.transform.scale(background_image, (window_width - 200, window_height - 100))
    next_button = pygame.image.load("images_/next_button.png")
    next_button = pygame.transform.scale(next_button, (50, 50))
    go_back_button = pygame.image.load("images_/go_back_button.png")
    go_back_button = pygame.transform.scale(go_back_button, (50, 50))
    center_image = pygame.image.load("images_/center.png")
    center_image = pygame.transform.scale(center_image, (window_width - 100, window_height - 200))


    next_button_rect = next_button.get_rect(bottomright=(window_width - 10, window_height - 10))
    go_back_button_rect = go_back_button.get_rect(bottomleft=(10, window_height - 10))

    current_page = 1

    window.fill(white)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button_rect.collidepoint(event.pos):
                    if current_page == 1:
                        current_page = 2
                elif go_back_button_rect.collidepoint(event.pos):
                    if current_page == 1:
                        title_page(window)
                        running = False
                    if current_page == 2:
                        current_page = 1
                    

                
                    

        window.blit(background_image, (0, 0))

        if current_page == 1:
            window.fill(white)
            window.blit(next_button, next_button_rect)
            window.blit(go_back_button, go_back_button_rect)
            window.blit(background_image, (0, 0))
        elif current_page == 2:
            window.fill(white)
            learn_text = font.render("Learn", True, black)
            window.blit(center_image, (100, 100))
            window.blit(learn_text, (100, 100))
            window.blit(go_back_button, go_back_button_rect)
            # Display the title and text on the page
            # Add your code here to display the title and text

        pygame.display.flip()
        clock.tick(60)

