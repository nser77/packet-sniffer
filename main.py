import socket
import binascii
import bitstring

class Sniffer:
    def sliceEthernetFrame(self, bitstream):
        dst_mac=binascii.hexlify(bitstream[:48].bytes, ':')
        src_mac=binascii.hexlify(bitstream[48:96].bytes, ":")
        ether_type=binascii.hexlify(bitstream[96:112].bytes)
        
        ethernet_frame = EthernetFrame(dst_mac, src_mac, ether_type)

        return ethernet_frame, ether_type

    def sliceIpv4Packet(self, raw):
        ipv4_packet = Ipv4Packet(raw)
        next = raw[ipv4_packet.size:]

        return ipv4_packet, next

    def start(self):
        conn = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            bitstream=bitstring.BitStream(raw)
            #bitstream.pp('bin, hex', width=100)
            
            ethernet_frame, ether_type = self.sliceEthernetFrame(bitstream)
            
            ip_version=bitstream[112:116].int
            ip_ihl=bitstream[116:120].int

            print(dst_mac, src_mac, ether_type, ip_version, ip_ihl)

    def output(self, layers):
        pass


sniffer=Sniffer()
sniffer.start()
