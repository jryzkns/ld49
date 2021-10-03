import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from definitions import *

import pygame as pg
pg.init()
pg.display.set_caption(GAME_NAME)
pg.display.set_icon(pg.image.load(asset("petal1.png")))

if __name__ == '__main__':
    
    game_win = pg.display.set_mode(RES, flags=pg.SCALED)

    bgm = pg.mixer.music.load(asset("title.ogg"))
    pg.mixer.music.play(-1)

    from scenes import title
    title(game_win)
    from game_session import game_session
    game_session(game_win)

    pg.mixer.music.stop()

    from scenes import credits
    credits(game_win)
