from scapy.all import IP, ICMP, send

src_ip = "192.168.1.48"
dst_ip =  "127.1.1"

packet = IP(src=src_ip, dst=dst_ip, ttl=128) / ICMP() / "HelloWorld"
while True:
    send(packet)

print(f"Sent ICMP packet from {src_ip} to {dst_ip}")

