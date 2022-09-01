import pytest
from vorbereitung.netzwerk.raw_socket import client


@pytest.mark.timeout(1)
@pytest.mark.netzwerk
def test_client(server):

    antwort = client("localhost", server.port, input=lambda x: b"Hallo Welt!")
    assert antwort == b"HALLO WELT!"
