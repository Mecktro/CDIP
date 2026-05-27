from attack_simulator import brute_force_simulation, port_scan_simulation, web_attack_simulation


SCENARIOS = {
    "brute_force": {
        "description": "Simulate repeated login failures against web authentication endpoints.",
        "mitre_id": "T1110",
        "generator": brute_force_simulation
    },
    "port_scan": {
        "description": "Simulate a network reconnaissance scan of common TCP ports.",
        "mitre_id": "T1046",
        "generator": port_scan_simulation
    },
    "web_attack": {
        "description": "Simulate suspicious web payloads against application endpoints.",
        "mitre_id": "T1190",
        "generator": web_attack_simulation
    }
}


def list_scenarios():
    return [key for key in SCENARIOS.keys()]


def generate_scenario(scenario_name):
    scenario = SCENARIOS.get(scenario_name)
    if not scenario:
        raise ValueError(f"Unknown scenario '{scenario_name}'")

    return scenario["generator"]()
