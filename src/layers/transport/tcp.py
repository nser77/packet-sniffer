from bitstring import BitStream

class Tcp(object):
    with_options=False
    options_bits=0

    def __init__(self, bitstream):
        self.setSrcPort(              bitstream[272:288])
        self.setDstPort(              bitstream[288:304])
        self.setSequenceNumber(       bitstream[304:336])
        self.setAcknowledgmentNumber( bitstream[336:368])
        self.setDataOffset(           bitstream[368:372])
        self.setReserved(             bitstream[372:376])
        self.setCwr(                  bitstream[376:377])
        self.setEce(                  bitstream[377:388])
        self.setUrg(                  bitstream[388:389])
        self.setAck(                  bitstream[389:390])
        self.setPsh(                  bitstream[390:391])
        self.setRst(                  bitstream[391:392])
        self.setSyn(                  bitstream[392:393])
        self.setFin(                  bitstream[393:394])
        self.setWindowSize(           bitstream[394:410])

    def setSrcPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.src_port=bitstream.uint

    def setDstPort(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.dst_port=bitstream.uint

    def setSequenceNumber(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.sequence_number=bitstream.uint

    def setAcknowledgmentNumber(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.acknowledgment_number=bitstream.uint

    def setDataOffset(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.data_offset=bitstream.uint

    def setReserved(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.reserved=bitstream.uint

    def setCwr(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.cwr=bitstream.int

    def setEce(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ece=bitstream.int

    def setUrg(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.urg=bitstream.int

    def setAck(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ack=bitstream.int

    def setPsh(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.psh=bitstream.int

    def setRst(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.rst=bitstream.int

    def setSyn(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.syn=bitstream.int

    def setFin(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.fin=bitstream.int

    def setWindowSize(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.window_size=bitstream.uint
