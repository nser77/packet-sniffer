import socket
import binascii
import bitstring

class Sniffer:
    def sliceEthernetFrame(self, bitstream):
        dst_mac=binascii.hexlify(bitstream[:48].bytes, ':')
        src_mac=binascii.hexlify(bitstream[48:96].bytes, ":")
        ether_type=binascii.hexlify(bitstream[96:112].bytes)
        
        ethernet_frame = EthernetFrame(dst_mac, src_mac, ether_type)

        return ethernet_frame

    def sliceIpv4Packet(self, raw):
        pass

    def start(self):
        conn = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            bitstream=bitstring.BitStream(raw)
            #bitstream.pp('bin, hex', width=100)
            
            ethernet_frame, ether_type = self.sliceEthernetFrame(bitstream)
            
            ip_version=bitstream[112:116].int
            ip_ihl=bitstream[116:120].int
            ip_tos=bitstream[120:128].int
            #ip_dscp=bitstream[123:128].int
            ip_total_length=bitstream[128:144].uint
            ip_id=bitstream[144:160].uint
            ip_flag_0=bitstream[160:161].int
            ip_flag_1=bitstream[161:162].int
            ip_flag_2=bitstream[162:163].int
            ip_fragment_offset=bitstream[163:176].uint
            ip_ttl=bitstream[176:184].int
            ip_protocol=bitstream[184:192].int
            ip_checksum=bitstream[192:208].uint
            ip_src=bitstream[208:240].bytes
            ip_dst=bitstream[240:272].bytes
            h_ip_src=".".join(map(str, ip_src))
            h_ip_dst=".".join(map(str, ip_dst))

            if ethernet_frame.ether_type == 'ipv4':
                print(ip_version, ip_ihl, ip_tos, ip_total_length,
                      ip_id, ip_flag_0, ip_flag_1, ip_flag_2, ip_fragment_offset,
                      ip_ttl, ip_protocol, ip_checksum,
                      h_ip_src, h_ip_dst)


    def output(self, layers):
        pass


sniffer=Sniffer()
sniffer.start()
