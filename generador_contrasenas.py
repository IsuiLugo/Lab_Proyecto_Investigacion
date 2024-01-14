import random
import string

def generar_usuario():
    nombre_base = "usuario"
    numero = random.randint(1, 1000)
    return f"{nombre_base}{numero}"

def generar_contrasena(longitud=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for i in range(longitud))

def generar_credenciales(num_credenciales=500):
    credenciales = []
    for _ in range(num_credenciales):
        usuario = generar_usuario()
        contrasena = generar_contrasena()
        credenciales.append((usuario, contrasena))
    return credenciales

def guardar_credenciales_en_archivo(credenciales, archivo="credenciales.txt"):
    with open(archivo, 'w') as file:
        for usuario, contrasena in credenciales:
            file.write(f"{usuario} {contrasena}\n")

# Generar las credenciales
credenciales = generar_credenciales()

# Guardarlas en un archivo
guardar_credenciales_en_archivo(credenciales)
