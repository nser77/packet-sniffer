"""
        https://www.rfc-editor.org/rfc/rfc1035
"""

from bitstring import BitStream
import binascii

class Dns(object):
    header_size=0

    def __init__(self, bitstream):
        self.setHeaderFlags(    bitstream[0:96])
        self.setQuestions(      bitstream[96:176])
        self.setResources(      bitstream[176:256])

    def setHeaderFlags(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.setIdentification( bitstream[0:16])
            self.setQr(             bitstream[16:17])
            self.setOpcode(         bitstream[17:21])
            self.setAa(             bitstream[21:22])
            self.setTc(             bitstream[22:23])
            self.setRd(             bitstream[23:24])
            self.setRa(             bitstream[24:25])
            self.setZ(              bitstream[25:28])
            self.setRcode(          bitstream[28:32])
            self.setQdCount(        bitstream[32:48])
            self.setAnCount(        bitstream[48:64])
            self.setNsCount(        bitstream[64:80])
            self.setArCount(        bitstream[80:96])

    def setIdentification(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.identification=bitstream.uint
            self.header_size += 16

    def setQr(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.qr=bitstream.uint
            self.header_size += 1

    def setOpcode(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.opcode=bitstream.uint
            self.header_size += 4

    def setAa(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.aa=bitstream.uint
            self.header_size += 1

    def setTc(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.tc=bitstream.uint
            self.header_size += 1

    def setRd(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.rd=bitstream.uint
            self.header_size += 1

    def setRa(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ra=bitstream.uint
            self.header_size += 1

    def setZ(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.z=bitstream.uint
            self.header_size += 3

    def setRcode(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.rcode=bitstream.uint
            self.header_size += 4

    def setQdCount(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.qd_count=bitstream.uint
            self.header_size += 16

    def setAnCount(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.an_count=bitstream.uint
            self.header_size += 16

    def setNsCount(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ns_count=bitstream.uint
            self.header_size += 16

    def setArCount(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.ar_count=bitstream.uint
            self.header_size += 16

    def setQuestions(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.setQname(  bitstream[0:48])
            self.setQtype(  bitstream[48:64])
            self.setQclass( bitstream[64:80])

    def setQname(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.qname=bitstream.uint
            self.header_size += 48

    def setQtype(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.qtype=bitstream.uint
            self.header_size += 16

    def setQclass(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.qclass=bitstream.uint
            self.header_size += 16

    def setResources(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.setName(  bitstream[0:16])
            self.setType(  bitstream[16:32])

    def setName(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.Name=bitstream.uint
            self.header_size += 16

    def setType(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.type=bitstream.uint
            self.header_size += 16
