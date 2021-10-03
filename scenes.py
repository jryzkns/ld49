from definitions import *
import pygame as pg

import sys
import time

from wind import Wind
from petal import Petal
from particles import Particles

TEXT_DISP_X = 15
TEXT_LINE_PAD = 10

def get_text(fn):
    with open(fn, "r") as f__:
        text = f__.read().split('\n')
    return text

def render_text(TEXT, start_h = None, color = WHITE, size = 24):
    scene_font = GET_SIZED_FONT(size)
    line_h = scene_font.render("", True, WHITE).get_rect().h
    ttl_h = line_h + (len(TEXT) - 1) * (size + TEXT_LINE_PAD)
    if start_h is None:
        start_h = (RES[1] - ttl_h) >> 1
    text_lines = []
    for i, line in enumerate(TEXT):
        rendered_line = scene_font.render(line, True, color)
        textRect = rendered_line.get_rect()
        textRect.center = ( TEXT_DISP_X + textRect.w // 2, 
            start_h + i * (size + TEXT_LINE_PAD))
        text_lines += [(rendered_line, textRect)]
    return text_lines

def title(game_win):

    wind = Wind(*RES)
    petals = Particles(*RES)
    title = render_text(["The Wind Rises"], start_h=25, size=36)[0]
    prompt = render_text(["BY JACK `JRYZKNS` ZHOU", "CLICK ANYWHERE TO CONTINUE"], start_h = 75)

    running, dt = True, 0
    prev = time.time()

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                running = False
        
        game_win.fill(BLACK)

        petals.draw(game_win)

        game_win.blit(*title)
        for line in prompt:
            game_win.blit(*line)

        pg.display.flip()

        now = time.time()
        dt = min(now - prev, 1/MAX_FPS)

        petals.emit_box(Petal, 1, pg.Rect(0, RES[1], RES[0], -10), yv=-100)
        wind.update(dt)
        petals.update(wind, dt)

        prev = now

def credits(game_win):

    wind = Wind(*RES)
    petals = Particles(*RES)
    text_lines = render_text(get_text(asset("credits.txt")))

    bgm = pg.mixer.music.load(asset("credits.ogg"))
    pg.mixer.music.play()

    running, dt = True, 0
    prev = time.time()

    pg.event.set_grab(False)
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        game_win.fill(BLACK)

        petals.draw(game_win)

        for line_info in text_lines:
            game_win.blit(*line_info)

        pg.display.flip()

        now = time.time()
        dt = min(now - prev, 1/MAX_FPS)

        petals.emit_box(Petal, 1, pg.Rect(RES[0], 0, -10, RES[1]), xv=-100)
        wind.update(dt)
        petals.update(wind, dt)

        prev = now
