import json
from log_reader import load_logs
from detection_rules import (
    detect_bruteforce,
    detect_port_scan,
    detect_web_attack
)
from mitre_mapping import map_to_mitre


def run_soc():
    logs = load_logs()

    alerts = []
    alerts += detect_bruteforce(logs)
    alerts += detect_port_scan(logs)
    alerts += detect_web_attack(logs)

    mapped_alerts = [map_to_mitre(a) for a in alerts]

    with open("alerts/soc_alerts.json", "w", encoding="utf-8") as f:
        json.dump(mapped_alerts, f, indent=4)

    print(f"[+] SOC Engine generated {len(mapped_alerts)} alerts")


if __name__ == "__main__":
    run_soc()
