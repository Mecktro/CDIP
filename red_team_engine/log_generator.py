import json
from attack_simulator import run_all_attacks


def save_logs():
    logs = run_all_attacks()

    with open("output_logs/red_team_logs.json", "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

    print(f"[+] Generated {len(logs)} attack logs")


if __name__ == "__main__":
    save_logs()
