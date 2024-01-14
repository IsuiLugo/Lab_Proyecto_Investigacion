import pyshark
import json
import sys

def packet_to_dict(packet):
    # Crear un diccionario para almacenar la información del paquete
    packet_dict = {}
    # Extraer información de capas comunes
    for layer in packet.layers:
        layer_name = layer.layer_name
        packet_dict[layer_name] = {}
        for field_name, field_value in layer._all_fields.items():
            packet_dict[layer_name][field_name] = field_value

    return packet_dict

def convert_pcap_to_json(pcap_file, json_file):
    cap = pyshark.FileCapture(pcap_file)

    packets_json = [packet_to_dict(packet) for packet in cap]

    with open(json_file, 'w') as outfile:
        json.dump(packets_json, outfile)

    print(f"Archivo {json_file} generado con éxito.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 convert_tcp_dumb_to_json.py <archivo.pcap>")
        sys.exit(1)

    pcap_path = sys.argv[1]
    json_path = pcap_path + '.json'

    convert_pcap_to_json(pcap_path, json_path)