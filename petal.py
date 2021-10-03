import pygame as pg
from definitions import *
import random

from utils import *

class Petal:
    def __init__(self, x, y, xv = None, yv = None):

        self.sprite = pg.image.load(asset(f'petal{random.choice([1, 2, 3])}.png'))
        self.sprite_aura = pg.transform.scale(
            self.sprite, scale(*self.sprite.get_size(), 1.5))
        lighten(self.sprite_aura, 150)

        self.x, self.y = x, y

        if xv is None and yv is None:
            xcos, ysin = random_direction()
            xv = random.uniform(20, 100) * xcos
            yv = random.uniform(20, 60) * ysin
        elif yv is None:
            yv = random.uniform(-60, 60)
        elif xv is None:
            xv = random.uniform(-100, 100)
        self.xvel, self.yvel = xv, yv
        
        self.lifetime = random.uniform(5, 7)

    def hitbox(self):
        return pg.Rect( *translate(
                            self.x, self.y, 
                            *scale(*self.sprite.get_size(), 0.5)),
                        *self.sprite.get_size())

    def update(self, wind_snapshot, dt):

        self.lifetime -= dt

        wind_xaccel, wind_yaccel = wind_snapshot
        # self.xvel += wind_xaccel
        # self.yvel += wind_yaccel + GRAVITY

        self.xvel = min(PETAL_MAX_XVEL, self.xvel + wind_xaccel)
        self.yvel = min(PETAL_MAX_YVEL, self.yvel + wind_yaccel + GRAVITY)

        self.x += self.xvel * dt
        self.y += self.yvel * dt

    def draw(self, surf):
        surf.blit(  self.sprite, 
                    translate(
                        self.x, self.y, 
                        *scale(*self.sprite.get_size(), 0.5)))
        surf.blit(  self.sprite_aura, 
                    translate(
                        self.x, self.y, 
                        *scale(*self.sprite_aura.get_size(), 0.5)), 
                    special_flags = pg.BLEND_RGB_ADD)
