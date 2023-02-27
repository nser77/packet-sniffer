import struct
import binascii

class EthernetFrame(object):
    _format_string_="! 6s 6s H"

    def __init__(self, raw=None):
        try:
            size=struct.calcsize(self._format_string_)
            dst_mac, src_mac, ether_type = struct.unpack(self._format_string_, raw[:size])
        except:
            # 802.1Q (VLAN) exception tag
            self._format_string_="! 6s 6s i H"
            size=struct.calcsize(self._format_string_)
            dst_mac, src_mac, dot1q, ether_type = struct.unpack(self._format_string_, raw[:size])
            self.dot1q=dot1q

        self.dst_mac=binascii.hexlify(dst_mac)
        self.src_mac=binascii.hexlify(src_mac)
        self.ether_type=hex(ether_type)

    def getEtherType(self, hex_ether_type):
        match hex_ether_type:
            case '0x800':
                ether_type='ipv4'
            case '0x806':
                ether_type='arp'
            case '0x86dd':
                ether_type='ipv6'

        return ether_type
