import pygame
import os

class State():
    EMPTY = 0
    SNAKE = 1
    SNAKE_HEAD = 2
    APPLE = 3

class Renderer():
    def __init__(self, window_width, window_height):
        self.empty_img = pygame.image.load(os.path.join("assets", "empty.png"))
        self.snake_head_img = pygame.image.load(os.path.join('assets', 'snake_head.png'))
        self.snake_body = pygame.image.load(os.path.join('assets', 'snake.png'))
        self.apple_img = pygame.image.load(os.path.join('assets', 'apple.png'))
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.window_width = window_width
        self.window_height = window_height

    def render(self, board):
        x_size = len(board)
        for x in range(x_size):
            x_window = self.window_width / x_size * x
            y_size = len(board[x])
            for y in range(y_size):
                y_window = self.window_height / y_size * y
                state = board[x][y]
                if state == State.EMPTY:
                    self.screen.blit(self.empty_img, (x_window, y_window))
                elif state == State.SNAKE_HEAD:
                    self.screen.blit(self.snake_head_img, (x_window, y_window))
                elif state == State.SNAKE:
                    self.screen.blit(self.snake_body, (x_window, y_window))
                elif state == State.APPLE:
                    self.screen.blit(self.apple_img, (x_window, y_window))


        pygame.display.flip()