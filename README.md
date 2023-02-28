# sniffer

Pure Python packet sniffer for academic purposes.

Working at bit level then return a Python object for each iso layer.

```
THIS IS A PACKET-SNIFFER, no a packet-capture software.
```

## Project's goals:
1) Academic purposes
2) Offering a pure Python Linux based packet sniffer
3) Create a interface to directly streaming packets to a message broker (REDIS, Kafka, RabbitMQ) 

## Output
At core level, each parsed layer is returned as object into an array:

```
[<ethernet.frame.EthernetFrame object at 0xffff8ca7ded0>, <internet.ipv4.ipv4_packet.Ipv4Packet object at 0xffff8ca7df30>]
```
