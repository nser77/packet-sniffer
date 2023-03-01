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
            sleep(0.001)
            layers=[]
            counter += 1
            raw, addr = conn.recvfrom(65536)
            bitstream = BitStream(raw)
            frame = Frame(bitstream)
            if frame:
                if not frame.ether_type == 'ipv4':
                    continue
                del bitstream[:frame.header_size]
                del bitstream[-frame.footer_size:]
                layers.append(frame)
                ip = frame.switch(bitstream)
                if ip:
                    if not ip.protocol == 6:
                        continue
                    del bitstream[:ip.header_size]
                    layers.append(ip)
                    transport = ip.switch(bitstream)
                    if transport:
                        del bitstream[:transport.header_size]
                        layers.append(transport)
            yield layers
