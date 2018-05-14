import pygame
import pygameMenu
from pygameMenu.locals import *
import time
import sys

# Initialize pygame
check_errors = pygame.init()

# Second value of tuple is the num of errors
if check_errors[1] > 0:
    print('(!) Had {} initialing errors, exiting...'.format(check_errors[1]))
    sys.exit(-1)
else:
    print('(+) PyGame initialized successfully!')
# Create window
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ultra Snake')

# Define important variables
white = pygame.Color(255, 255, 255)

# Snake position
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

direction = 'RIGHT'
change_to = direction

score = 0

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
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'

    # Direction validation
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Change position
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10

    
    


    # Update display
    main_menu.mainloop(events)
    pygame.display.flip()
    fps_controller.tick(24)