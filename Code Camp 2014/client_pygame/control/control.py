#
# This file is where you will control your player.
# Make changes and add functions as you need.
#

import pygame
import math
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
        elif pygame.K_3 in newkeys:
            engine.set_player_speed_medium()
        elif pygame.K_4 in newkeys:
            engine.set_player_speed_fast()

        if pygame.K_q in newkeys:
            engine.set_missile_range_none()
        elif pygame.K_w in newkeys:
            engine.set_missile_range_short()
        elif pygame.K_e in newkeys:
            engine.set_missile_range_long()

        if pygame.K_a in newkeys:
            engine.set_missile_power_none()
        elif pygame.K_s in newkeys:
            engine.set_missile_power_low()

        if pygame.K_x in newkeys:
            self.attack_npcs(engine)
        elif pygame.K_z in newkeys:
            self.point_at_character(engine)    
        
        


        if pygame.K_SPACE in newkeys:
            engine.fire_missile()

        self.show_info = True

        return
        
    def game_control(self, engine):
        """
        This method is called every frame while the game is
        running.  You should put here any calls to the
        game engine you want to do based on your program's
        calculations.  This method is called immediately
        following the game_input_control() method.
        """

        opp = engine.get_object(engine.get_opponent_oid())
        pl = engine.get_object(engine.get_player_oid())
        if not pl or not opp:
            return

        # if the opponent's exeperience is higher then the players then chase npc's
        try:
            plex = pl.get_experience()
            oppex = opp.get_experience()

            #if plex < oppex:
            #self.attack_npcs(engine,pl)
            #else:
            #    self.point_at_character(engine,pl,opp)

        except:
            print "error in game control"
            raise
        # if the player's experience is higher chase the opponent

        return

    def attack_npcs(self, engine):
        player = engine.get_object(engine.get_player_oid())
        all = engine.get_objects()
        closest_npc = None
        for obj in all:
            if closest_npc and engine.get_object(obj).is_npc():
                if self.distance_between(engine.get_object(obj).get_x(), engine.get_object(obj).get_y(), player.get_x(), player.get_y()) \
                < self.distance_between(closest_npc.get_x(), closest_npc.get_y(), player.get_x(), player.get_y()):
                    closest_npc = engine.get_object(obj)
            elif engine.get_object(obj).is_npc():
                closest_npc = engine.get_object(obj)
        
        #self.opponent_closeby(engine, player)
        #self.wall_closeby(engine, player)
        

        self.point_at_character(engine, closest_npc)

    def distance_between(self,x1,y1,x2,y2):
        d = ((x2-x1)**2 + (y2-y1)**2)**(1./2)
        return d

    def get_centerpoint(self, character):
        px = character.get_x() + character.get_w()/2.
        py = character.get_y() + character.get_h()/2.
        return px,py


    def opponent_closeby(self, engine, player):
        opponent = engine.get_object(engine.get_opponent_oid())
        oppcenter = self.get_centerpoint(opponent)
        playercenter = self.get_centerpoint(player)
        distance = self.distance_between(oppcenter[0], oppcenter[1], playercenter[0], playercenter[1])

        if distance < 45:
            return True
        return False

    def character_closeby(self, engine, character, limit):
        player = engine.get_object(engine.get_player_oid())
        charcenter = self.get_centerpoint(character)
        playercenter = self.get_centerpoint(player)
        distance = self.distance_between(charcenter[0], charcenter[1], playercenter[0], playercenter[1])

        if distance < limit:
            return True
        return False

    def wall_closeby(self, engine, player):
        all = engine.get_objects()
        for c in all:
            character = engine.get_object(c)
            charcenter = self.get_centerpoint(character)
            playercenter = self.get_centerpoint(player)
            distance = self.distance_between(charcenter[0], charcenter[1], playercenter[0], playercenter[1])

            if distance < 45:
                return True
        return False

    def point_at_character(self, engine, character=None):
            """
            find the character and track it down and shoot at it.
            """
            #point missile towards opponent
            if not character:
                character = engine.get_object(engine.get_opponent_oid())
            player = engine.get_object(engine.get_player_oid())
                        
            try:
                px = player.get_x() + player.get_w()/2.
                py = player.get_y() + player.get_h()/2.
                dx = character.get_x() - px
                dy = character.get_y() - py
                theta = math.atan2(dy, dx)
                degrees = math.degrees(theta)
                engine.set_missile_direction(degrees)
                engine.set_player_direction(degrees)

                if self.character_closeby(engine,character,player.get_missile_range()-20):
                    engine.set_player_speed_stop()
                    engine.fire_missile()
                else:
                    engine.set_player_speed_slow()
                

            except:
                print "error pointing at character"
                raise

    def run_from_character(self, engine, player, character):
            """
            find the character and track it down and shoot at it.
            """
            #point missile towards opponent
                        
            try:
                px = player.get_x() + player.get_w()/2.
                py = player.get_y() + player.get_h()/2.
                dx = character.get_x() - px
                dy = character.get_y() - py
                theta = math.atan2(dy, dx)
                degrees = math.degrees(theta)
                
                engine.set_player_direction(degrees+180)
                engine.set_player_speed_slow()

            except:
                print "error pointing at character"









