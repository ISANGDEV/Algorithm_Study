class Hero:
    def __init__(self, coordinates, direction):
        self.coordinates = coordinates
        self.direction = direction

    def peek(self):
        self.direction -= 1
        if self.direction == 0:
            