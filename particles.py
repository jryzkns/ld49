import random
import pygame as pg
from definitions import *

class Particles(list):
    def __init__(self, w, h):
        list.__init__(self)
        self.window_bound = pg.Rect(0, 0, w, h)

    def update(self, wind, dt):
        if len(self) > MAX_PETALS:
            for _ in range(len(self) - MAX_PETALS):
                self.pop()

        for idx, particle in enumerate(self):
            particle_hitbox = particle.hitbox()
            particle.update(wind.wind_at(*particle_hitbox.center), dt)
            if not self.window_bound.colliderect(particle_hitbox) \
                or particle.lifetime <= 0:
                self.pop(idx)

    def emit_box(self, type, n, rect, **kwargs):
        for _ in range(n):
            self.append( type(
                random.uniform(rect.left, rect.right),
                random.uniform(rect.top, rect.bottom),
                **kwargs))

    def emit_point(self, type, n, x, y, **kwargs):
        for _ in range(n):
            self.append(type(x, y, **kwargs))

    def draw(self, surf):
        for particle in self:
            particle.draw(surf)
