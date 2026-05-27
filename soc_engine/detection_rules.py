def detect_bruteforce(logs):
    ip_count = {}
    ip_timestamps = {}

    for log in logs:
        if log.get("attack_type") == "brute_force":
            ip = log["source_ip"]
            ip_count[ip] = ip_count.get(ip, 0) + 1
            ip_timestamps.setdefault(ip, []).append(log.get("timestamp", ""))

    alerts = []
    for ip, count in ip_count.items():
        if count >= 5:
            alerts.append({
                "type": "BRUTE_FORCE_DETECTED",
                "attack_type": "brute_force",
                "source_ip": ip,
                "timestamp": sorted(ip_timestamps.get(ip, [" "]))[0],
                "attempts": count,
                "severity": "HIGH"
            })

    return alerts


def detect_port_scan(logs):
    ip_ports = {}
    ip_timestamps = {}

    for log in logs:
        if log.get("attack_type") == "port_scan":
            ip = log["source_ip"]
            ip_ports[ip] = ip_ports.get(ip, 0) + 1
            ip_timestamps.setdefault(ip, []).append(log.get("timestamp", ""))

    alerts = []
    for ip, count in ip_ports.items():
        if count >= 3:
            alerts.append({
                "type": "PORT_SCAN_DETECTED",
                "attack_type": "port_scan",
                "source_ip": ip,
                "timestamp": sorted(ip_timestamps.get(ip, [" "]))[0],
                "ports_scanned": count,
                "severity": "MEDIUM"
            })

    return alerts


def detect_web_attack(logs):
    alerts = []

    for log in logs:
        if log.get("attack_type") == "web_attack":
            alerts.append({
                "type": "WEB_ATTACK_BLOCKED",
                "attack_type": "web_attack",
                "source_ip": log["source_ip"],
                "timestamp": log.get("timestamp", ""),
                "payload": log.get("payload"),
                "severity": "HIGH"
            })

    return alerts
