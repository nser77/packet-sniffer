import binascii

class EthernetFrame(object):
    def __init__(self, bytes_dst_mac, bytes_src_mac, bytes_ether_type):
        self.setDstMac(bytes_dst_mac)
        self.setSrcMac(bytes_src_mac)
        self.setEtherType(bytes_ether_type)

    def setDstMac(self, bytes_dst_mac):
        self.dst_mac=binascii.hexlify(bytes_dst_mac, ":")
        return True

    def setSrcMac(self, bytes_src_mac):
        self.src_mac=binascii.hexlify(bytes_src_mac, ":")
        return True

    def setEtherType(self, bytes_ether_type):
        match bytes_ether_type.hex():
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
