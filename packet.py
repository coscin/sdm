
import os
import logging
import socket
import sys
import errno


import collections
import logging

from scapy.all import *

all_pkts = collections.OrderedDict()

def gen_report_packet():
    pkt = PacketList()
    hdr = Ether(type=0x88, src="11:22:33:44:55:66", dst="77:88:99:aa:bb:cc") / IP(src="10.0.0.1", dst="10.0.0.2")
    data = bytearray(os.urandom(random.randint(0, 10)))
    pkt.append(hdr/Raw(data))
    all_pkts['reportcard'] = pkt

if __name__ == "__main__":
    gen_report_packet()
    for k, v in all_pkts.iteritems():
        wrpcap("%s.pcap" % k, v)
