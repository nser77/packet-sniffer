"""
    https://datatracker.ietf.org/doc/html/rfc768
"""

from bitstring import BitStream

from layers.application.dns import Dns

class Udp(object):
    header_size=0

    def __init__(self, bitstream):
        self.setSrcPort(              bitstream[:16])
        self.setDstPort(              bitstream[16:32])
        self.setLength(               bitstream[32:48])
        self.setChecksum(             bitstream[48:64])

    def setSrcPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.src_port=bitstream.uint
            self.header_size += 16

    def setDstPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.dst_port=bitstream.uint
            self.header_size += 16

    def setLength(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.length=bitstream.uint
            self.header_size += 16

    def setChecksum(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.checksum=bitstream.bin
            self.header_size += 16

    def next(self, bitstream):
        if self.src_port == 53 or self.dst_port == 53:
            return Dns(bitstream)
        return False
