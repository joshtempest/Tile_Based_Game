# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 4
# Scrolling Map/Camera
# Video link: https://youtu.be/3zV2ewk-IGU
import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from combat import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'E':
                    Enemy(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    #responsible for creating an easy way to load from folders in the gamefolder (C:users/oliver/"gamefolder")
    def load_data(self):
        game_folder = path.dirname(__file__)
        assets_folder = path.join(game_folder, 'assets')
        map_folder = path.join(game_folder, 'Maps')
        self.map = Map(path.join(map_folder, C_MAP))

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    self.quit()

# create the game object
g = Game()
while True:
    g.new()
    g.run()
