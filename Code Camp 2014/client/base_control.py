#
# Don't change this file.
#

CONTROL_STATE_NO_ENGINE = 0
CONTROL_STATE_WANT_DUAL = 1
CONTROL_STATE_WANT_SINGLE = 2
CONTROL_STATE_HAVE_ENGINE = 3
CONTROL_STATE_WANT_TOURNAMENT = 4
CONTROL_STATE_WANT_VIEW = 5

class BaseControl:
    """
    Base class for game controls in pygame.
    You should not need to modify this class.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = CONTROL_STATE_NO_ENGINE
        return

    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
        return
        
    def pregame_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        raise NotImplementedError("Control.pregame_control is not yet implemented")
        return

    def game_input_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        raise NotImplementedError("Control.game_input_control is not yet implemented")
        return
        
    def game_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        raise NotImplementedError("Control.game_control is not yet implemented")
        return
        
    def control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        """
        This method handles all user input,
        managing the state of the control system,
        and delegating to the proper method based
        on the current state.
        """

        if self.state == CONTROL_STATE_HAVE_ENGINE:
            # we think we have a game engine
            if engine:
                # still have a game engine
                self.game_input_control(engine, keys, newkeys, buttons, newbuttons, mouse_position)
                self.game_control(engine)
            else:
                # no longer have a game engine
                self.set_state(CONTROL_STATE_NO_ENGINE)
        elif self.state == CONTROL_STATE_NO_ENGINE:
            # we don't have a game engine, waiting for instructions from user
            self.pregame_control(engine, keys, newkeys, buttons, newbuttons, mouse_position)
        elif (self.state == CONTROL_STATE_WANT_DUAL or
              self.state == CONTROL_STATE_WANT_SINGLE or
              self.state == CONTROL_STATE_WANT_TOURNAMENT or
              self.state == CONTROL_STATE_WANT_VIEW):
            # we know what the user wants and we're waiting for the game to start
            if engine:
                # if we have a game engine, then the game has begun
                self.set_state(CONTROL_STATE_HAVE_ENGINE)
        else:
            # this should not happen
            print "Unexpected Control.state"

        return
