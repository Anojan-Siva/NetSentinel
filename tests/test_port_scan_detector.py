from analysis.port_scan_detector import PortScanDetector

detector = PortScanDetector(threshold=5)
source_ip = "192.168.1.50"
destination_ip = "192.168.1.25"
ports = [21, 22, 23, 25, 80]
for port in ports:
    detected, count = detector.analyze(source_ip, destination_ip, port)
    print(f"Port {port} | Unique ports: {count} | Detected: {detected}")