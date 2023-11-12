from scapy.all import IP, TCP, send, sr1 , 
import random 

while True :
    source_ip = "192.168.1.48"
    destination_ip = "192.168.1.50"
    source_port = random.randint(1,100000)
    destination_port = 80
    ip_packet = IP(src=source_ip, dst=destination_ip)
    tcp_packet = TCP(sport=source_port, dport=destination_port)
    initial_packet = ip_packet / tcp_packet
    response_packet = sr1(initial_packet)
    
