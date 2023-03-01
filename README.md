# sniffer

Pure Python packet sniffer for academic purposes.

Working at bit level then return a Python object for each iso layer.

Supported protocols for layer:
- Data link: [Ethernet frame](src/layers/ethernet.frame.py)
- Internet: [IP](src/layers/internet/ipv4/ip.py),
    - Internet procols: [VRRP](src/layers/internet/ipv4/protocol/vrrp.py),
- Transport: [TCP](src/layers/transport/tcp.py),

## Project's goals:
1) Academic purposes
2) Offering a pure Python Linux based packet sniffer
3) Create a interface to directly streaming packets to a message broker (REDIS, Kafka, RabbitMQ) 

## Output
At core level, each parsed layer is returned as object into an array.

TCP example:
```
[<layers.ethernet.frame.Frame object at 0xffff8a2bbfa0>, <layers.internet.ipv4.ip.Ip object at 0xffff8a13e380>, <layers.transport.tcp.Tcp object at 0xffff8a13e7a0>]
```

VRRP example:
```
[<layers.ethernet.frame.Frame object at 0xffffb84332b0>, <layers.internet.ipv4.ip.Ip object at 0xffffb8433940>, <layers.internet.ipv4.protocol.vrrp.Vrrp object at 0xffffb8433880>]
``` 
