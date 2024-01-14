from scapy.all import *

# Función para realizar OS Fingerprinting
def os_fingerprinting(target_ip):
    # Envío de paquete ICMP Echo Request
    packet = IP(dst=target_ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)

    # Análisis de la respuesta recibida
    if response:
        if response.ttl <= 64:
            print("Probablemente es un sistema operativo basado en Unix (Linux, macOS, etc.)")
        else:
            print("Probablemente es un sistema operativo basado en Windows")
    else:
        print("No se recibió respuesta")

# Dirección IP del dispositivo objetivo
target_ip = "192.168.93.135"

# Llamada a la función de OS Fingerprinting
os_fingerprinting(target_ip)