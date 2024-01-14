import json
import re
import sys
import os

def parse_snort_alert_line(line):
    pattern = r"(\d{2}/\d{2}-\d{2}:\d{2}:\d{2}.\d{6})  \[\*\*\] \[(\d+:\d+:\d+)\] (.+?) \[\*\*\] \[Priority: (\d+)\] {(\w+)} (\d+\.\d+\.\d+\.\d+)(?::(\d+))? -> (\d+\.\d+\.\d+\.\d+)(?::(\d+))?"
    match = re.match(pattern, line)
    if match:
        return {
            "marca_temporal": match.group(1),
            "id_sid": match.group(2),
            "descripcion": match.group(3),
            "prioridad": int(match.group(4)),
            "protocolo": match.group(5),
            "ip_origen": match.group(6),
            "puerto_origen": int(match.group(7)) if match.group(7) else None,
            "ip_destino": match.group(8),
            "puerto_destino": int(match.group(9)) if match.group(9) else None
        }
    else:
        return None

def convert_snort_to_json(filename, output_filename):
    alerts = []
    alert_count = 0
    with open(filename, "r") as file:
        for line in file:
            alert = parse_snort_alert_line(line)
            if alert:
                alerts.append(alert)
                alert_count += 1
    
    with open(output_filename, "w") as outfile:
        json.dump(alerts, outfile, indent=4)

    return alert_count

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 convert.py <archivo_snort_alert>")
        sys.exit(1)

    input_filename = sys.argv[1]
    base_filename = os.path.splitext(os.path.basename(input_filename))[0]
    output_filename = f"{base_filename}_alertas.json"

    alert_count = convert_snort_to_json(input_filename, output_filename)
    print(f"Archivo JSON guardado como: {output_filename}")
    print(f"Número total de alertas detectadas: {alert_count}")

if __name__ == "__main__":
    main()