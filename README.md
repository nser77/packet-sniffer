# sniffer

Pure Python packet sniffer for academic purposes.

Slicing and unpacking network packets by OSI stack (Frame, Packet and Data) then create the correspondend Python object.

Each object accept his part of the packet sliced out of the bytes of the preceding layer.

## Project's goals:
1) Academic purposes
2) Offering a pure Python Linux based packet sniffer
3) Create a interface to directly streaming packets to a message broker (REDIS, Kafka, RabbitMQ) 
