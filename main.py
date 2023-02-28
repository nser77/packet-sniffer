import socket
import binascii
import bitstring

class EthernetFrame(object):
    def __init__(self, bitstream):
        self.setDstMac(    bitstream[:48])
        self.setSrcMac(    bitstream[48:96])
        self.setEtherType( bitstream[96:112])
        #self.setFcs(      bitstream[:-32])

    def setDstMac(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            self.dst_mac=binascii.hexlify(bitstream.bytes, ":")

    def setSrcMac(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            self.src_mac=binascii.hexlify(bitstream.bytes, ":")

    def setEtherType(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            match bitstream.hex:
                case '0800':
                    self.ether_type='ipv4'
                case '0806':
                    self.ether_type='arp'
                case '086dd':
                    self.ether_type='ipv6'

class Ipv4Packet(object):
    def __init__(self, bitstream):
        self.setVersion(        bitstream[112:116])
        self.setIhl(            bitstream[116:120])
        self.setTos(            bitstream[120:128])
        self.setTotalLength(    bitstream[128:144])
        self.setIdentification( bitstream[144:160])

    def setVersion(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            self.version=bitstream.int

    def setIhl(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            self.ihl=bitstream.int

    def setTos(self, bitstream):
        # not implemented yet
        if isinstance(bitstream, bitstring.BitStream):
            self.tos=bitstream.int

    def setTotalLength(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            self.total_length=bitstream.uint

    def setIdentification(self, bitstream):
        if isinstance(bitstream, bitstring.BitStream):
            self.identification=bitstream.uint

class Sniffer:
    def start(self):
        conn = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

        while True:
            raw, addr = conn.recvfrom(65536)

            bitstream=bitstring.BitStream(raw)

            print('-----------------------')
            print('--- Ethernet frame --- ')
            ethernet_frame = EthernetFrame(bitstream)
            print(ethernet_frame.dst_mac, ethernet_frame.src_mac, ethernet_frame.ether_type)
            print('--- Ip Packet ---')
            ipv4_packet=Ipv4Packet(bitstream)
            print(ipv4_packet.version, ipv4_packet.ihl, ipv4_packet.total_length, ipv4_packet.identification)

    def output(self, layers):
        pass

try:
    sniffer=Sniffer()
    sniffer.start()
except KeyboardInterrupt:
    print("\n")
