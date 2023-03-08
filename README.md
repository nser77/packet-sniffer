# packet-sniffer

Pure Python object oriented packet sniffer that streams packets to message brokers.

## Project's goals:
1) Academic purposes
2) Offering a pure Python packet sniffer
3) Object oriented sniffer
4) Directly stream packets to message brokers (REDIS, Kafka, RabbitMQ)
5) High code readability

## Supported protocols for layer
Very work in progress project:

### Data link 
Protocol | Version | Switch | Source
--- | --- | --- | ---
Ethernet frame | Stable | yes | [frame.py](src/layers/ethernet.frame.py)

### Internet
Protocol | Version | Switch | Source
--- | --- | --- | ---
IPv4 | Stable | yes | [ip.py](src/layers/internet/ipv4/ip.py)

#### IPv4 protocols
Name | Number | Version | Stable | Data | Source | Example
--- | --- | --- | --- | --- | --- | ---
ICMP | 1 | ipv4 | Stable | No | [icmp.py](src/layers/internet/ipv4/protocol/icmp.py) | [icmp.json](examples/icmp.json.md)
VRRP | 112 | ipv4 | Stable | yes | [vrrp.py](src/layers/internet/ipv4/protocol/vrrp.py) | [vrrp.json](examples/vrrp.json.md)

### IPv4 transport protocols
Name | Number | Version | Stable | Data | Source | Example
--- | --- | --- | --- | --- | --- | ---
TCP | 6 | ipv4 | Unstable | No | [tcp.py](src/layers/transport/tcp.py) | [tcp.json](examples/tcp.json.md)

## Usage
Prints packet to cli and sending them to REDIS:
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

Example of REDIS client:
```
import redis, json

r=redis.Redis(host="redis.it.home.local")

for i in r.lrange("vrrp", 0, -1):
    packet=json.loads(i)
    print(packet[1]['identification'], "\n")

r.rpop("vrrp", r.llen("vrrp"))
```

### next(bistream) method
Each object class must implement a method called next; where the only parameter is a Bitstream object.

This is useful to implement a protocol-oriented switch like this:

```
src/ethernet/frame.py:

[...]
    def next(self, bitstream):
        if isinstance(bitstream, BitStream):
            match self.ether_type:
                case 'ipv4':
                    return Ip(bitstream)
                case _:
                    return False
[...]
```

In the above example, the next() method will return the Ip object only if ```ether_type``` is equal to ```"ipv4"```.

This could be more useful in protocols like UDP or TCP:

```
src/transport/udp.py:

[...]
    def next(self, bitstream):
        if isinstance(bitstream, BitStream):
            # unencrypted protocols
            if self.src_port == 53 or self.dst_port == 53:
                return Dns(bitstream)
            if self.src_port == 5060 or self.dst_port == 5060:
                return Sip(bitstream)
[...]

--

src/transport/tcp.py:

[...]
    def next(self, bitstream):
        if isinstance(bitstream, BitStream):
            # unencrypted protocols
            if self.src_port == 23 or self.dst_port == 23:
                return Telnet(bitstream)
            if self.src_port == 53 or self.dst_port == 53:
                return Dns(bitstream)
            if self.src_port == 80 or self.dst_port == 80:
                return Http(bitstream)
[...]

```

## Output
Output types:

### Core
Because the length of each packet can variate based on his scope, each parsed layer is returned as an object within an array.

VRRP example:
```
[<layers.ethernet.frame.Frame object at 0xffffbd6a03d0>, <layers.internet.ipv4.ip.Ip object at 0xffffbd7fbdc0>, <layers.internet.ipv4.protocol.vrrp.Vrrp object at 0xffffbd6a0430>]
```

### JSON
In case of VRRP packet, the sniffer can get the VIPs; but this is not an additional layer:
```
[{"dst_mac": "01:00:5e:00:00:12", "header_size": 112, "src_mac": "e4:5f:01:9d:b9:e0", "ether_type": "ipv4", "footer_size": 32},
{"version": 4, "header_size": 160, "ihl": 5, "tos": "c0", "total_length": 40, "identification": 159, "flag0": 0, "flag1": 0, "flag2": 0, "fragment_offset": 0, "ttl": 255, "protocol": 112, "header_checksum": "cfe5", "src": "10.1.0.14", "dst": "224.0.0.18"},
{"version": 3, "header_size": 64, "type": 1, "virtual_router_id": 99, "priority": 233, "count_ipvx_addr": 3, "reserved": 0, "max_advertisement_interval_c": 100, "vips": ["192.168.1.252", "192.168.1.253", "192.168.1.254"]}]
```
