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
        self.animal_sprite.center_x = 700
        self.animal_sprite.center_y = 100
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/pepe.png", 1)
        self.animal_sprite.center_x = 50
        self.animal_sprite.center_y = 45
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/Mario.png", 0.25)
        self.animal_sprite.center_x = 700
        self.animal_sprite.center_y = 500
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/hyper.png", 0.5)
        self.animal_sprite.center_x = 100
        self.animal_sprite.center_y = 500
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/OG.png", 0.5)
        self.animal_sprite.center_x = 400
        self.animal_sprite.center_y = 500
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/Rubick.png", 0.25)
        self.animal_sprite.center_x = 400
        self.animal_sprite.center_y = 480
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/bowl.png", 0.5)
        self.animal_sprite.center_x = 215
        self.animal_sprite.center_y = 100
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/gold.png", 0.1)
        self.animal_sprite.center_x = 550
        self.animal_sprite.center_y = 25
        self.animal_list.append(self.animal_sprite)  

        self.animal_sprite = arcade.Sprite("assets/Rodgers.png", 0.5)
        self.animal_sprite.center_x = 400
        self.animal_sprite.center_y = 100
        self.animal_list.append(self.animal_sprite) 
        
        self.animal_sprite = arcade.Sprite("assets/sun.png", 0.08)
        self.animal_sprite.center_x = 397
        self.animal_sprite.center_y = 175
        self.animal_list.append(self.animal_sprite)  
        
        self.animal_sprite = arcade.Sprite("assets/blunt.png", 0.08)
        self.animal_sprite.center_x = 415
        self.animal_sprite.center_y = 151
        self.animal_list.append(self.animal_sprite) 

        self.animal_sprite = arcade.Sprite("assets/like.png", 0.05)
        self.animal_sprite.center_x = 400
        self.animal_sprite.center_y = 300
        self.animal_list.append(self.animal_sprite)  











    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()