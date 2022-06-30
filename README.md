# Raft Kurs

Dieser Kurs ist über [raft][raft-website], ein Konsens Algorithmus. Das [Paper gibt es hier][raft-paper].
Ziel des Kurses ist es Raft zu implementieren und alles notwendige dafür zu erlernen. Dieser Kurs ist
noch in Arbeit und wird weiterhin erweitert.

## Vorbereitung

1. [Netzwerkprogrammierung](docs/00_Vorbereitung/01_Netzwerkprogrammierung/README.md)
   1. [Raw TCP Sockets](docs/00_Vorbereitung/01_Netzwerkprogrammierung/01_Raw_TCP_Sockets.md)
   2. Raw UDP Sockets
   3. Mehrere Verbindungen auf einmal
   4. High-Level Server
   5. Asyncio
2. Tests
   1. `pytest` Grundlagen
   2. Mit `parametrized` Tests generieren
   3. Mit `mock` Funktionen und Module nachmachen

## Der Raft Algorithmus

1. Das Log
2. Die Nachrichten
3. Die Netzwerkintegration

[raft-website]: https://raft.github.io/
[raft-paper]: https://raft.github.io/raft.pdf

