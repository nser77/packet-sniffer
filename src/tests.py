from json import dumps

from sniffer import Sniffer

try:
    sniffer=Sniffer()

    for packet in sniffer.start():
        if len(packet) >= 3:
            if packet[1].protocol == 112:
                 print(packet)

            frame = dumps(packet[0].__dict__)
            ip = dumps(packet[1].__dict__)
            transport = dumps(packet[2].__dict__)

            print(frame,ip,transport)

except KeyboardInterrupt:
    print("\n")


