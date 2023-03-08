"""
    https://datatracker.ietf.org/doc/html/rfc768
"""

from bitstring import BitStream

from layers.application.dns import Dns

class Udp(object):
    header_size=0
    header_options=False
    header_options_size=288

    def __init__(self, bitstream):
        self.setSrcPort(              bitstream[:16])
        self.setDstPort(              bitstream[16:32])

    def setSrcPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.src_port=bitstream.uint
            self.header_size += 16

    def setDstPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.dst_port=bitstream.uint
            self.header_size += 16

    def next(self, bitstream):
        return False
