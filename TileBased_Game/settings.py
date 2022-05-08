import pygame as pg
import sys
from os import path

pg.init()
# define some colors (R, G, B)
TRANSPARENT = (0, 0, 0, 0) #den fjerde værdi er gennemsigtigheden
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   #Easy Division '/' = 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  #Easy Division '/' = 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_SPEED = 700

#current map
C_MAP = 'Hub.txt'

Dead = False

# combat settings
#Makes a new screen specifically for combat
cscreen = pg.display.set_mode((WIDTH, HEIGHT))

Text = pg.font.SysFont(None, 32) #Laver en textfont som bruges til at vise tekst på skærmen
textH = 500 #Pixel positionen til brug til at placere teksten
textW = 400 #Pixel positionen til brug til at placere teksten

#assigns folders for loading in files
game_folder = path.dirname(__file__)
assets_folder = path.join(game_folder, 'assets')
map_folder = path.join(game_folder, 'Maps')

#assets
PLAYER_ASSET = pg.image.load(path.join(assets_folder, 'player.png')).convert_alpha()
ENEMY_ASSET = pg.image.load(path.join(assets_folder, 'Enemy.png')).convert_alpha()
