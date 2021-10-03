import pygame as pg
from pygame.constants import SRCALPHA
from definitions import *
from utils import *

from notifications import Notifications

class Memory(pg.Surface):
    def __init__(   self,
                    path,
                    activation,
                    energy_decay,
                    sprite_scale = 1,
                    pos = None,
                    spawn_box = None,
                    release_amount=150,
                    text=['', '', '']):

        s = pg.image.load(path)
        s = pg.transform.scale(s, scale(*s.get_size(), sprite_scale))
        w, h = s.get_size()
        pg.Surface.__init__(self, (w, h), flags=SRCALPHA)
        self.blit(s, (0, 0))
        self.set_alpha(1)

        if pos is None:
            pos = ( random.uniform(0, RES[0] - w), 
                    random.uniform(0, RES[1] - h))
        self.pos = pos

        if spawn_box is None:
            spawn_box = self.hitbox()
            while spawn_box.colliderect(self.hitbox()):
                spawn_box = pg.Rect(
                    random.uniform(0, RES[0]-SPAWNER_SIZE), 
                    random.uniform(0, RES[1]-SPAWNER_SIZE), 
                    SPAWNER_SIZE, SPAWNER_SIZE)
        self.spawn_box = spawn_box

        self.revealed, self.action, self.released = False, False, False

        self.dest = ((RES[0] - w) // 2, (RES[1] - h) // 2)

        self.activation, self.energy, self.energy_decay = activation, 0, energy_decay
        self.release_amount = release_amount

        self.show_exp = True
        self.bar_offset = ((RES[0] - MEMORY_BAR_WIDTH)//2, RES[1] - 40)
        self.bound = pg.Rect(*self.bar_offset, MEMORY_BAR_WIDTH, 10)
        self.fill = pg.Rect(*self.bar_offset, 0, 10)

        self.text = text
        self.notifier = Notifications()
        self.notifier.post(self.text[TEXT_INIT], 10, 10, time = 30)

    def complete(self):
        return self.released and self.notifier.current_msg == ''

    def releasable(self):
        if self.revealed:
            if not self.action:
                if not self.released:
                    return True
        return False

    def on_release(self):
        self.released = True
        self.notifier.post(self.text[TEXT_GOODBYE], *pg.mouse.get_pos())
        return self.release_amount, self.hitbox()

    def can_release(self, p):
        if self.hitbox().collidepoint(p):
            return self.releasable()
        return False

    def hitbox(self):
        return pg.Rect(*self.pos, *self.get_size())

    def update(self, count, dt):
        self.notifier.update(dt)
        self.show_exp = self.energy != 0
        if not self.revealed:
            self.set_alpha(clip(1.5*count, lo=1))
            self.energy = max(0, self.energy + (count - self.energy_decay) * dt)
            self.fill.w = int(MEMORY_BAR_WIDTH * (self.energy/self.activation))
            if self.energy >= self.activation:
                self.revealed, self.action, self.show_exp = True, True, False
                self.set_alpha(255)
        if self.action:
            x, y, dx, dy = *self.pos, *translate(*self.dest, *self.pos)
            dist = norm(dx, dy)
            if dist > dt * MEMORY_MOVE_SPEED:
                move = dt * MEMORY_MOVE_SPEED/dist
                self.pos = (x + move * dx, y + move * dy)
            else:
                self.pos, self.action = self.dest, False
                self.notifier.post(self.text[TEXT_REVEAL], *self.hitbox().topleft, align_bot=True)

    def draw(self, surf):
        if not self.released:
            surf.blit(self, self.pos)

    def UI(self, surf):
        if not self.revealed:
            if self.show_exp:
                pg.draw.rect(surf, WHITE, self.bound, 1)
                pg.draw.rect(surf, WHITE, self.fill)

        self.notifier.draw(surf)
