# CDIP — Cyber Defense Intelligence Platform

A simulated enterprise-grade cybersecurity platform combining:
- Red Team attack simulation
- SOC detection engine
- Cloud security monitoring
- Container runtime security
- Automated incident response reporting

## Overview
This repository is designed as a security engineering platform that models real-world adversary behavior and SOC telemetry.

## Structure
- `red_team_engine/`: attack simulation tooling, payloads, and logs.
- `soc_engine/`: detection rules, log parsing, and alerting.
- `cloud_security_lab/`: cloud configs, IAM policies, and misconfiguration tests.
- `container_security/`: Dockerfiles, runtime monitoring, and container logs.
- `incident_response_ai/`: report generator and templates.
- `shared/`: shared utilities, configuration, and schemas.
- `docs/` and `reports/`: documentation and generated reports.

## MITRE Mapping
| Attack Type | MITRE ID |
| ----------- | -------- |
| brute_force | T1110    |
| web_attack  | T1190    |
| port_scan   | T1046    |

## Cloud Security Frameworks
- CIS AWS Benchmark
- AWS Well-Architected Security Pillar
- NIST Cybersecurity Framework
- MITRE ATT&CK Cloud techniques

Use this skeleton as a starting point for implementing tooling and workflows.
