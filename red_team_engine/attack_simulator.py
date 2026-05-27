import random
import json
from datetime import datetime


def generate_ip():
    return f"192.168.1.{random.randint(2, 254)}"


def brute_force_simulation():
    logs = []

    ip = generate_ip()
    for attempt in range(random.randint(3, 10)):
        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": ip,
            "target": "web_login",
            "attack_type": "brute_force",
            "status": "failed",
            "attempt": attempt + 1,
            "mitre_id": "T1110"
        }
        logs.append(log)

    return logs


def port_scan_simulation():
    logs = []

    ip = generate_ip()
    ports = random.sample(range(20, 1000), 5)

    for port in ports:
        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": ip,
            "attack_type": "port_scan",
            "target_port": port,
            "status": "detected",
            "mitre_id": "T1046"
        }
        logs.append(log)

    return logs


def web_attack_simulation():
    payloads = ["' OR 1=1 --", "<script>alert(1)</script>", "../../etc/passwd"]
    logs = []

    ip = generate_ip()

    for payload in payloads:
        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": ip,
            "target": "/login",
            "attack_type": "web_attack",
            "payload": payload,
            "status": "blocked",
            "mitre_id": "T1190"
        }
        logs.append(log)

    return logs


def run_all_attacks():
    all_logs = []
    all_logs += brute_force_simulation()
    all_logs += port_scan_simulation()
    all_logs += web_attack_simulation()

    return all_logs


if __name__ == "__main__":
    print(json.dumps(run_all_attacks(), indent=2))
