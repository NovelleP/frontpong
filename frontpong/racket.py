import pyglet


class Racket(pyglet.shapes.Rectangle):

    def __init__(self, speed_x, speed_y, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.window = window

    def update(self, keyboard, dt):
        if keyboard.get(pyglet.window.key.UP):
            self.y = min(self.window.height - self.height,
                         self.y + self.speed_y * dt)
        if keyboard.get(pyglet.window.key.DOWN):
            self.y = max(0,
                         self.y - self.speed_y * dt)

    def update_speed_by_factor(self, factor):
        self.speed_x += self.speed_x * factor
        self.speed_y += self.speed_y * factor