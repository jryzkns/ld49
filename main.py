import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame as pg
pg.init()

if __name__ == '__main__':
    from title import title
    title()
    from game_session import game_session
    game_session()
    from credits import credits
    credits()