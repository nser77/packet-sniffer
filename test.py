from sniffer import Sniffer

sniffer=Sniffer()
    
for packet in sniffer.start():
    if len(packet) >= 2:
        # gettig 'version' ip packet field
        print(packet[1].version)
        print(packet[0].src_mac)
