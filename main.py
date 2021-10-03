import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from definitions import RES

import pygame as pg
pg.init()

if __name__ == '__main__':
    
    game_win = pg.display.set_mode(RES, pg.SRCALPHA)

    from scenes import title
    title(game_win)
    from game_session import game_session
    game_session(game_win)
    from scenes import credits
    credits(game_win)
