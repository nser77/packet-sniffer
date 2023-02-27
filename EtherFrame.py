class EthernetFrame(object):
    def __init__(self, raw=None):
        _format_string_="!6s6sH"

        self.ip_header=struct.unpack(_format_string_, raw)
        self.dst_mac=binascii.hexlify(self.ip_header[0])
        self.src_mac=binascii.hexlify(self.ip_header[1])
        self.raw_ether_type=self.ip_header[2]
        self.hex_ether_type, self.ether_type = self.getEtherType(self.raw_ether_type)

    def getEtherType(self, raw_ether_type):
        hex_ether_type=hex(raw_ether_type)
        ether_type=None

        match hex_ether_type:
            case '0x800':
                ether_type='ipv4'
            case '0x806':
                ether_type='arp'
            case '0x86dd':
                ether_type='ipv6'

        return hex_ether_type, ether_type
