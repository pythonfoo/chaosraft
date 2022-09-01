import socket


def client(host, port, input=input) -> bytes:
    """
    TODO: Implementiere einen Client, der einen RAW-Socket eröffnet und mit dem Server verbindet
    und die Antwort des Servers zurückliefert.

    :param host: Hostname des Servers
    :param port: Port des Servers
    :return: Antwort des Servers
    """

    daten_für_den_server = input("Daten für den Server: ")

    return b""


if __name__ == "__main__":
    host = frage("Host: ", default="localhost")
    port = frage("Port: ", default=8080)
    client(host, port)
