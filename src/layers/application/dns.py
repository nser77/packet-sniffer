from bitstring import BitStream

class Dns(object):
    header_size=0

    def __init__(self, bitstream):
        self.setIdentification( bitstream[0:16])

    def setIdentification(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.identification=bitstream.uint
            self.header_size += 16
