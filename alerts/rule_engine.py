class RuleEngine:

    def __init__(self):
        self.rules = []

    def add_rule(self, name, detector):
        self.rules.append({"name": name, "detector": detector})

    def get_rules(self):
        return self.rules