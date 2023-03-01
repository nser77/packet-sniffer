from binascii import hexlify
from bitstring import BitStream

class Frame(object):
    header_size=0
    footer_size=0

    def __init__(self, bitstream):
        self.setDstMac(    bitstream[:48])
        self.setSrcMac(    bitstream[48:96])
        self.setEtherType( bitstream[96:112])
        self.setFcs(       bitstream[:-32])

    def setDstMac(self, bitstream):
        if isinstance(bitstream, BitStream):
            dst_mac=hexlify(bitstream.bytes, ":")
            self.dst_mac=dst_mac.decode('utf-8')
            self.header_size += 48

    def setSrcMac(self, bitstream):
        if isinstance(bitstream, BitStream):
            src_mac=hexlify(bitstream.bytes, ":")
            self.src_mac=src_mac.decode('utf-8')
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
                case _:
                    self.ether_type=None

            self.header_size += 16

    def setFcs(self, bitstream):
       self.footer_size += 32

    def switch(self, bitstream):
        pass
