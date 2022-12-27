# API operations (For easy reference)
# Create - Post
# Read - get
# Update - Put
# Delete - Delete

# Server Test

import json
import socket
from select import select

class Session(object):
    def call(self, name, *args):
        pass

    def error():
        pass

class RpcServer(object):

    pass


class RpcCore(object):
    def __init__(self):
        self.selectable = []
        self.endpoints = {}
    
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