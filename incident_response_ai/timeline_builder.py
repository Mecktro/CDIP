import json


def build_timeline():
    timeline = []

    try:
        with open("../soc_engine/alerts/soc_alerts.json", "r", encoding="utf-8") as f:
            soc_alerts = json.load(f)
            timeline.extend(soc_alerts)
    except FileNotFoundError:
        pass

    try:
        with open("../cloud_security_lab/cloud_logs/cloud_events.json", "r", encoding="utf-8") as f:
            cloud_events = json.load(f)
            timeline.extend(cloud_events)
    except FileNotFoundError:
        pass

    try:
        with open("../red_team_engine/output_logs/red_team_logs.json", "r", encoding="utf-8") as f:
            red_logs = json.load(f)
            timeline.extend(red_logs)
    except FileNotFoundError:
        pass

    timeline.sort(key=lambda x: x.get("timestamp", ""))

    return timeline
