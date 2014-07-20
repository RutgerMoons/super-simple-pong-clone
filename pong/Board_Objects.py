__author__ = 'rutger'

class Paddle():
    def __init__(self, x, y, width, height, moving_speed, max_height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.velocity = 0
        self.speed = moving_speed

        self.maximum_height = max_height

    def up(self):
        self.velocity = - self.speed


    def down(self):
        self.velocity = self.speed


    def move(self):
        self.y += self.velocity
        if self.y < 0:
            self.y = 0
        elif self.y > self.maximum_height - self.height:
            self.y = self.maximum_height - self.height