MITRE_MAP = {
    "BRUTE_FORCE_DETECTED": "T1110",
    "PORT_SCAN_DETECTED": "T1046",
    "WEB_ATTACK_BLOCKED": "T1190"
}


def map_to_mitre(alert):
    alert["mitre_id"] = MITRE_MAP.get(alert["type"], "UNKNOWN")
    return alert
