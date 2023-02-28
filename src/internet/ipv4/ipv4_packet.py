from bitstring import BitStream

class Ipv4Packet(object):
    def __init__(self, bitstream):
        self.setVersion(        bitstream[112:116])
        self.setIhl(            bitstream[116:120])
        self.setTos(            bitstream[120:128])
        self.setTotalLength(    bitstream[128:144])
        self.setIdentification( bitstream[144:160])

    def setVersion(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.version=bitstream.int

    def setIhl(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ihl=bitstream.int

    def setTos(self, bitstream):
        # not implemented yet
        if isinstance(bitstream, BitStream):
            self.tos=bitstream.int

    def setTotalLength(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.total_length=bitstream.uint

    def setIdentification(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.identification=bitstream.uint
