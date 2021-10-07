#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about pybadge

import ugame
import stage


def game_scene():
    # add backgrond
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    # put background in game
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()
    # loop
    while True:
        pass

if __name__ == "__main__":
    game_scene()
