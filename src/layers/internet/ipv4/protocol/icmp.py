"""
        https://datatracker.ietf.org/doc/html/rfc792
"""

from bitstring import BitStream

class IcmpBase(object):
    header_size=0

    def __init__(self, bitstream):
        self.setType(      bitstream[0:8])
        self.setCode(      bitstream[8:16])
        self.setChecksum(  bitstream[16:32])

    def setType(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.type=bitstream.uint
            self.header_size += 8

    def setCode(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.code=bitstream.int
            self.header_size += 8

    def setChecksum(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.checksum=bitstream.bin
            self.header_size += 16

class IcmpType5(IcmpBase):
    def setGatewayInternetAddress(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.gateway_internet_address=bitstream.uint
            self.header_size += 32

class IcmpType8Type0(IcmpBase):
    def setIdentifier(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.identifier=bitstream.uint
            self.header_size += 16

    def setSequenceNumber(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.sequence_number=bitstream.uint
            self.header_size += 16

class Icmp(IcmpType5, IcmpType8Type0):
    def next(self, bitstream):
        if self.type == 8 or self.type == 0:
            if self.code == 0:
                self.setIdentifier(     bitstream[0:16])
                self.setSequenceNumber( bitstream[16:32])
        if self.type == 5:
            self.setGatewayInternetAddress(bitstream[0:32])

        return False
