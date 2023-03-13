from sniffer import Sniffer
from output.output import Output
from output.type import OutputType

try:
    sniffer=Sniffer('eth0')
    for packet in sniffer.start(10):
        if packet:
            Output.cli(OutputType.json(packet))
            Output.redis("vrrp", OutputType.json(packet))
except KeyboardInterrupt:
    print("\n")
