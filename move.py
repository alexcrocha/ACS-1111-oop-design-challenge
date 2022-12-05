class Move:
    x_edge = 100
    y_edge = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
        if self.x == self.x_edge:
            self.x = 50
        if self.y == self.y_edge:
            self.y = 0
