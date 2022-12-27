# API operations (For easy reference)
# Create - Post
# Read - get
# Update - Put
# Delete - Delete

# Server Test

import json
import socket
from select import select
from http.client import HTTPConnection

class Error(Exception):
    pass
    
# Playing around with socket to make a server

# Server: 
# RPc Session
class Session(object):
    def __init__(self, core, s):
        self.core = core
        self.s = s
        self.output_buffer = ''
        self.input_buffer = ''
    
    def call(self, name, *args):
        if not self.core.endpoints.has_key(name):
            self.error("No endpoint")
            return
        
        endpoint = self.core.endpoints[name]
        if len(args) != endpoint.__code__.co_argcount:
            self.error("Wrong endpoint address")
            return

        try:
            result = endpoint(*args)
        except:
            self.error("Error")
            return

        data = {'type': 'result', 'result': result}
        # Puts result in cache/memory
        self.output_buffer += json.dumps(data) + '\n'
    
    def error(self, reason):
        error = {'type': 'error', 'reason': reason}
        self.output_buffer += json.dumps(error) + '\n'
    
    # Missing: Write function


# Rpc Server
# Credit: johnmarshall for some of the code for RpcServer function (https://github.com/joshmarshall/jsonrpclib/blob/master/jsonrpclib/jsonrpc.py)
class RpcServer(object):

    def __init__(self, core, addr):
        self.core = core

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Reminder: Sockopt used to control socket; SO_REUSADOR Specifies that the rules used in validating addresses supplied to bind() should allow reuse of local addresses, if this is supported by the protocol. This option takes an int value. This is a Boolean option.
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(addr)
        self.s.listen(5)

    def location(self):
        return self.s.location()
    
    @property
    def can_read(self):
        return True
        
    @property
    def can_write(self):
        return False

    def read(self):
        conn, _ = self.s.accept()
        session = Session(self.core, conn)
        self.core.selectable.append(session)


#server core

class RpcCore(object):
    def __init__(self):
        self.selectable = []
        self.endpoints = {}
    
    #listen to port
    
    def listen(self, addr=('0.0.0.0', 12345)):
        #listener function here
        self.selectable.append()

    def listen_2(self, addr=('127.0.0.1', 54321)):
        #listener
        self.selectable.append()

    def run(self):
        self.terminate = False
        while not self.terminate:
            self.tick()

    def tick(self):
        read_objs = (obj for obj in self.selectable if obj.can_read)
        write_objs = (obj for obj in self.selectable if obj.can_write)

        readable, writeable, _ = select(read_objs, write_objs, [], 0.25)

        for obj in readable:
            obj.do_read()

        for obj in writeable:
            obj.do_write()

    def shutdown(self, reason=''):
        self.terminate = True

    def export(self, f):
        name = f.__name__
        self.endpoints[name] = f
        return f

# running

if __name__ == '__main__':
    core = RpcCore()
    #core.listen()
    #core.listen_2()

    @core.export
    def test():
        return 'k'

    core.run()