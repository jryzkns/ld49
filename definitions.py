import sys
from os.path import abspath, join
HERE = abspath(".")
try:
    BASE_PATH = sys._MEIPASS
except Exception:
    BASE_PATH = abspath(".")

asset = lambda fn : join(BASE_PATH, 'assets', fn)

RES = (900, 600)
MAX_FPS = 60

TRANSPARENT = (0, 0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GRAVITY = 0.5

SPAWNER_SIZE = 50

MEMORY_MOVE_SPEED = 100
MEMORY_BAR_WIDTH = 600

WIND_RESOLUTION = 75
WIND_CHANGE_TIME = 10

MAX_PETALS = 200
PETAL_MAX_XVEL = 300
PETAL_MAX_YVEL = 300

MSG_EXPIRY = 10
from pygame.font import Font
GET_SIZED_FONT = lambda pts : Font(asset("orange-kid.regular.ttf"), pts)

TEXT_INIT = 0
TEXT_REVEAL = 1
TEXT_GOODBYE = 2

GAME_NAME = "The Wind Rises"
