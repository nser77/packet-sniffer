from binascii import hexlify
from bitstring import BitStream

class EthernetFrame(object):
    header_size=0
    footer_size=0

    def __init__(self, bitstream):
        self.setDstMac(    bitstream[:48])
        self.setSrcMac(    bitstream[48:96])
        self.setEtherType( bitstream[96:112])
        self.setFcs(       bitstream[:-32])

    def setDstMac(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.dst_mac=hexlify(bitstream.bytes, ":")
            self.header_size += 48

    def setSrcMac(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.src_mac=hexlify(bitstream.bytes, ":")
            self.header_size += 48

    def setEtherType(self, bitstream):
        if isinstance(bitstream, BitStream):
            match bitstream.hex:
                case '0800':
                    self.ether_type='ipv4'
                case '0806':
                    self.ether_type='arp'
                case '086dd':
                    self.ether_type='ipv6'

            self.header_size += 16

    def setFcs(self, bitstream):
       self.footer_size += 32
