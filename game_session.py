import asyncio
from definitions import *
import pygame as pg
import sys
import time

from wind import Wind
from petal import Petal
from particles import Particles
from memory_collection import memory_collection

async def game_session(game_win):

    wind = Wind(*RES)
    petals = Particles(*RES)

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
        memory.UI(game_win)
        pg.display.flip()

        now = time.time()
        dt = min(now - prev, 1/MAX_FPS)

        wind.update(dt)
        petals.update(wind, dt)

        in_count, memory_hb = 0, memory.hitbox()
        for petal in petals:
            in_count += memory_hb.colliderect(petal.hitbox())
                
        memory.update(in_count, dt)
        if not memory.revealed:
            petals.emit_box(Petal, 1, memory.spawn_box)
        if memory.complete() and len(petals) == 0:
            memory = next(memories, None)
            if memory is None:
                running = False

        prev = now
        await asyncio.sleep(0)
