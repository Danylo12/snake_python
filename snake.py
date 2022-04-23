
class Dir():
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake():
    def __init__(self, x_head, y_head, length, dir):
        self.x_head = x_head
        self.y_head = y_head
        self.length = length
        self.dir = dir
        self.turns = []

    def update(self, key_state):
        print(len(self.turns))
        prev_dir = self.dir
        if key_state["KEY_LEFT"]:
            if self.dir != Dir.RIGHT:
                self.dir = Dir.LEFT
        if key_state["KEY_RIGHT"]:
            if self.dir != Dir.LEFT:
                self.dir = Dir.RIGHT
        if key_state["KEY_UP"]:
            if self.dir != Dir.DOWN:
                self.dir = Dir.UP
        if key_state["KEY_DOWN"]:
            if self.dir != Dir.UP:
                self.dir = Dir.DOWN
        if self.dir != prev_dir:
            self.turns.append((prev_dir, self.x_head, self.y_head))
        if self.dir == Dir.LEFT:
            self.x_head -= 1
        if self.dir == Dir.RIGHT:
            self.x_head += 1
        if self.dir == Dir.UP:
            self.y_head -= 1
        if self.dir == Dir.DOWN:
            self.y_head += 1

    def get_body(self):
        x = self.x_head
        y = self.y_head
        dir = self.dir
        turns = self.turns
        total_length = 1
        while total_length < self.length:
            if dir == Dir.LEFT:
                x += 1
            if dir == Dir.RIGHT:
                x -= 1
            if dir == Dir.UP:
                y += 1
            if dir == Dir.DOWN:
                y -= 1
            if len(turns) != 0:
                last_turn_dir, last_turn_x, last_turn_y = turns[-1]
                if last_turn_x == x and last_turn_y == y:
                    dir = last_turn_dir
                    turns = turns[:-1]
            total_length += 1
            yield x, y
        self.turns = self.turns[len(turns):]








