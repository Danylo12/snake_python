from controls import Controls
from snake import Snake, Dir
from renderer import Renderer, State
import time


class Game():
    def __init__(self, x_size, y_size, cell_size):
        window_width = cell_size * x_size
        window_height = cell_size * y_size
        self.x_size = x_size
        self.y_size = y_size
        self.board = [
            [
                State.EMPTY
                for y in range(y_size)
            ]
            for x in range(x_size)
        ]
        self.controls = Controls()
        self.snake = Snake(x_size // 2, y_size // 2, 15, Dir.RIGHT)
        self.renderer = Renderer(window_width, window_height)

    def handle_input(self):
        self.controls.handle_input()

    def update(self):
        self.snake.update(self.controls.key_state)
        for x in range(self.x_size):
            for y in range(self.y_size):
                self.board[x][y] = State.EMPTY
        self.board[self.snake.x_head][self.snake.y_head] = State.SNAKE_HEAD
        for x, y in self.snake.get_body():
            self.board[x][y] = State.SNAKE



    def render(self):
        self.renderer.render(self.board)

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.render()
            self.controls.clear_inputs()
            time.sleep(0.2)

