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

    def stop_moving(self):
        self.velocity = 0

    def move(self):
        self.y += self.velocity
        if self.y < 0:
            self.y = 0
        elif self.y > self.maximum_height - self.height:
            self.y = self.maximum_height - self.height


class Ball():
    def __init__(self, x, y, radius, horizontal_moving_speed, vertical_moving_speed, max_width, max_height):
        self.x = x
        self.y = y

        self.radius = radius

        self.horizontal_velocity = 0
        self.horizontal_speed = horizontal_moving_speed
        self.vertical_velocity = 0
        self.vertical_speed = vertical_moving_speed

        self.maximum_width = max_width
        self.maximum_height = max_height

    def stop_moving(self):
        self.horizontal_velocity = 0
        self.vertical_velocity = 0

    def switch_horizontal_velocity(self):
        self.horizontal_speed *= -1

    def switch_vertical_velocity(self):
        self.vertical_speed *= -1

    def move(self):
        self.horizontal_velocity = self.horizontal_speed
        self.vertical_velocity = self.vertical_speed


        #check bouncy stuff
        self.x += self.horizontal_velocity

        if self.vertical_velocity < 0 and self.y < self.vertical_velocity + self.radius:
            self.bounce_vertically()
        elif self.vertical_velocity > 0 and self.y > self.maximum_height - self.radius + self.vertical_velocity:
            self.bounce_vertically()
        else:
            self.y += self.vertical_velocity

    def bounce_horizontally(self):
        pass

    def bounce_vertically(self):
        if self.vertical_velocity < 0:
            self.y = self.vertical_velocity + self.radius - self.y
        elif self.vertical_velocity > 0:
            self.y += self.maximum_height - self.radius - self.y - self.vertical_velocity

        self.switch_vertical_velocity()
