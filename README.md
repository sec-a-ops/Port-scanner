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

These are the most commonly scanned ports from Nmap’s fast scan (top 100) list.

```
20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,
7,9,13,15,17,19,37,49,67,68,69,70,79,88,102,113,119,135,137,138,139,143,161,162,
177,179,389,427,465,512,513,514,515,520,521,540,554,587,631,636,873,902,990,992,
993,995,1080,1194,1433,1434,1494,1521,1720,1723,2049,2082,2083,2086,2087,2095,2096,
3306,3389,3690,5432,5900,6000,6667,7001,8000,8080,8081,8443,8888,9000,9090,10000
```

You can load them in your Python script with:
```
python
Copy
Edit
def load_common_ports(filename="common_ports.txt"):
    with open(filename, "r") as f:
        ports = f.read().replace("\n", "").split(",")
    return [int(p.strip()) for p in ports if p.strip()]
```
Then your “fast mode” will read from this file instead of hardcoding ports.

🛡️ Disclaimer
This tool is built for educational purposes only.
Please do not use it on any system you don’t own or have explicit permission to scan.
The author is not responsible for misuse.



🤝 Contributing
Contributions are welcome!
 *Fork the repo
 *Create a feature branch
 *Submit a Pull Request

⭐ Support
If you find this project useful, consider leaving a ⭐ on the repo!



