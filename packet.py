
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
    hdr = Ether(type=0x808, src="a0:36:9f:51:2c:3a", dst="ff:ff:ff:ff:ff:ff") 
    data = "\x06\x07\x08"
    pkt.append(hdr/Raw(data))
    all_pkts['reportcard'] = pkt

if __name__ == "__main__":
    gen_report_packet()
    for k, v in all_pkts.iteritems():
        sendp(v, iface="eth5", loop=300,inter=60)
