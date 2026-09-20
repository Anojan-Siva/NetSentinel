from collections import defaultdict

class SynFloodDetector:
    def __init__(self, threshold=100):
        self.threshold = threshold
        self.syn_counts = defaultdict(int)

    def analyze(self, source_ip):
        self.syn_counts[source_ip] += 1
        syn_count = self.syn_counts[source_ip]
        if syn_count >= self.threshold:
            return True, syn_count
        return False, syn_count