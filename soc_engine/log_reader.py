import json


def load_logs(path="../red_team_engine/output_logs/red_team_logs.json"):
    with open(path, "r", encoding="utf-8") as f:
        logs = json.load(f)
    return logs
