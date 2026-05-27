MITRE_DESCRIPTIONS = {
    "T1110": "Brute Force Attack - Repeated login attempts to gain access",
    "T1046": "Network Service Scanning - Discovery of open ports/services",
    "T1190": "Exploit Public-Facing Application - Web application attack attempt",
    "T1078": "Valid Account Abuse - Use of compromised credentials",
    "T1087": "Account Discovery - Enumeration of user accounts"
}


def explain_mitre(mitre_id):
    return MITRE_DESCRIPTIONS.get(
        mitre_id,
        "Unknown MITRE Technique"
    )
