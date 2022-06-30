# Raw TCP Sockets

## Client

Hier wird gezeigt wie man mit {class}`socket.socket` umgeht.
Um sich als Client um sich zu einem Server zu verbinden nutzt man die
{class}`socket.socket.connect` Methode.

```
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("chaosdorf.de", 80))
```

Zum senden gibt es {class}`socket.socket.send` und zum lesen die {class}`socket.socket.recv` Methode.

```
sock.send("GET / HTTP 1.0\r\n\r\n".encode())
data = sock.recv(1024)
print(f"Received: {data.decode()}")
```

## Server
Um als Server einen Socket zum lesen aufzumachen benötigt man die {class}`socket.socket.bind` Methode.

```
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("", 12345))
sock.listen()
```

```{admonition} Aufgepasst
:class: attention
`SO_REUSEADDR` kann unsicher sein, da der Port sofort wieder freigegeben wird sobald der Prozess sich beendet. Zum Entwickeln ist es aber hilfreich nicht immer den Port ändern zu müssen.
```
