import json
from datetime import datetime
from timeline_builder import build_timeline
from mitre_explainer import explain_mitre


def generate_report():
    timeline = build_timeline()

    report = []
    report.append("=== CYBER INCIDENT RESPONSE REPORT ===\n")
    report.append(f"Generated: {datetime.now()}\n\n")
    report.append("=== ATTACK TIMELINE ===\n")

    for event in timeline:
        mitre_id = event.get("mitre_id", "UNKNOWN")
        explanation = explain_mitre(mitre_id)

        report.append(f"Time: {event.get('timestamp')}\n")
        report.append(f"Source: {event.get('source_ip', event.get('user', 'N/A'))}\n")
        report.append(f"Event: {event.get('attack_type', event.get('event_type', 'N/A'))}\n")
        report.append(f"MITRE: {mitre_id}\n")
        report.append(f"Description: {explanation}\n")
        report.append(f"Severity: {event.get('severity', 'INFO')}\n")
        report.append("---\n")

    report.append("\n=== SUMMARY ===\n")
    report.append(f"Total Events: {len(timeline)}\n")
    report.append("System Status: COMPROMISED / UNDER INVESTIGATION\n")

    with open("templates/final_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print(f"[+] Incident Report Generated with {len(timeline)} events")


if __name__ == "__main__":
    generate_report()
