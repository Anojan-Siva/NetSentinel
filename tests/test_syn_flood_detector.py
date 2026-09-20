from analysis.syn_flood_detector import SynFloodDetector

detector = SynFloodDetector(threshold=5)
source_ip = "192.168.1.50"
for i in range(5):
    detected, count = detector.analyze(source_ip)
    print(f"SYN {i + 1} | " f"SYN count: {count} | " f"Detected: {detected}")
