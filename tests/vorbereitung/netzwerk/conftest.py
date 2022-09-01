import random
from multiprocessing import Process

import pytest


@pytest.fixture
def server():
    # TODO server fährt nicht richtig runter wenn keine Verbindung aufgebaut wurde
    import socket

    class Server:
        def __init__(self, port: int):
            self.port = port

        def run(self):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind(("", self.port))
            self.sock.listen(1)
            self.client_sock = None
            self.client_addr = None
            self.client_sock, self.client_addr = self.sock.accept()
            data = self.client_sock.recv(1024)
            self.client_sock.send(self.process_data(data))
            # self.client_sock.close()

        def process_data(self, data: bytes) -> bytes:
            return data.upper()

    # start subprocess of server
    server = Server(random.randint(1024, 65535))
    server_process = Process(target=server.run)
    server_process.start()
    yield server

    # stop subprocess of server
    server_process.terminate()
