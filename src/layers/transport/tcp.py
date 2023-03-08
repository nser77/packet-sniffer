"""
    https://datatracker.ietf.org/doc/html/rfc793
"""

from bitstring import BitStream

class Tcp(object):
    header_size=0
    header_options=False
    header_options_size=288

    def __init__(self, bitstream):
        self.setSrcPort(              bitstream[:16])
        self.setDstPort(              bitstream[16:32])
        self.setSequenceNumber(       bitstream[32:64])
        self.setAcknowledgmentNumber( bitstream[64:96])
        self.setDataOffset(           bitstream[96:100])
        self.setReserved(             bitstream[100:104])
        self.setCwr(                  bitstream[104:105])
        self.setEce(                  bitstream[105:106])
        self.setUrg(                  bitstream[106:107])
        self.setAck(                  bitstream[107:108])
        self.setPsh(                  bitstream[108:109])
        self.setRst(                  bitstream[109:110])
        self.setSyn(                  bitstream[110:111])
        self.setFin(                  bitstream[111:112])
        self.setWindowSize(           bitstream[112:128])
        self.setChecksum(             bitstream[128:144])
        self.setUrgentPointer(        bitstream[144:160])

        if self.data_offset > 5:
            self.header_options=True
            self.setOptions(bitstream[160:self.header_options_size])

    def setSrcPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.src_port=bitstream.uint
            self.header_size += 16

    def setDstPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.dst_port=bitstream.uint
            self.header_size += 16

    def setSequenceNumber(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.sequence_number=bitstream.uint
            self.header_size += 32

    def setAcknowledgmentNumber(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.acknowledgment_number=bitstream.uint
            self.header_size += 32

    def setDataOffset(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.data_offset=bitstream.uint
            self.header_size += 4

    def setReserved(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.reserved=bitstream.int
            self.header_size += 4

    def setCwr(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.cwr=bitstream.uint
            self.header_size += 1

    def setEce(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ece=bitstream.uint
            self.header_size += 1

    def setUrg(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.urg=bitstream.uint
            self.header_size += 1

    def setAck(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ack=bitstream.uint
            self.header_size += 1

    def setPsh(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.psh=bitstream.uint
            self.header_size += 1

    def setRst(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.rst=bitstream.uint
            self.header_size += 1

    def setSyn(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.syn=bitstream.uint
            self.header_size += 1

    def setFin(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.fin=bitstream.uint
            self.header_size += 1

    def setWindowSize(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.window_size=bitstream.uint
            self.header_size += 16

    def setChecksum(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.checksum=bitstream.bin
            self.header_size += 16

    def setUrgentPointer(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.urgent_pointer=bitstream.uint
            self.header_size += 16

    def setOptions(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.options=bitstream.uint
            self.header_size += self.header_options_size

    def next(self, bitstream):
        pass
