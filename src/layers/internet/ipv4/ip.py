from bitstring import BitStream

class Ip(object):
    header_size=0
    header_options=False
    header_options_size=288

    def __init__(self, bitstream):
        self.setVersion(        bitstream[:4])
        self.setIhl(            bitstream[4:8])
        self.setTos(            bitstream[8:16])
        self.setTotalLength(    bitstream[16:32])
        self.setIdentification( bitstream[32:48])
        self.setFlag0(          bitstream[48:49])
        self.setFlag1(          bitstream[49:50])
        self.setFlag2(          bitstream[50:51])
        self.setFragmentOffset( bitstream[51:64])
        self.setTtl(            bitstream[64:72])
        self.setProtocol(       bitstream[72:80])
        self.setHeaderChecksum( bitstream[80:96])
        self.setSrc(            bitstream[96:128])
        self.setDst(            bitstream[128:160])

        if self.ihl > 5 and self.ihl <= 15:
             self.header_options=True
             self.setOptions(bitstream[160:self.header_options_size])

    def setVersion(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.version=bitstream.int
            self.header_size += 4

    def setIhl(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ihl=bitstream.int
            self.header_size += 4

    def setTos(self, bitstream):
        # not implemented yet
        if isinstance(bitstream, BitStream):
            self.tos=bitstream.int
            self.header_size += 8

    def setTotalLength(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.total_length=bitstream.uint
            self.header_size += 16

    def setIdentification(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.identification=bitstream.uint
            self.header_size += 16

    def setFlag0(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.flag0=bitstream.int
            self.header_size += 1

    def setFlag1(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.flag1=bitstream.int
            self.header_size += 1

    def setFlag2(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.flag2=bitstream.int
            self.header_size += 1

    def setFragmentOffset(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.fragment_offset=bitstream.uint
            self.header_size += 13

    def setTtl(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ttl=bitstream.int
            self.header_size += 8

    def setProtocol(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.protocol=bitstream.int
            self.header_size += 8

    def setHeaderChecksum(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.header_checksum=bitstream.uint
            self.header_size += 16

    def setSrc(self, bitstream):
        if isinstance(bitstream, BitStream):
           self.src=".".join(map(str, bitstream.bytes))
           self.header_size += 32

    def setDst(self, bitstream):
        if isinstance(bitstream, BitStream):
           self.dst=".".join(map(str, bitstream.bytes))
           self.header_size += 32

    def setOptions(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.options=bitstream.uint
            self.header_size += self.header_options_size