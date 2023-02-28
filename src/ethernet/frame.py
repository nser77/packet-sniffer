from binascii import hexlify
from bitstring import BitStream

class EthernetFrame(object):
    def __init__(self, bitstream):
        self.setDstMac(    bitstream[:48])
        self.setSrcMac(    bitstream[48:96])
        self.setEtherType( bitstream[96:112])
        #self.setFcs(      bitstream[:-32])

    def setDstMac(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.dst_mac=hexlify(bitstream.bytes, ":")

    def setSrcMac(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.src_mac=hexlify(bitstream.bytes, ":")

    def setEtherType(self, bitstream):
        if isinstance(bitstream, BitStream):
            match bitstream.hex:
                case '0800':
                    self.ether_type='ipv4'
                case '0806':
                    self.ether_type='arp'
                case '086dd':
                    self.ether_type='ipv6'
