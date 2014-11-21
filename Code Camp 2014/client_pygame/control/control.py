#
# This file is where you will control your player.
# Make changes and add functions as you need.
#

import pygame
from client.base_control import *

class Control(BaseControl):
    """
    This class is where you specify how your player
    behaves in the game.  You can use key presses,
    mouse clicks, and mouse montion to receive input
    from the user.

    You can also add calculations in this code to 
    control the behavior of your player based on the
    state of the game.

    The 4 methods below have specific purposes:
    __init__ is used to create an variables (data members) that
        you need to remember here and in the display class.
    pregame_control is used to get user input before you join 
        a game.  This is most important in deciding what kind 
        of game the user would like to join.
    game_input_control is used to get user input during a running
        game.  This is most important in allowing the user to
        tell your code what they would like to have happen.
    game_control is used to have your program make calculations
        and choose what actions to take, without user input.

    There are several parameters and data members that are
    of interest in some or all of these methods:
    engine is the game engine that contains all of the information
        about the current game.  It also has all of the control
        methods that allows you to send commands to the server
        to control your player.
    keys is the set of all keys that are currently pressed.  This
        allows your program to know what keys are held down, if you
        want to implement behavior that repeats when a key is held
        down.
    newkeys is the set of all keys that were newly pressed since.
        the last time these methods were called.  This allows your
        program to know what keys were just pressed, if you
        want to implement behavior that occurs once, when the key
        is first pressed.
    buttons is the set of all mouse buttons that are currently held
        down.  Much like keys is for the keyboard.
    newbuttons is the set of mouse buttons that were newly pressed
        since the last time these methods were called.  Much like
        newkeys is for the keyboard.
    mouse_position is the current location of the mouse.
    self.width is the width of the display screen in pixels.
    self.height is the height of the display screen in pixels.

    A note on keys and newkeys:
    pygame.K_UP is the symbol for the up arrow on your keyboard.
    If you want to know more keyboard symbols look at this
    site http://www.pygame.org/docs/ref/key.html.

    A note on buttons and newbuttons:
    The values in these sets are numbers 1, 2, 3, etc.,
    depending on the number of buttons you have on your
    mouse.  Usually, 1 is left, 2 is middle (holding down
    the scroll wheel), and 3 is right.

    A note on engine:
    You should look at engine_client/game_engine.py to learn
    more about the information and commands that are available
    from this object.
    """

    def __init__(self, width, height):
        """Create any control variables in this method"""
        
        BaseControl.__init__(self, width, height)
        # used to control display of individual item information
        self.show_info = False
        return

    def pregame_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        """
        This method is called every frame while waiting for the
        user to decide they want to join a game, and what kind
        of game they want to join.

        Somewhere in this method you should make one of these calls:
        self.set_state(CONTROL_STATE_WANT_DUAL)
        self.set_state(CONTROL_STATE_WANT_SINGLE),
        self.set_state(CONTROL_STATE_WANT_TOURNAMENT),
        self.set_state(CONTROL_STATE_WANT_VIEW),
        based on the user input.  Defaults here are for the
        user to press 'd' for dual, 's' for single player game, 't' for tournament.
        """

        if pygame.K_d in newkeys:
            self.set_state(CONTROL_STATE_WANT_DUAL)
        elif pygame.K_s in newkeys:
            self.set_state(CONTROL_STATE_WANT_SINGLE)
        elif pygame.K_t in newkeys:
            self.set_state(CONTROL_STATE_WANT_TOURNAMENT)
        elif pygame.K_v in newkeys:
            self.set_state(CONTROL_STATE_WANT_VIEW)
        return
        
    def game_input_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        """
        This method is called every frame while the game is
        running.  You should put controls in here
        to make changes to the game engine based on the
        user input.
        """
        
        (mouse_x, mouse_y) = mouse_position
        
        if pygame.K_UP in newkeys:
            engine.set_player_direction(270)
            engine.set_missile_direction(270)
        elif pygame.K_DOWN in newkeys:
            engine.set_player_direction(90)
            engine.set_missile_direction(90)
        elif pygame.K_LEFT in newkeys:
            engine.set_player_direction(180)
            engine.set_missile_direction(180)
        elif pygame.K_RIGHT in newkeys:
            engine.set_player_direction(0)
            engine.set_missile_direction(0)

        if pygame.K_1 in newkeys:
            engine.set_player_speed_stop()
        elif pygame.K_2 in newkeys:
            engine.set_player_speed_slow()
            
        if pygame.K_q in newkeys:
            engine.set_missile_range_none()
        elif pygame.K_w in newkeys:
            engine.set_missile_range_short()

        if pygame.K_a in newkeys:
            engine.set_missile_power_none()
        elif pygame.K_s in newkeys:
            engine.set_missile_power_low()
                
        if pygame.K_SPACE in newkeys:
            engine.fire_missile()

        if pygame.K_i in newkeys:
            self.show_info = not self.show_info

        return
        
    def game_control(self, engine):
        """
        This method is called every frame while the game is
        running.  You should put here any calls to the
        game engine you want to do based on your program's
        calculations.  This method is called immediately
        following the game_input_control() method.
        """

        return

