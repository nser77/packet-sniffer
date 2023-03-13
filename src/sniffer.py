from time import sleep

from socket import socket
from socket import PF_PACKET, SOCK_RAW, ntohs

from bitstring import BitStream

from layers.ethernet.frame import Frame

class Sniffer:
    def __init__(self):
        pass

    def start(self, stop=0):
        counter = 0

        conn = socket(PF_PACKET, SOCK_RAW, ntohs(3))

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
                    if not layer1.protocol == 112:
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
