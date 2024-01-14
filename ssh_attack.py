import paramiko
import time

def connect_ssh(host, port, username, password):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=host, port=port, username=username, password=password)
            print(f"Conexión exitosa a {host} con usuario {username}")
            return ssh_client
        except paramiko.AuthenticationException:
            print(f"Autenticación fallida para {username} en {host}")
            return None
        except paramiko.SSHException as e:
            if "Error reading SSH protocol banner" in str(e) and attempt < max_retries - 1:
                print(f"Reintentando conexión a {host} con usuario {username} (intento {attempt + 1})")
                time.sleep(5)  # Esperar 5 segundos antes de reintentar
            else:
                print(f"Error al conectar a {host} con usuario {username}: {e}")
                return None
        except Exception as e:
            print(f"Error al conectar a {host} con usuario {username}: {e}")
            return None

# Configuración del servidor SSH
host = "192.168.93.135"
port = 22  # Puerto SSH, por defecto es el 22

# Leer las credenciales desde un archivo
ruta_archivo_credenciales = "/home/isui/tesis/programas/credenciales.txt"
ssh_client = None

with open(ruta_archivo_credenciales, "r") as file:
    for line in file:
        username, password = line.strip().split()  # Asegúrate de que el archivo tiene el formato correcto
        ssh_client = connect_ssh(host, port, username, password)
        if ssh_client:
            break  # Salir del bucle si la conexión es exitosa

# No olvides cerrar la conexión cuando termines
if ssh_client:
    ssh_client.close()