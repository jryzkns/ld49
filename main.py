import os

from petal import Petal
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time

from definitions import *

import pygame as pg
pg.init()

from wind import Wind
from particles import Particles

wind = Wind(*RES)
petals = Particles(*RES)

game_win = pg.display.set_mode(RES, pg.SRCALPHA)

running, dt = True, 0
prev = time.time()

from memory import memory_collection
memories = memory_collection()
memory = next(memories)

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LCTRL:
                pg.event.set_grab(not pg.event.get_grab())
        elif event.type == pg.MOUSEBUTTONDOWN:
            wind.register_md()
            if len(petals) == 0 and memory.can_release(event.pos):
                wind.reset_field()
                wind.perturb()
                petals.emit_box(Petal, memory.release_amount, memory.hitbox())
                memory.released = True

    game_win.fill(BLACK)
    memory.draw(game_win)
    petals.draw(game_win)

    wind.draw(game_win)

    pg.display.flip()

    now = time.time()
    dt = min(now - prev, 1/MAX_FPS)

    wind.update(dt)
    petals.update(wind, dt)

    in_count = 0
    for petal in petals:
        in_count += memory.hitbox().colliderect(petal.hitbox())
    
    reveal_state = memory.revealed
    memory.update(in_count, dt)
    if memory.revealed != reveal_state:
        wind.streakable = False
    if not memory.revealed:
        petals.emit_box(Petal, 1, memory.spawn_box)
    if memory.released and len(petals) == 0:
        memory = next(memories, None)
        wind.streakable = True
        if memory is None:
            running = False

    pg.display.set_caption(
        f"petals:{len(petals)} fps: {round(1 / (now - prev), 2) if dt !=0 else 0}")

    prev = now
