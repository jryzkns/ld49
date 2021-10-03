import pygame as pg
from pygame.constants import SRCALPHA
from definitions import *
from utils import *

def memory_collection():
    memory_data = [
        (asset('queen_goose.png'), 10, 70),
        (asset('seal.png'), 10, 70),
    ]
    for data in memory_data:
        yield Memory(*data)

class Memory(pg.Surface):
    def __init__(self, path, activation, energy_decay, pos = None, spawn_box = None, release_amount=150):
        sprite = pg.image.load(path)
        pg.Surface.__init__(self, sprite.get_size(), flags=SRCALPHA)
        self.blit(sprite, (0, 0))
        self.set_alpha(1)

        if pos is None:
            pos = ( random.uniform(0, RES[0]-sprite.get_width()), 
                    random.uniform(0, RES[1]-sprite.get_height()))
        self.pos = pos

        if spawn_box is None:
            spawn_box = self.hitbox()
            while spawn_box.colliderect(self.hitbox()):
                spawn_box = pg.Rect(
                    random.uniform(0, RES[0]-SPAWNER_SIZE), 
                    random.uniform(0, RES[1]-SPAWNER_SIZE), 
                    SPAWNER_SIZE, SPAWNER_SIZE)
        self.spawn_box = spawn_box

        self.release_amount = release_amount

        self.revealed, self.action, self.released = False, False, False

        self.movespeed = 150
        self.dest_x = (RES[0] - sprite.get_width()) // 2
        self.dest_y = (RES[1] - sprite.get_height()) // 2
        self.dest = (self.dest_x, self.dest_y)

        self.activation, self.energy, self.energy_decay = activation, 0, energy_decay

        self.show_exp = True
        self.bar_offset = ((RES[0] - MEMORY_BAR_WIDTH)//2, RES[1] - 40)
        self.bound = pg.Rect(*self.bar_offset, MEMORY_BAR_WIDTH, 10)
        self.fill = pg.Rect(*self.bar_offset, 0, 10)

    def releasable(self):
        if self.revealed:
            if not self.action:
                if not self.released:
                    return True
        return False

    def can_release(self, p):
        if self.hitbox().collidepoint(p):
            return self.releasable()
        return False

    def hitbox(self):
        return pg.Rect(*self.pos, *self.get_size())

    def update(self, count, dt):
        if self.releasable():
            pass # TODO: some UI indication
        if not self.revealed:
            self.set_alpha(clip(2 * count, lo=1))
            self.energy = max(0, self.energy + (count - self.energy_decay) * dt)
            self.fill.w = int(MEMORY_BAR_WIDTH * (self.energy/self.activation))
            if self.energy >= self.activation:
                self.revealed, self.action, self.show_exp = True, True, False
                self.set_alpha(255)
        if self.action:
            x, y, dx, dy = *self.pos, *translate(*self.dest, *self.pos)
            dist = norm(dx, dy)
            if dist > dt * self.movespeed:
                move = dt * self.movespeed/dist
                self.pos = (x + move * dx, y + move * dy)
            else:
                self.pos, self.action = self.dest, False

    def draw(self, surf):
        if not self.released:
            surf.blit(self, self.pos)
            if self.show_exp:
                pg.draw.rect(surf, WHITE, self.bound, 1)
                pg.draw.rect(surf, WHITE, self.fill)
