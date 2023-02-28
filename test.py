from sniffer import Sniffer

sniffer=Sniffer()
    
for packet in sniffer.start():
    if len(packet) >= 2:
        # getting 'src_mac' ethernet frame field
        print(packet[0].src_mac)
        
        # gettig 'version' ip packet field
        print(packet[1].version)

