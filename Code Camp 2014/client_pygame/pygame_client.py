#
# You should not make changes to this file
#
import pygame
import sys
from config import *
from client.base_control import *
from client.pygame_socket_game import PygameSocketGame
from common.game_comm import *
from engine_client.game_engine import ClientGameEngine
import engine_client.game_engine as game_engine
from display.display import Display
from control.control import Control

class PygameClient(PygameSocketGame):
    """
    This class connects the control and display for the game.
    You shouldn't need to make changes here.
    """

    def __init__(self, width, height, frame_rate, name, title, server_host="localhost", server_port=20149):
        PygameSocketGame.__init__(self, title, width, height, frame_rate, server_host, server_port)
        self.name = name
        self.display = Display(width, height)
        self.control = Control(width, height)
        return
    
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.control.control(self.engine, keys, newkeys, buttons, newbuttons, mouse_position)

        if self.control.get_state() == CONTROL_STATE_WANT_DUAL:
            self.new_game(game_engine.MODE_DUAL)
        elif self.control.get_state() == CONTROL_STATE_WANT_SINGLE:
            self.new_game(game_engine.MODE_SINGLE)
        elif self.control.get_state() == CONTROL_STATE_WANT_TOURNAMENT:
            self.new_game(game_engine.MODE_TOURNAMENT)
        elif self.control.get_state() == CONTROL_STATE_WANT_VIEW:
            self.new_game(game_engine.MODE_VIEW)
        
        if self.engine and self.engine.get_data().get_game_over():
            self.game_over_pause += 1
            if self.game_over_pause > self.frames_per_second * POST_GAME_WAIT_TIME:
                self.disconnect_from_server()
                self.set_engine(None)
        return

    def paint(self, surface):
        self.display.paint(surface, self.engine, self.control)
        return
    
    def new_game(self, mode):
        self.set_engine(ClientGameEngine(self.name, mode))
        self.disconnect_from_server()
        self.connect_to_server()
        self.game_over_pause = 0
        return
