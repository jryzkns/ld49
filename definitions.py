import sys
from os.path import abspath, join
HERE = abspath(".")
try:
    BASE_PATH = sys._MEIPASS
except Exception:
    BASE_PATH = abspath(".")

asset = lambda fn : join(BASE_PATH, 'assets', fn)

RES = (1200, 600)
MAX_FPS = 60

TRANSPARENT = (0, 0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

GRAVITY = 0.5


SPAWNER_SIZE = 100

MEMORY_BAR_WIDTH = 600

WIND_RESOLUTION = 50
STREAK_DECAY_TIME = 0.1
WIND_CHANGE_TIME = 3

PETAL_MAX_XVEL = 300
PETAL_MAX_YVEL = 300
