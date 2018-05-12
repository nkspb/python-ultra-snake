import pygame
import pygameMenu
from pygameMenu.locals import *
import time
import sys

# Initialize pygame
pygame.init()

# Create window
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ultra Snake')

# Define important variables
white = pygame.Color(255, 255, 255)
# Game window size
W_SIZE = 640
H_SIZE = 480

def new_game():
    pass

def settings_menu():
    pass

# About menu
about_menu = pygameMenu.TextMenu(surface,
                                dopause=False,
                                font=pygameMenu.fonts.FONT_NEVIS,
                                font_size_title=30,
                                font_title=pygameMenu.fonts.FONT_8BIT,
                                menu_color_title=(0, 0, 100),
                                onclose=PYGAME_MENU_DISABLE_CLOSE,  # Disable menu close (ESC button)
                                text_fontsize=20,
                                title='About',
                                window_height=H_SIZE,
                                window_width=W_SIZE
                                )

about_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
about_menu.add_line('Ultra Snake 0.1a')
about_menu.add_line('by Nikolay Komolov')

def mainmenu_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    surface.fill((0, 0, 0))

# Define fps controller to limit fps
fps_controller = pygame.time.Clock()

main_menu = pygameMenu.Menu(surface,
                       bgfun=mainmenu_background,
                       enabled=True,
                       font=pygameMenu.fonts.FONT_NEVIS,
                       menu_alpha=90,
                       onclose=PYGAME_MENU_CLOSE,
                       title='Main Menu',
                       title_offsety=5,
                       window_height=480,
                       window_width=640
                       )

main_menu.add_option('New Game', new_game)
main_menu.add_option('Settings', settings_menu)
main_menu.add_option('About', about_menu)

# Main game loop
while True:
    surface.fill(white)
    # Listen for events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Create an event
                # pygame.event.post(pygame.event.Event(pygame.QUIT))
                main_menu.enable()

    # Update display
    main_menu.mainloop(events)
    pygame.display.flip()
    fps_controller.tick(24)