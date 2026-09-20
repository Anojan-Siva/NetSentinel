from alerts.rule_engine import RuleEngine

engine = RuleEngine()
engine.add_rule("Port Scan", "PortScanDetector")
engine.add_rule("SYN Flood", "SynFloodDetector")
rules = engine.get_rules()
print(f"Number of rules: {len(rules)}")
for rule in rules:
    print(f"Rule: {rule['name']}, Detector: {rule['detector']}")

