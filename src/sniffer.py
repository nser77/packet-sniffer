from socket import socket
from socket import PF_PACKET, SOCK_RAW, ntohs

from bitstring import BitStream

from ethernet.frame import EthernetFrame
from internet.ipv4.ipv4_packet import Ipv4Packet

class Sniffer:
    def start(self):
        conn = socket(PF_PACKET, SOCK_RAW, ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            bitstream=BitStream(raw)
            ethernet_frame = EthernetFrame(bitstream)
            ipv4_packet=Ipv4Packet(bitstream)
            
            layers=[]
            layers.append(ethernet_frame)
            layers.append(ipv4_packet)

            yield layers
