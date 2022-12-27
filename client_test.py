import socket
from select import select
import json


class Client(object):
    def __init__(self, addr):
        # ._s is socket
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.connect(addr)
        self._input_buffer = ''
    
    def close_session(self):
        self._s.close()