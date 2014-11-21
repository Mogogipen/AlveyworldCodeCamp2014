#
# Don't change this file.
#
import pygame
pygame.font.init()
pygame.mixer.init()
from client.base_control import *

class BaseDisplay:

    def __init__(self, width, height):
        """
        Configure display-wide settings and one-time
        setup work here.
        """
        self.width = width
        self.height = height
        return

    def paint(self, surface, engine, control):
        """
        Main control for displaying a frame.
        """

        state = control.get_state()
        if state == CONTROL_STATE_HAVE_ENGINE:
            if engine:
                data = engine.get_data()
                if data.get_game_started():
                    self.paint_game(surface, engine, control)
                elif (data.get_waiting_for_dual() or
                      data.get_waiting_for_single() or
                      data.get_waiting_for_tournament() or
                      data.get_waiting_for_view()):
                    self.paint_waiting_for_game(surface, engine, control)
                elif data.get_game_over():
                    self.paint_game_over(surface, engine, control)
                else:
                    print "Unexpected game state in BaseDisplay.paint() [may happen once per game.]"
                self.process_events(surface, engine, control)
            else:
                # this happens 1 frame at the end of the game.  No problem
                # print "No engine in BaseDisplay.paint()"
                pass
        elif state == CONTROL_STATE_NO_ENGINE:
            self.paint_pregame(surface, control)
        elif (state == CONTROL_STATE_WANT_DUAL or
              state == CONTROL_STATE_WANT_SINGLE or
              state == CONTROL_STATE_WANT_TOURNAMENT or
              state == CONTROL_STATE_WANT_VIEW):
            self.paint_waiting_for_game(surface, engine, control)
        else:
            print "Unexpected state in BaseDisplay.paint()"
        return

    def paint_pregame(self, surface, control):
        raise NotImplementedError("Display.paint_pregame is not yet implemented")
        return
    def paint_waiting_for_game(self, surface, engine, control):
        raise NotImplementedError("Display.paint_waiting_for_game is not yet implemented")
        return
    def paint_game(self, surface, engine, control):
        raise NotImplementedError("Display.paint_game is not yet implemented")
        return
    def paint_game_over(self, surface, engine, control):
        raise NotImplementedError("Display.paint_game_over is not yet implemented")
        return
    def process_event(self, surface, engine, control, event):
        raise NotImplementedError("Display.process_event is not yet implemented")
        return
    def process_events(self, surface, engine, control):
        """
        Processes each event in the engine's event queue, then empties the queue.
        """
        for event in engine.get_event_queue():
            self.process_event(surface, engine, control, event)
        engine.clear_event_queue()
        return
        
    def obj_to_rect(self, obj):
        return pygame.Rect(obj.get_px(), obj.get_py(),
                           obj.get_pw(), obj.get_ph())
        
    def draw_text_left(self, surface, text, color, x, y, font):
        """Draws text left justified"""
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def draw_text_center(self, surface, text, color, x, y, font):
        """Draws text centered"""
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)
        return

    def draw_text_right(self, surface, text, color, x, y, font):
        """Draws text right justified"""
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return

