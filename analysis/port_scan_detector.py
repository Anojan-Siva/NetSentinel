from collections import defaultdict

class PortScanDetector:
    def __init__(self, threshold=10):
        self.threshold = threshold
        self.port_activity = defaultdict(set)

    def analyze(self, source_ip, destination_ip, destination_port):
        key = (source_ip, destination_ip)
        self.port_activity[key].add(destination_port)
        unique_ports = len(self.port_activity[key])
        if unique_ports >= self.threshold:
            return True, unique_ports
        return False, unique_ports