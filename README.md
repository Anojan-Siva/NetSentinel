# NetSentinel — Network Intrusion Detection System

NetSentinel is a Python-based Network Intrusion Detection System (NIDS) designed to monitor network traffic, analyze packets, identify suspicious activity, and generate security alerts.

The project was built as a hands-on network security project to explore packet analysis, TCP/IP networking, intrusion detection techniques, and security monitoring using Python.

## Features

* Captures live network traffic using Scapy
* Extracts packet information including:

  * Source IP addresses
  * Destination IP addresses
  * Protocols
  * Destination ports
  * TCP information
* Tracks network traffic statistics
* Calculates packet-per-second activity
* Identifies frequently contacted IP addresses and ports
* Detects potential TCP port scanning activity
* Generates real-time alerts when suspicious port activity reaches a configurable threshold
* Includes automated testing for the port scan detection logic

## Technologies Used

| Technology                       | Purpose                                    |
| -------------------------------- | ------------------------------------------ |
| Python                           | Core programming language                  |
| Scapy                            | Network packet capture and analysis        |
| TCP/IP                           | Network communication and traffic analysis |
| Git/GitHub                       | Version control and project management     |
| Python `Counter`                 | Traffic statistics and aggregation         |
| Python `unittest` / test scripts | Testing detection logic                    |


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnojanSiva722/NetSentinel.git
cd NetSentinel
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running NetSentinel

NetSentinel currently captures traffic from the Wi-Fi interface on macOS.

The Wi-Fi interface can be identified using:

```bash
networksetup -listallhardwareports
```

For the development environment, the Wi-Fi interface is `en0`.

Start the NIDS with:

```bash
sudo python3 -m capture.packet_capture
```

The program will begin monitoring network traffic and display statistics when the capture is stopped.

Press:

```text
Ctrl+C
```

to stop the capture.

## Example Traffic Report

```text
==================================================
           NETSENTINEL TRAFFIC REPORT
==================================================
Packets analyzed: 1247
Capture duration: 60.32 seconds
Packets per second: 20.67

Top Source IPs:
192.168.1.10: 642 packets
192.168.1.1: 421 packets

Top Destination IPs:
192.168.1.1: 421 packets
142.250.72.14: 87 packets

Protocols:
TCP: 1024 packets
UDP: 198 packets
Other: 25 packets

Top Destination Ports:
Port 443: 512 packets
Port 53: 143 packets
Port 80: 72 packets
==================================================
```

*Example output is illustrative.*

## Security Considerations

NetSentinel is intended for use on networks and systems that I own or have explicit authorization to monitor.

Packet capture can expose network metadata and potentially sensitive traffic information. Testing should therefore be performed only in controlled environments such as:

* A personal home network
* A local virtual machine
* A dedicated security lab
* Other explicitly authorized environments

## Learning Objectives

This project is designed to develop practical experience with:

* Network packet analysis
* TCP/IP protocols
* Intrusion detection
* Network reconnaissance detection
* Python security programming
* Security monitoring
* Detection rules and thresholds
* Automated security testing
* Secure development practices

## Disclaimer

NetSentinel is an educational cybersecurity project. It should only be used to monitor and test networks, devices, and systems for which the user has explicit authorization.