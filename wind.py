import pygame as pg
from definitions import *
from utils import *

class Wind:
    def __init__(self, world_w, world_h):
        self.w, self.h = world_w, world_h
        self.reset()

        self.mx, self.my = 0, 0
        self.update_timer = 0

    def reset(self):
        self.blank_field()
        self.perturb()

    def blank_field(self):
        self.wind_map = [ [ (0,0)
                    for _ in range(3 + (self.h // WIND_RESOLUTION)) ]
                    for _ in range(3 + (self.w // WIND_RESOLUTION)) ]

    def perturb(self, spacing=1):
        for i in range(0, 3 + (self.h // WIND_RESOLUTION), spacing):
            for j in range(0, 3 + (self.w // WIND_RESOLUTION), spacing):
                self.wind_map[j][i] = \
                    clip_norm(*add(*self.wind_map[j][i], *random_direction()), 2)

    def register_md(self):
        self.mx, self.my = pg.mouse.get_pos()

    def update(self, dt):
        self.update_timer += dt
        if self.update_timer > WIND_CHANGE_TIME:
            self.update_timer -= WIND_CHANGE_TIME
            self.perturb(3)
        if any(pg.mouse.get_pressed()):
            mx, my = pg.mouse.get_pos()
            head_x, head_y = 1 + mx // WIND_RESOLUTION, 1 + my // WIND_RESOLUTION
            v = translate(mx, my, self.mx, self.my)
            self.wind_map[head_x    ][head_y    ] = clip_norm(*add(*self.wind_map[head_x    ][head_y    ], *v))
            self.wind_map[head_x + 1][head_y    ] = clip_norm(*add(*self.wind_map[head_x + 1][head_y    ], *v), 3)
            self.wind_map[head_x    ][head_y + 1] = clip_norm(*add(*self.wind_map[head_x    ][head_y + 1], *v), 3)
            self.wind_map[head_x + 1][head_y + 1] = clip_norm(*add(*self.wind_map[head_x + 1][head_y + 1], *v), 0.5)
            self.mx, self.my = mx, my

    def wind_at(self, x, y):
        head_x, tail_x = divmod(x, WIND_RESOLUTION)
        head_y, tail_y = divmod(y, WIND_RESOLUTION)
        head_x += 1; head_y += 1
        Q2, Q1 = self.wind_map[head_x    ][head_y    ], self.wind_map[head_x + 1][head_y    ]
        Q3, Q4 = self.wind_map[head_x    ][head_y + 1], self.wind_map[head_x + 1][head_y + 1]
        top = translate(*Q2, *scale(*translate(*Q1, *Q2), tail_x / WIND_RESOLUTION))
        bot = translate(*Q3, *scale(*translate(*Q4, *Q3), tail_x / WIND_RESOLUTION))
        return translate(*top, *scale(*translate(*bot, *top), tail_y / WIND_RESOLUTION))
