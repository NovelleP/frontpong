import pyglet


class Ball(pyglet.shapes.Circle):

    def __init__(self, speed_x, speed_y, window, racket, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.window = window
        self.racket = racket

    def update(self, dt):
        if self.__are_collisioned_with(self.racket):
            self.speed_x = -self.speed_x
        else:
            if self.__is_game_over():
                self.speed_x = 0
                self.speed_y = 0
            if self.__is_x_right_limit():
                self.speed_x = -self.speed_x
            if self.__is_y_limit():
                self.speed_y = -self.speed_y
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

    def update_speed_by_factor(self, factor):
        self.speed_x += self.speed_x * factor
        self.speed_y += self.speed_y * factor

    def __is_game_over(self):
        return self.__is_x_left_limit()

    def __are_collisioned_with(self, object):
        return (object.y <= self.y <= object.y + object.height) \
               and (self.x <= object.x + object.width)

    def __is_x_right_limit(self):
        return (self.x + self.radius) >= self.window.width

    def __is_x_left_limit(self):
        return self.x - self.radius <= 0

    def __is_y_limit(self):
        return not (0 <= (self.y - self.radius) <= (self.window.height - self.radius * 2))

