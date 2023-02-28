import binascii

class EthernetFrame(object):
    def __init__(self, dst_mac, src_mac, ether_type):
        self.setDstMac(dst_mac)
        self.setSrcMac(src_mac)
        self.setEtherType(ether_type)

    def setDstMac(self, byte_dst_mac):
        self.dst_mac=binascii.hexlify(byte_dst_mac, ":")
        return True

    def setSrcMac(self, byte_src_mac):
        self.src_mac=binascii.hexlify(byte_src_mac, ":")
        return True

    def setEtherType(self, byte_ether_type):
        match byte_ether_type.hex():
            case '0800':
                ether_type='ipv4'
            case '0806':
                ether_type='arp'
            case '086dd':
                ether_type='ipv6'
            case _:
                ether_type=None

        self.ether_type=ether_type
        return True

    def getEtherType(self):
        return self.ether_type
