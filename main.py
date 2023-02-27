import socket
import struct
import binascii

class Sniffer:
    def sliceEtherFrame(self, raw):
        ether_frame = EthernetFrame(raw[0:14])
        next = raw[14:]

        return ether_frame, next

    def sliceIpv4Packet(self, raw):
        version_header_len = raw[0]
        version = version_header_len >> 4
        header_len = (version_header_len & 15) * 4
        
        ipv4_packet = Ipv4Packet(raw)
        next = raw[header_len:]

        return ipv4_packet, next

    def sliceIpv4IcmpPacket(self, raw):
        ipv4_icmp_packet = Ipv4IcmpPacket(raw[:4])
        next = raw[4:]

        return ipv4_icmp_packet, next

    def sliceIpv4TcpPacket(self, raw):
        ipv4_tcp_packet = Ipv4TcpPacket(raw)
        next = raw[24:]

        return ipv4_tcp_packet, next

    def start(self):
        conn = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            layers = []

            ether_frame, raw_ip_packet = self.sliceEtherFrame(raw)
            layers.append(ether_frame)

            if ether_frame.ether_type == 'ipv4':
                ip_packet, raw_transport_packet = self.sliceIpv4Packet(raw_ip_packet)
                layers.append(ip_packet)
                
    def output(self, layers):
        pass
