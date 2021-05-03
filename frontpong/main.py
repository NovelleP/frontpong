import pyglet
from frontpong import Ball, Racket

keys = {}


if __name__ == '__main__':
    window = pyglet.window.Window()
    racket = Racket(speed_x=0, speed_y=350, window=window, x=15, y=window.height - 100, width=5, height=100, color=(50, 225, 30))
    ball = Ball(speed_x=150, speed_y=150, window=window, racket=racket, x=100, y=150, radius=10, color=(50, 225, 30))
    pyglet.clock.schedule_interval(lambda dt: racket.update(keys, dt), 1 / 120.0)
    pyglet.clock.schedule_interval(ball.update, 1 / 120.0)
    pyglet.clock.schedule_interval(lambda _: ball.update_speed_by_factor(0.2), 2)
    pyglet.clock.schedule_interval(lambda _: racket.update_speed_by_factor(0.1), 2)


    @window.event
    def on_draw():
        window.clear()
        ball.draw()
        racket.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        keys[symbol] = True

    @window.event
    def on_key_release(symbol, modifiers):
        keys[symbol] = False


    pyglet.app.run()
