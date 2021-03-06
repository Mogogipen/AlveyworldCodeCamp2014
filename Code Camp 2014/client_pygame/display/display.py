#
# This file is where you make the display for your game
# Make changes and add functions as you need.
#

import pygame
from config import *
from common.event import *
from client.base_display import BaseDisplay

class Display(BaseDisplay):
    """
    This class controls all of the drawing of the screen
    for your game.  The process of drawing a screen is
    to first draw the background, and then draw everything
    that goes on top of it.  If two items are drawn in the
    same place, then the last item drawn will be the one
    that is visible.

    The screen is a 2 dimensional grid of pixels, with the
    origin (0,0) located at the top-left of the screen, and
    x values increase to the right and y values increase as
    you go down.  The y values are opposite of what you learned
    in your math classes.

    Documentation on drawing in pygame is available here:
    http://www.pygame.org/docs/ref/draw.html

    The methods in this class are:
    __init__ creates data members (variables) that are used
        in the rest of the methods of this class.  This is
        useful for defining colors and sizes, loading image
        or sound files, creating fonts, etc.  Basically,
        any one time setup.

    paint_game controls the drawing of the screen while the
        game is in session.  This is responsible for making
        sure that any information, whether graphics, text, or
        images are drawn to the screen.

    paint_waiting_for_game controls the drawing of the screen
        after you have requested to join a game, but before
        the game actually begins.
    
    paint_game_over controls the drawing of the screen after
        the game has been won, but before the game goes away.
        This is a short (3-5 second) period.

    process_event controls handling events that occur in the
        game, that aren't represented by objects in the game
        engine.  This includes things like collisions,
        objects dying, etc.  This would be a great place to
        play an audio file when missiles hit objects.

    paint_pregame controls the drawing of the screen before
        you have requested to join a game.  This would usually
        allow the user to know the options available for joining
        games.

    Method parameters and data members of interest in these methods:
    self.width is the width of the screen in pixels.
    self.height is the height of the screen in pixels.
    self.* many data members are created in __init__ to set up
        values for drawing, such as colors, text size, etc.
    surface is the screen surface to draw to.
    control is the control object that is used to
        control the game using user input.  It may
        have data in it that influences the display.
    engine contains all of the game information about the current
        game.  This includes all of the information about all of
        the objects in the game.  This is where you find all
        of the information to display.
    event is used in process_event to communicate what
        interesting thing occurred.
    
    Note on text display:  There are 3 methods to assist
    in the display of text.  They are inherited from the
    BaseDisplay class.  See client/base_display.py.
    
    """

    def __init__(self, width, height):
        """
        Configure display-wide settings and one-time
        setup work here.
        """
        BaseDisplay.__init__(self, width, height)

        # There are other fonts available, but they are not
        # the same on every computer.  You can read more about
        # fonts at http://www.pygame.org/docs/ref/font.html
        self.font_size = 15
        self.font = pygame.font.SysFont("Courier New",self.font_size)

        # Colors are specified as a triple of integers from 0 to 255.
        # The values are how much red, green, and blue to use in the color.
        # Check out http://www.colorpicker.com/ if you want to try out
        # colors and find their RGB values.
        self.player_color     = (255, 0, 0)
        self.opponent_color   = (0, 0, 0)
        self.missile_color    = (0, 0, 255)
        self.npc_color        = (255, 255, 0)
        self.wall_color       = (50, 50, 50)
        self.text_color       = (225, 225, 225)
        self.background_color = (255, 255, 255)
        self.player_image     = [pygame.image.load("display/player1.png"), pygame.image.load("display/player2.png"), pygame.image.load("display/player3.png"), pygame.image.load("display/player4.png"), pygame.image.load("display/player.png")]
        self.opponent_image   = [pygame.image.load("display/opponent1.png"), pygame.image.load("display/opponent2.png"), pygame.image.load("display/opponent3.png"), pygame.image.load("display/opponent4.png"), pygame.image.load("display/opponent.png")]
        self.missile_image    = [pygame.image.load("display/missile1.png"), pygame.image.load("display/missile2.png")]
        self.npc_images       = [pygame.image.load("display/npcd1.png"), pygame.image.load("display/npcd2.png"), pygame.image.load("display/npcd3.png"), pygame.image.load("display/npc.png")]
        self.wall_image       = pygame.image.load("display/wall.png")
        self.background_image = pygame.image.load("display/background.png")
        self.title_background = pygame.image.load("display/Space.png")
        self.player_animation = 0
        self.opponent_animation = 0
        self.animation_count2 = 0
        self.dying_npc_animation = 0
        return

    def paint_pregame(self, surface, control):
        """
        Draws the display before the user selects the game type.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.blit(self.title_background, (0, 0))
        # text message in center of screen
        s = "Press 'd' for dual player, 's' for single player,"
        self.draw_text_center(surface, s, self.text_color,
                              self.width/3, self.height/5,
                              self.font)
        s = "'t' for tournament, 'esc' to quit."
        self.draw_text_center(surface, s, self.text_color,
                              self.width/3, self.height/5 + 3*self.font_size/2,
                              self.font)
        return
        
    def paint_waiting_for_game(self, surface, engine, control):
        """
        Draws the display after user selects the game type, before the game begins.
        This is usually a brief period of time, while waiting for an opponent
        to join the game.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill(self.background_color, rect)
        # text message in center of screen
        s = "Waiting for opponent to connect."
        self.draw_text_center(surface, s, self.text_color,
                              self.width/2, self.height/2,
                              self.font)
        return

    def paint_game(self, surface, engine, control):
        """
        Draws the display after the game starts.
        """
        # background
        rect = pygame.Rect(0, 0, self.width, self.height)
        surface.fill(self.background_color, rect)
        surface.blit(self.background_image, (0, 0))


        self.player_animation += .2
        if self.player_animation >= 4:
            self.player_animation = 0
        self.opponent_animation += .2
        if self.opponent_animation >= 4:
            self.opponent_animation = 0

        self.animation_count2 += .25
        if self.animation_count2 >= 2:
            self.animation_count2 = 0

        self.dying_npc_animation += 1./50
        if self.dying_npc_animation >= 3:
            self.dying_npc_animation = 0

        # draw each object
        objs = engine.get_objects()
        for key in objs:
            obj = objs[key]
            if obj.is_wall():
                self.paint_wall(surface, engine, control, obj)
            elif obj.is_npc():
                self.paint_npc(surface, engine, control, obj)
            elif obj.is_missile():
                self.paint_missile(surface, engine, control, obj, int(self.animation_count2))
            elif obj.is_player():
                self.paint_player(surface, engine, control, obj)
            else:
                print "Unexpected object type: %s" % (str(obj.__class__))
                
        # draw game data
        if control.show_info:
            self.paint_game_status(surface, engine, control)
        return

        
    def paint_game_over(self, surface, engine, control):
        """
        Draws the display after the game ends.  This
        chooses to display the game, and add a game over
        message.
        """
        self.paint_game(surface, engine, control)
        
        s = "Game Over (%s wins!)" % (engine.get_winner_name())
        self.draw_text_center(surface, s, self.text_color, int(self.width/2), int(self.height/2), self.font)
        return

    def process_event(self, surface, engine, control, event):
        """
        Should process the event and decide if it needs to be displayed, or heard.
        """
        #print event
        return

    # The following methods draw appropriate rectangles
    # for each of the objects, by type.
    # Most objects have an optional text display to
    # demonstrate how to send information from the control
    # to the display.
    def paint_wall(self, surface, engine, control, obj):
        """
        Draws walls.
        """
        rect = self.obj_to_rect(obj)
        surface.blit(self.wall_image, (obj.get_px(), obj.get_py()))
        return
        
    def paint_npc(self, surface, engine, control, obj):
        """
        Draws living NPCs.
        """
        if obj.is_alive():
            rect = self.obj_to_rect(obj)
            surface.blit(self.npc_images[3], (obj.get_px(), obj.get_py()))
        elif obj.is_dying():
            surface.blit(self.npc_images[int(self.dying_npc_animation)], (obj.get_px(), obj.get_py()))
        return
        
    def paint_missile(self, surface, engine, control, obj, animation):
        """
        Draws living missiles.
        """
        if obj.is_alive():
            color = self.missile_color
            rect = self.obj_to_rect(obj)
            surface.blit(self.missile_image[animation], (obj.get_px(), obj.get_py()))
        return
        
    def paint_player(self, surface, engine, control, obj):
        """
        Draws living players.
        My player is my opponent are in different colors
        """
        if obj.is_alive():
            image = ""
            rect = self.obj_to_rect(obj)
            if obj.get_oid() == engine.get_player_oid():
                player = engine.get_object(engine.get_player_oid())
                if player:
                    if player.get_speed() <= .5:
                        self.player_animation = 4
                image = self.player_image[int(self.player_animation)]
            else:
                opponent = engine.get_object(engine.get_opponent_oid())
                if opponent:
                    if opponent.get_speed() <= .5:
                        self.opponent_animation = 4
                image = self.opponent_image[int(self.opponent_animation)]
            surface.blit(image, (obj.get_px(), obj.get_py()))
        return

    def paint_game_status(self, surface, engine, control):
        """
        This method displays some text in the bottom strip
        of the screen.  You can make it do whatever you want,
        or nothing if you want.
        """

        # display my stats
        oid = engine.get_player_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                alignment_spacing = ""
                if len(engine.get_name()) + 4 < len(engine.get_opponent_name()) + 10:
                    alignment_spacing = " " * ((len(engine.get_opponent_name()) + 10) - (len(engine.get_name()) + 4))
                s = "Me: %s %s HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_name(),
                     alignment_spacing,
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                position_x = 20
                position_y = self.height - STATUS_BAR_HEIGHT + 3 * self.font_size / 2
                self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
                
        # display opponent's stats
        oid = engine.get_opponent_oid()
        if oid > 0: 
            obj = engine.get_object(oid)
            if obj:
                alignment_spacing = ""
                if len(engine.get_opponent_name()) + 10 < len(engine.get_name()) + 4:
                    alignment_spacing = " " * ((len(engine.get_name()) + 4) - (len(engine.get_opponent_name()) + 10))
                s = "Opponent: %s %s HP: %.1f  XP: %.1f Mv: %.1f Ms: %.1f" % \
                    (engine.get_opponent_name(),
                     alignment_spacing,
                     obj.get_health(),
                     obj.get_experience(),
                     obj.get_move_mana(),
                     obj.get_missile_mana())
                position_x = 20
                position_y = self.height - STATUS_BAR_HEIGHT + 6 * self.font_size / 2
                self.draw_text_left(surface, s, self.text_color, position_x, position_y, self.font)
        return
