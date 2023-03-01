from socket import socket
from socket import PF_PACKET, SOCK_RAW, ntohs

from bitstring import BitStream

from layers.ethernet.frame import Frame
from layers.internet.ipv4.ip import Ip
from layers.transport.tcp import Tcp

class Sniffer:
    def start(self):
        conn = socket(PF_PACKET, SOCK_RAW, ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            bitstream = BitStream(raw)

            layers=[]

            frame = Frame(bitstream)

            if frame:
                del bitstream[:frame.header_size]
                del bitstream[-frame.footer_size:]
                layers.append(frame)
                
                if frame.ether_type == 'ipv4':    
                    ip = Ip(bitstream)
                    
                    if ip:
                        del bitstream[:ip.header_size]
                        layers.append(ip)
                        
                        transport = ip.switch(bitstream)
                        
                        if transport:
                            del bitstream[:transport.header_size]
                            layers.append(transport)

                            #data=transport.switch(bitstream)

            yield layers
