import pygame, sys

class Controls():
    def __init__(self):
        self.keymap = {
            "KEY_LEFT": pygame.K_LEFT,
            "KEY_RIGHT": pygame.K_RIGHT,
            "KEY_UP": pygame.K_UP,
            "KEY_DOWN": pygame.K_DOWN,
        }
        self.key_state = {
            key: False for (key, _) in self.keymap.items()
        }

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for (key, val) in self.keymap.items():
                    if event.key == val:
                        self.key_state[key] = True

    def clear_inputs(self):
        for key in self.key_state:
            self.key_state[key] = False




