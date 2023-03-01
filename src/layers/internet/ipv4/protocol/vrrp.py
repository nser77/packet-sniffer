from bitstring import BitStream

class Vrrp(object):
    header_size=0

    def __init__(self, bitstream):
        self.setVersion(                         bitstream[0:4])
        self.setType(                            bitstream[4:8])
        self.setVirtualRouterId(                 bitstream[8:16])
        self.setPriority(                        bitstream[16:24])
        self.setCountIpvxAddr(                   bitstream[24:32])
        self.setReserved(                        bitstream[32:36])
        self.setMaxAdvertisementInterval(        bitstream[36:48])
        self.setChecksum(                        bitstream[48:64], True)

    def setVersion(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.version=bitstream.int
            self.header_size += 4

    def setType(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.type=bitstream.int
            self.header_size += 4

    def setVirtualRouterId(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.virtual_router_id=bitstream.int
            self.header_size += 8

    def setPriority(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.priority=bitstream.uint
            self.header_size += 8

    def setCountIpvxAddr(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.count_ipvx_addr=bitstream.uint
            self.header_size += 8

    def setReserved(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.reserved=bitstream.int
            self.header_size += 4

    def setMaxAdvertisementInterval(self, bitstream):
        if isinstance(bitstream, BitStream):
            self.max_advertisement_interval_c=bitstream.uint
            self.header_size += 12

    def setChecksum(self, bitstream, skip=False):
        if isinstance(bitstream, BitStream):
            if not skip:
                self.checksum=bitstream.uint
            self.header_size += 16