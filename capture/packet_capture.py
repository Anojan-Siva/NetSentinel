from scapy.all import sniff, IP, TCP, UDP
from analysis.port_scan_detector import PortScanDetector
from analysis.syn_flood_detector import SynFloodDetector
from collections import Counter
import time

packet_count = 0
source_ips = Counter()
destination_ips = Counter()
protocols = Counter()
destination_ports = Counter()
start_time = time.time()
port_scan_detector = PortScanDetector(threshold=10)
syn_flood_detector = SynFloodDetector(threshold=100)

def process_packet(packet):
    global packet_count
    if IP not in packet:
        return
    packet_count += 1
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    source_ips[source_ip] += 1
    destination_ips[destination_ip] += 1
    if TCP in packet:
        protocols["TCP"] += 1
        destination_port = packet[TCP].dport
        destination_ports[destination_port] += 1
        detected, unique_ports = port_scan_detector.analyze(source_ip, destination_ip, destination_port)
        if detected:
            print(f"\n PORT SCAN DETECTED: " f"{source_ip} -> {destination_ip} " f"({unique_ports} unique ports)")
        if packet[TCP].flags == "S":
            detected, syn_count = syn_flood_detector.analyze(source_ip)
            if detected:
                print(f"\n SYN FLOOD DETECTED: " f"{source_ip} -> {destination_ip} " f"({syn_count} SYN packets)")
    elif UDP in packet:
        protocols["UDP"] += 1
        destination_ports[packet[UDP].dport] += 1
    else:
        protocols["Other"] += 1


def display_statistics():
    elapsed_time = time.time() - start_time
    print("\n" + "=" * 50)
    print("           NETSENTINEL TRAFFIC REPORT")
    print("=" * 50)
    print(f"Packets analyzed: {packet_count}")
    print(f"Capture duration: {elapsed_time:.2f} seconds")
    if elapsed_time > 0:
        print(f"Packets per second: {packet_count / elapsed_time:.2f}")
    print("\nTop Source IPs:")
    for ip, count in source_ips.most_common(5):
        print(f"{ip}: {count} packets")
    print("\nTop Destination IPs:")
    for ip, count in destination_ips.most_common(5):
        print(f"{ip}: {count} packets")
    print("\nProtocols:")
    for protocol, count in protocols.items():
        print(f"{protocol}: {count} packets")
    print("\nTop Destination Ports:")
    for port, count in destination_ports.most_common(5):
        print(f"Port {port}: {count} packets")
    print("\n" + "=" * 50)

print("NetSentinel is starting...")
print("Listening for network traffic...")
print("Press Ctrl+C to stop.\n")
try:
    sniff(iface="en0", prn=process_packet, store=False)
except KeyboardInterrupt:
    pass
finally:
    print("\nStopping packet capture...")
    display_statistics()