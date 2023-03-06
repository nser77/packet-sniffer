# packet-sniffer

Pure Python packet sniffer for academic purposes that streams packets to message brokers.

Supported protocols for layer:
- Data link: [Ethernet frame](src/layers/ethernet.frame.py)
- Internet: [IP](src/layers/internet/ipv4/ip.py),
    - Internet procols: [VRRP](src/layers/internet/ipv4/protocol/vrrp.py),
- Transport: [TCP](src/layers/transport/tcp.py),

# TO-DO
- Using ```ctypes``` library to convert sliced bit data from ```bitstring```.  

## Project's goals:
1) Academic purposes
2) Offering a pure Python packet sniffer
3) Object oriented sniffer
4) Directly stream packets to message brokers (REDIS, Kafka, RabbitMQ)
5) High code readability

## Usage

```
from sniffer import Sniffer

from output.output import Output
from output.type import OutputType

try:
    sniffer=Sniffer()
    for packet in sniffer.start():
        if packet:
            Output.cli(OutputType.json(packet))
            Output.redis("vrrp", OutputType.json(packet))
except KeyboardInterrupt:
    print("\n")
```

## Output
At core level, each parsed layer is returned as object into an array.

VRRP example:
```
[<layers.ethernet.frame.Frame object at 0xffffbd6a03d0>, <layers.internet.ipv4.ip.Ip object at 0xffffbd7fbdc0>, <layers.internet.ipv4.protocol.vrrp.Vrrp object at 0xffffbd6a0430>]

[{"dst_mac": "01:00:5e:00:00:12", "header_size": 112, "src_mac": "e4:5f:01:9d:b9:e0", "ether_type": "ipv4", "footer_size": 32}, {"version": 4, "header_size": 160, "ihl": 5, "tos": "c0", "total_length": 32, "identification": 25132, "flag0": 0, "flag1": 0, "flag2": 0, "fragment_offset": 0, "ttl": 255, "protocol": 112, "header_checksum": "6e60", "src": "10.1.0.14", "dst": "224.0.0.18"}, {"version": 3, "header_size": 64, "type": 1, "virtual_router_id": 99, "priority": 233, "count_ipvx_addr": 1, "reserved": 0, "max_advertisement_interval_c": 100}]
``` 

TCP example:
```
[<layers.ethernet.frame.Frame object at 0xffff8a2bbfa0>, <layers.internet.ipv4.ip.Ip object at 0xffff8a13e380>, <layers.transport.tcp.Tcp object at 0xffff8a13e7a0>]

[{"dst_mac": "c4:ad:34:c5:82:f6", "header_size": 112, "src_mac": "e4:5f:01:9d:b9:e0", "ether_type": "ipv4", "footer_size": 32}, {"version": 4, "header_size": 160, "ihl": 5, "tos": "10", "total_length": 792, "identification": 4487, "flag0": 0, "flag1": -1, "flag2": 0, "fragment_offset": 0, "ttl": 64, "protocol": 6, "header_checksum": "119b", "src": "10.1.0.14", "dst": "10.150.0.10"}, {"src_port": 22, "header_size": 160, "dst_port": 30877, "sequence_number": 453040850, "acknowledgment_number": 2150666073, "data_offset": 5, "reserved": 0, "cwr": 0, "ece": 0, "urg": 0, "ack": -1, "psh": -1, "rst": 0, "syn": 0, "fin": 0, "window_size": 1365, "checksum": "17b9", "urgent_pointer": 0}]
```
