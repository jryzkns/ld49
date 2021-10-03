from definitions import *
import pygame as pg
import sys
import time

from wind import Wind
from petal import Petal
from particles import Particles
from memory_collection import memory_collection

def game_session():

    wind = Wind(*RES)
    petals = Particles(*RES)

    game_win = pg.display.set_mode(RES, pg.SRCALPHA)

    running, dt = True, 0
    prev = time.time()

    memories = memory_collection()
    memory = next(memories)

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                elif event.key == pg.K_LCTRL:
                    pg.event.set_grab(not pg.event.get_grab())
            elif event.type == pg.MOUSEBUTTONDOWN:
                wind.register_md()
                if len(petals) == 0 and memory.can_release(event.pos):
                    petals.emit_box(Petal, *memory.on_release())
                    wind.reset()

        game_win.fill(BLACK)
        
        memory.draw(game_win)
        petals.draw(game_win)

        wind.draw(game_win)
        memory.UI(game_win)

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
        if memory.complete() and len(petals) == 0:
            memory = next(memories, None)
            wind.streakable = True
            if memory is None:
                running = False

        pg.display.set_caption(
            f"petals:{len(petals)} fps: {round(1 / (now - prev), 2) if dt !=0 else 0}")

        prev = now
