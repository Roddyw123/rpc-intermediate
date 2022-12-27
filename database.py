import json
import socket


class Database(object):
    def __init__(self, host, port, driver, connection_string, password=""):
        self._socket = socket.create_connection((host, port))
        self._pass = password
        self._driver = driver
        self._connection_string = connection_string
        self._id = 0
    
    def retrieve(self, statement, params=[]):

        message_id = self._id
        self._id = self._id + 1

        # didnt know what to do here
    
    def request(self, request):
        pass




if __name__ == "__main__":
    db = Database('127.0.0.1', 12345, "sqlite3", "./1.db")
    print(db.sql("select * from test"))