import asyncio
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from definitions import *

import pygame as pg
pg.init()
pg.display.set_caption(GAME_NAME)
pg.display.set_icon(pg.image.load(asset("petal1.png")))

setmodekwargs = { 'flags': pg.SCALED, }

# emscripten builds do not work with setting a SCALED flag
if sys.platform == 'emscripten':
    del setmodekwargs[ 'flags' ]

game_win = pg.display.set_mode(RES, **setmodekwargs)

from scenes import title
from game_session import game_session
from scenes import credits

async def main(game_win):
    bgm = pg.mixer.music.load(asset("title.ogg"))
    pg.mixer.music.play(-1)

    await title(game_win)
    await game_session(game_win)

    pg.mixer.music.stop()

    await credits(game_win)

if __name__ == '__main__':
   asyncio.run(main(game_win))