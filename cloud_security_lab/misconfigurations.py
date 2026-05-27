def check_misconfig(logs):
    alerts = []

    for log in logs:
        if log.get("event_type") == "PUBLIC_S3_BUCKET":
            alerts.append({
                "type": "S3_PUBLIC_EXPOSURE",
                "severity": "CRITICAL",
                "resource": log.get("resource"),
                "user": log.get("user")
            })

        if log.get("event_type") == "IAM_PRIVILEGE_ESCALATION":
            alerts.append({
                "type": "IAM_ESCALATION_ATTEMPT",
                "severity": "HIGH",
                "user": log.get("user"),
                "resource": log.get("resource")
            })

    return alerts
