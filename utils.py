import pygame as pg
import random
import math

def lighten(surf, lighteness = 30):
    light_mask = pg.Surface(surf.get_size(), flags=pg.SRCALPHA)
    light_mask.fill((lighteness, lighteness, lighteness, 0))
    surf.blit(light_mask, (0, 0), special_flags = pg.BLEND_RGBA_SUB)

def scale(x, y, scale):
    return int(x * scale), int(y * scale)

def translate(x, y, dx, dy):
    return x - dx, y - dy

def random_direction(scale = 1):
    theta = random.uniform(0, 2 * math.pi)
    return scale * math.sin(theta), scale * math.cos(theta)

def flip_theta_sign(theta):
    return theta if theta > 0 else 2 * math.pi - theta

def norm(x, y):
    return math.sqrt(x*x + y*y)

def clip(x, lo = 0, hi = 255):
    if lo < x < hi: return x
    return lo if x < lo else hi

def clip_norm(x, y, max_norm=5):
    vn, rescale = norm(x, y), 1
    if vn == 0:
        return 0, 0
    if vn > max_norm:
        rescale = max_norm/vn
    return x*rescale, y*rescale

def normalize(x, y):
    vn = norm(x, y)
    if vn == 0:
        return 0, 0
    return x/vn, y/vn