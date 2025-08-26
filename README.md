# Port-scanner
 Simple Python Port Scanner::  A lightweight and customizable Python-based port scanner that helps you quickly check for open and closed ports on any target system.
# 🔍 Python Port Scanner

A simple yet powerful **Python-based port scanner** for learning and practicing cybersecurity fundamentals.  
This project lets you scan open and closed ports on a target host with options for single, ranged, or fast scanning.  

---

## ✨ Features
- 🚀 **Fast & Lightweight** – Pure Python, no external dependencies.
- 🖥️ **Flexible Scan Modes**  
  - Single Port Scan  
  - Range Scan (custom range)  
  - Fast Scan (common 100 ports)  
- 📊 **Progress Indicator** – See scanning progress in real-time.  
- ✅ **Open & Closed Port Detection** – Full results shown in the terminal.  
- 💾 **Save Results** – Export results to a text file with your chosen filename.  

---

## 📦 Installation
Clone the repo and navigate into it:
```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```
Run the script:

```bash
python port_scanner.py
```
⚡ Usage
Enter the target IP address or domain name.

Select scan type:

1 → Single port

2 → Range of ports

3 → Fast mode (common 100 ports)

Optionally save results to a file.

📂 Example Output
yaml
```
Scanning scanme.nmap.org from port 20 to 200...

Port 22: OPEN
Port 23: CLOSED
Port 25: CLOSED
Port 80: OPEN
Port 110: CLOSED
Port 143: CLOSED
Port 443: OPEN
```
🛡️ Disclaimer
This tool is built for educational purposes only.
Please do not use it on any system you don’t own or have explicit permission to scan.
The author is not responsible for misuse.

Fast Scan mode scans the 100 most commonly used ports (see common_ports.txt)

🤝 Contributing
Contributions are welcome!
 *Fork the repo
 *Create a feature branch
 *Submit a Pull Request

⭐ Support
If you find this project useful, consider leaving a ⭐ on the repo!




```

