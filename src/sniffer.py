from time import sleep

from socket import socket
from socket import PF_PACKET, SOCK_RAW, ntohs

from bitstring import BitStream

from layers.ethernet.frame import Frame

class Sniffer:
    def __init__(self, interface):
        self.setInterface(interface)

    def setInterface(self, interface):
        self.interface=False
        if interface:
            with open('/proc/net/dev', 'r') as f:
                for i in f.readlines():
                    raw=i.replace(":", "")
                    interfaces=raw.split(" ")
                    if interface in interfaces:
                        self.interface=interface
                        self.bind=(self.interface, 0)

    def start(self, stop=0):
        counter = 0

        if not self.interface:
            raise Exception("Interface not found")

        conn = socket(PF_PACKET, SOCK_RAW, ntohs(3))
        conn.bind(self.bind)

        while True:
            if not stop == 0 and counter == stop:
                break
            raw, addr = conn.recvfrom(65536)
            bitstream = BitStream(raw)
            layers=[]
            layer0 = Frame(bitstream)
            if layer0:
                if not layer0.ether_type == 'ipv4':
                    continue

                del bitstream[:layer0.header_size]
                #del bitstream[-layer0.footer_size:]
                layers.append(layer0)

                layer1 = layer0.next(bitstream)

                if layer1:
                    if not layer1.protocol == 1:
                        continue

                    del bitstream[:layer1.header_size]
                    layers.append(layer1)

                    layer2 = layer1.next(bitstream)

                    if layer2:
                        del bitstream[:layer2.header_size]
                        layers.append(layer2)

                        layer3 = layer2.next(bitstream)

                        if layer3:
                            del bitstream[:layer3.header_size]
                            layers.append(layer3)

            counter += 1
            yield layers

            sleep(0.001)
