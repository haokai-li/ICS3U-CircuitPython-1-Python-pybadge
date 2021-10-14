#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about pybadge

import ugame
import stage

import constants


def game_scene():
    # add background
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    # size
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # sprite frame
    ship = stage.Sprite(image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))


    # put background in game
    # set the frame rate
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers
    game.layers = [ship] + [background]
    # render the background
    game.render_block()

    # loop
    while True:
        # get input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic

        # redraw Sprite
        game.render_sprites([ship])
        game.tick() # wait

if __name__ == "__main__":
    game_scene()

