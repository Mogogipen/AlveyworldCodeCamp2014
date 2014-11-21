#
# Don't change this file.
#
import socket, select, sys, logging
from client.pygame_game import PygameGame
from client.client_game_socket import ClientGameSocket

class PygameSocketGame(PygameGame):
    """
    PygameSocketGame uses the main_loop() from PygameGame
    to get all pygame event handling. It overrides the
    generate_external_events() method to add in socket
    message processing.  This means the sockets are not
    event driven, but poll driven, with polls at the frame
    rate of pygame. It uses a ClientGameSocket object
    to manage all server communications.

    Methods:
    get_sock()
    set_engine(engine)
    connect_to_server()
    disconnect_from_server()
    generate_external_events()
    """

    def __init__(self, name, width, height, frames_per_second, server_host="localhost", server_port=20149, engine=None):
        self.logger = logging.getLogger('PygameSocketGame')
        PygameGame.__init__(self, name, width, height, frames_per_second)
        self.read_list = []
        self.server_host = server_host
        self.server_port = server_port
        self.client_game_socket = ClientGameSocket(self.read_list, self.server_host, self.server_port)
        self.engine = engine
        return

    def get_sock(self):
        return self.client_game_socket.get_sock()
        
    def set_engine(self, engine):
        self.engine = engine
        return
        
    def connect_to_server(self):
        self.client_game_socket.connect_to_server()
        return

    def disconnect_from_server(self):
        self.client_game_socket.disconnect_from_server()
        return
        
    def socket_is_ready(self):
        rds, wrs, xs = select.select(self.read_list, [], [], 0.0)
        for fd in rds:
            if self.client_game_socket.is_ready(fd):
                return True
        return False
        
    def generate_external_events(self):
        if self.engine:
            # receive incoming messages
            while self.socket_is_ready():
                self.client_game_socket.process_event(self.engine)
            # send outgoing messages
            self.client_game_socket.send_messages(self.engine)
        return
