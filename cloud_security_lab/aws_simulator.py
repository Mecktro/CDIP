import json
import random
from datetime import datetime


def generate_cloud_event():
    events = [
        "PUBLIC_S3_BUCKET",
        "IAM_PRIVILEGE_ESCALATION",
        "UNUSUAL_API_CALL",
        "ACCESS_KEY_ABUSE"
    ]

    event = random.choice(events)

    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cloud_provider": "AWS",
        "service": "AWS_SIMULATION",
        "event_type": event,
        "user": f"user_{random.randint(1, 5)}",
        "resource": f"resource_{random.randint(100, 999)}",
        "status": "detected"
    }

    return log


def generate_cloud_logs(n=15):
    return [generate_cloud_event() for _ in range(n)]


def save_logs():
    logs = generate_cloud_logs()

    with open("cloud_logs/cloud_events.json", "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

    print(f"[+] Generated {len(logs)} cloud security events")


if __name__ == "__main__":
    save_logs()
