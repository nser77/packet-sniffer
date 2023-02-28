from socket import socket
from socket import PF_PACKET, SOCK_RAW, ntohs

from bitstring import BitStream

from ethernet.frame import EthernetFrame
from internet.ipv4.ipv4_packet import Ipv4Packet
from internet.ipv4.tcp.tcp_packet import Ipv4PacketTcp

class Sniffer:
    def start(self):
        conn = socket(PF_PACKET, SOCK_RAW, ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            bitstream = BitStream(raw)

            layers=[]

            ethernet_frame = EthernetFrame(bitstream)
            del bitstream[:ethernet_frame.header_size]
            del bitstream[-ethernet_frame.footer_size:]
            layers.append(ethernet_frame)

            ipv4_packet = Ipv4Packet(bitstream)
            del bitstream[:ipv4_packet.header_size]
            layers.append(ipv4_packet)

            #ipv4_packet.switch()
 
            yield layers
