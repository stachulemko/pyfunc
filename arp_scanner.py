from scapy.all import *
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Ustal docelowy adres IP
dst_ip = "192.168.1.1"

# Przeskanuj zakres portów od 1 do 65535
for dst_port in range(1, 65536):
    # Tworzenie pakietu TCP SYN (nawiązanie połączenia)
    syn_packet = IP(dst=dst_ip) / TCP(dport=dst_port, flags="S")

    # Wysłanie pakietu i oczekiwanie na odpowiedź
    response_packet = sr1(syn_packet, timeout=1, verbose=0)

    # Jeśli otrzymaliśmy odpowiedź (TCP SYN-ACK), możemy wysłać trzeci pakiet, aby nawiązać połączenie
    if response_packet and response_packet.haslayer(TCP) and response_packet[TCP].flags == "SA":
        # Tworzenie pakietu TCP ACK (potwierdzenie nawiązania połączenia)
        ack_packet = IP(dst=dst_ip) / TCP(dport=dst_port, sport=response_packet[TCP].dport,
                                          seq=response_packet[TCP].ack, ack=response_packet[TCP].seq + 1, flags="A")

        # Wysłanie pakietu ACK
        send(ack_packet, verbose=0)

        print(f"Port {dst_port} is open")

print("Skanowanie zakończone.")
