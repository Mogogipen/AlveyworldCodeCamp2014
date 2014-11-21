import sys
sys.path.append('..')
from engine_server.config import *

# You are encouraged to set the DEFAULT_GAME_TITLE and
# DEFAULT_TEAM_NAME, but discouraged from changing other
# values, unless you are sure you know what you are doing.

# Configure this to put a title in the top of your window
DEFAULT_GAME_TITLE = "We didn't set our game title yet"
# Configure this to use your name during games with others
DEFAULT_TEAM_NAME  = "We didn't set our team name yet"

# This is the number of times to check for input and redraw
# the screen every second.  If your computer is slow, then
# you may want to make this smaller.  If you have a fast
# computer, you can try to make this larger.
FRAMES_PER_SECOND = 30

# This is how long to wait after the game is over
# before returning to the pre-game display
POST_GAME_WAIT_TIME = 5 # seconds


# How wide the window is.  This doesn't change the width of the game.
WINDOW_WIDTH       = FIELD_WIDTH + 0
# How high the status bar at the bottom of the window is.
STATUS_BAR_HEIGHT  = 60
# How tall the window is.  This doesn't change the height of the game.
WINDOW_HEIGHT      = FIELD_HEIGHT + STATUS_BAR_HEIGHT
