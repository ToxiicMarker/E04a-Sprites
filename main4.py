#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)

        self.animal_list = arcade.SpriteList()

    def setup(self):
        self.animal_sprite = arcade.Sprite("assets/froggy.png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 100
        self.animal_list.append(self.animal_sprite)     

    def on_draw(self):
        arcade.start_render()
        pass


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()