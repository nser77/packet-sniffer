from sniffer import Sniffer

sniffer=Sniffer()
    
for packet in sniffer.start():
    if len(packet) >= 2:
        print(packet[1].version)
