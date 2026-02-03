import json
import os

STATE_FILE = "zonas_estado.json"


def load_previous_zones():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_current_zones(zonas):
    with open(STATE_FILE, "w") as f:
        json.dump(zonas, f, indent=2)


def check_zone_alerts(current_zones):
    previous = load_previous_zones()
    alerts = []

    for acao, zona in current_zones.items():
        zona_anterior = previous.get(acao)
        if zona_anterior and zona_anterior != zona:
            alerts.append(f"{acao}: {zona_anterior} → {zona}")

    save_current_zones(current_zones)
    return alerts
  
