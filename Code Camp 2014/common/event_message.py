#
# Don't change this file
#
from common.game_message import GameMessage
from common.event import *

M_EVENT = "M_EVENT"
M_MISSILE_FIRE_EVENT = "M_MISSILE_FIRE_EVENT"
M_MISSILE_MISFIRE_EVENT = "M_MISSILE_MISFIRE_EVENT"
M_MISSILE_HIT_EVENT = "M_MISSILE_HIT_EVENT"
M_MISSILE_DYING_EVENT = "M_MISSILE_DYING_EVENT"

class EventMessage(GameMessage):
    def __init__(self, event=None):
        GameMessage.__init__(self, M_EVENT)
        if event:
            event.set_message(self)
        return

def string_to_event_message(string):
    msg = EventMessage()
    msg.from_string(string)
    return msg
    
class MissileFireEventMessage(GameMessage):
    def __init__(self, event=None):
        GameMessage.__init__(self, M_MISSILE_FIRE_EVENT)
        if event:
            event.set_message(self)
        return

def string_to_missile_fire_event_message(string):
    msg = EventMessage()
    msg.from_string(string)
    return msg
    
class MissileMisfireEventMessage(GameMessage):
    def __init__(self, event=None):
        GameMessage.__init__(self, M_MISSILE_MISFIRE_EVENT)
        if event:
            event.set_message(self)
        return

def string_to_missile_misfire_event_message(string):
    msg = EventMessage()
    msg.from_string(string)
    return msg
    
class MissileHitEventMessage(GameMessage):
    def __init__(self, event=None):
        GameMessage.__init__(self, M_MISSILE_HIT_EVENT)
        if event:
            event.set_message(self)
        return

def string_to_missile_hit_event_message(string):
    msg = EventMessage()
    msg.from_string(string)
    return msg
    
class MissileDyingEventMessage(GameMessage):
    def __init__(self, event=None):
        GameMessage.__init__(self, M_MISSILE_DYING_EVENT)
        if event:
            event.set_message(self)
        return

def string_to_missile_dying_event_message(string):
    msg = EventMessage()
    msg.from_string(string)
    return msg
    
def message_to_event(msg):
    code = msg.get_command()
    if code == M_EVENT:
        event = Event()
    elif code == M_MISSILE_FIRE_EVENT:
        event = MissileFireEvent()
    elif code == M_MISSILE_MISFIRE_EVENT:
        event = MissileMisfireEvent()
    elif code == M_MISSILE_HIT_EVENT:
        event = MissileHitEvent()
    elif code == M_MISSILE_DYING_EVENT:
        event = MissileDyingEvent()
    else:
        event = None
    if event:
        event.set_from_message(msg)
    return event

def event_to_message(event):
    kind = event.get_kind()

    if kind == E_MISSILE_FIRE:
        msg = MissileFireEventMessage(event)
    elif kind == E_MISSILE_MISFIRE:
        msg = MissileMisfireEventMessage(event)
    elif kind == E_MISSILE_HIT:
        msg = MissileHitEventMessage(event)
    elif kind == E_MISSILE_DYING:
        msg = MissileDyingEventMessage(event)
    else:
        msg = None
    return msg

# 
EVENT_MESSAGES = { M_EVENT:   string_to_event_message,
                   M_MISSILE_FIRE_EVENT:    string_to_missile_fire_event_message,
                   M_MISSILE_MISFIRE_EVENT: string_to_missile_misfire_event_message,
                   M_MISSILE_HIT_EVENT:     string_to_missile_hit_event_message,
                   M_MISSILE_DYING_EVENT:   string_to_missile_dying_event_message }


