from definitions import *
import pygame as pg

import sys

def title():
    running = True
    game_win = pg.display.set_mode(RES, pg.SRCALPHA)
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                running = False
        
        game_win.fill(BLACK)