import os
import logging
import socket
import sys
import errno

from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
from twisted.internet.task import LoopingCall
from twisted.python import log

from scapy.all import *



class LinkUtilProbe(DatagramProtocol):
    '''
    build a special mac frame to communicate link utilization
    with controller
    '''
    def __init__(self):
        self.rate = 1
        self.hdr = Ether(type=0x808, src="11:22:33:44:55:66", dst="ff:ff:ff:ff:ff:ff") 
        self.data = "\x06\x07\x08"

    def construct(self):
        pkt = PacketList()
        pkt.append(hdr/Raw(data))

    def start(self):
        self._call = LoopingCall(self.reportUtil)
        self._loop = self._call.start(self.rate)

    def reportUtil(self):
        print "report utilization"
        pass

if __name__ == "__main__":
    probe = LinkUtilProbe()
    probe.start()
    reactor.listenUDP(1000, probe)
    reactor.run()
