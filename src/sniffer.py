from socket import socket
from socket import PF_PACKET, SOCK_RAW, ntohs

from bitstring import BitStream

from json import dumps

from layers.ethernet.frame import Frame
from layers.internet.ipv4.ip import Ip

class Sniffer:
    def __init__(self):
        pass

    def start(self, stop=0):
        counter = 0

        conn = socket(PF_PACKET, SOCK_RAW, ntohs(3))

        while True:
            counter += 1

            if not stop == 0 and counter == stop:
                break

            raw, addr = conn.recvfrom(65536)

            bitstream = BitStream(raw)

            layers=[]

            frame = Frame(bitstream)

            if frame:
                del bitstream[:frame.header_size]
                del bitstream[-frame.footer_size:]
                layers.append(frame)

                ip = frame.switch(bitstream)

                if ip:
                    del bitstream[:ip.header_size]
                    layers.append(ip)

                    transport = ip.switch(bitstream)

                    if transport:
                        del bitstream[:transport.header_size]
                        layers.append(transport)

                        #data=transport.switch(bitstream)

            #print(bitstream.bytes)

            yield layers
