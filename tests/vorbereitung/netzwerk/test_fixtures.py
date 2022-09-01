import socket

import pytest


def test_server(server):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", server.port))
    sock.send(b"Hallo Welt!")
    antwort = sock.recv(1024)
    assert antwort == b"HALLO WELT!"
    sock.close()


def test_fail():
    d = dict(a=True, b=True, r="other")

    assert d["a"] == True and d["b"] == False and d["r"] == "other"
