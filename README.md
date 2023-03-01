# sniffer

Pure Python packet sniffer for academic purposes.

Working at bit level then return a Python object for each iso layer.

## Project's goals:
1) Academic purposes
2) Offering a pure Python Linux based packet sniffer
3) Create a interface to directly streaming packets to a message broker (REDIS, Kafka, RabbitMQ) 

## Output
At core level, each parsed layer is returned as object into an array:

```
[<layers.ethernet.frame.Frame object at 0xffffa65586a0>, <layers.internet.ipv4.ip.Ip object at 0xffffa63ed330>]
```
