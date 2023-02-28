from bitstring import BitStream

class Ipv4Packet(object):
    with_options=False
    options_bits=0

    def __init__(self, bitstream):
        self.setVersion(        bitstream[112:116])
        self.setIhl(            bitstream[116:120])
        self.setTos(            bitstream[120:128])
        self.setTotalLength(    bitstream[128:144])
        self.setIdentification( bitstream[144:160])
        self.setFlag0(          bitstream[160:161])
        self.setFlag1(          bitstream[161:162])
        self.setFlag2(          bitstream[162:163])
        self.setFragmentOffset( bitstream[163:176])
        self.setTtl(            bitstream[176:184])
        self.setProtocol(       bitstream[184:192])
        self.setHeaderChecksum( bitstream[192:208])
        self.setSrc(            bitstream[208:240])
        self.setDst(            bitstream[240:272])

        if self.ihl > 5 and self.ihl <= 15:
             self.with_options=True
             self.options_bits=288
             self.setOptions(bitstream[272:self.options_bits])

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

    def setFlag0(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.flag0=bitstream.int

    def setFlag1(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.flag1=bitstream.int

    def setFlag2(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.flag2=bitstream.int

    def setFragmentOffset(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.fragment_offset=bitstream.uint

    def setTtl(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ttl=bitstream.int

    def setProtocol(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.protocol=bitstream.int

    def setHeaderChecksum(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.header_checksum=bitstream.uint

    def setSrc(self, bitstream):
        if isinstance(bitstream, BitStream):
           self.src=".".join(map(str, bitstream.bytes))

    def setDst(self, bitstream):
        if isinstance(bitstream, BitStream):
           self.dst=".".join(map(str, bitstream.bytes))

    def setOptions(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.options=bitstream.uint
