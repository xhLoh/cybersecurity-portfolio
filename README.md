# Cybersecurity Portfolio

## About Me
My name is **Loh Xin Herng**. I am a full-time **Software Engineer** and a part-time **Master of Cybersecurity** student.

With a strong foundation in software development, I am transitioning into the security domain to bridge the gap between building applications and securing them. My professional experience in software developing allows me to approach cybersecurity with a practical mindset to focus on how vulnerabilities are introduced during the development lifecycle.

My primary academic interests lie in Penetration Testing, Network and Application Security. I am passionate about understanding secure infrastructures from designing robust network topologies to implementing defense-in-depth strategies against modern threats.

## Technical Skills
* **Network Security:** OSPF Routing, GRE over IPSec Tunnels, VLAN Configuration, Network Topology Design
* **Offensive Security:** Penetration Testing Lifecycle, Vulnerability Assessment, Internal Network Scanning
* **Security Tools:** Cisco IOS (CLI), Nmap, Wireshark, Cisco Packet Tracer, GNS3
* **Programming:** Python

## Certification and Training
* **Cisco Certified CyberOps Associate** 
   * *Provider:* Cisco Networking Academy
   * *Module:* WQE7001 Cyber Security (Sem 1 2025/2026)
   * *Skills Gained:* Security Concepts, Security Monitoring, Host-Based Analysis.
 
* **TryHackMe Online Course** 
  * **OSINT & Reconnaissance:**
     * Modules: Sakura Room (Image Intelligence), Google Dorking, Search Skills.
  * **Offensive Security & Scanning:**
     * Modules: Nmap (Network Mapping), Pentesting Fundamentals, Offensive Security Intro.
  * **Defensive Security:**
     * Modules: Cyber Kill Chain, Network Traffic Basics, Detecting Web Attacks.
   
## Project Experience

### 1. Secure Network Topology Implementation
* **Objective:** To design and secure a multi-site enterprise network simulation connecting three distinct geographical areas.
* **Tools Used:** Cisco Packet Tracer, Cisco IOS.
* **Methodology:**
    * **Routing:** Configured OSPF (Open Shortest Path First) for dynamic routing between core routers (R1, R2, R3).
    * **Encryption:** Implemented GRE over IPSec VPN tunnels to ensure encrypted, private communication between branch offices over a public network simulation.
    * **Access Control:** Hardened switch configurations using VLANs to segregate departmental traffic.
* **Outcome:** Successfully established a stable, redundant network with verified encrypted connectivity (Ping/ICMP) between all simulated branch offices.

### 2. External Reconnaissance & Vulnerability Assessment
* **Objective:** To perform a comprehensive security audit on a target infrastructure to identify exposed assets and critical vulnerabilities.
* **Tools Used:** Nmap (Network Mapper), Shodan, CVE Databases (NVD).
* **Methodology:**
    * **Passive Reconnaissance:** Utilized Shodan to identify internet-facing devices and gather banner information without direct interaction.
    * **Active Scanning:** Conducted Nmap scans (Device Mapping & Service Detection) to enumerate open ports and running service versions.
    * **Vulnerability Analysis:** Correlated identified service versions with known Common Vulnerabilities and Exposures (CVEs) to assess risk levels.
* **Outcome:** Produced a vulnerability report detailing exposed services and potential exploit vectors based on mapped CVEs.
