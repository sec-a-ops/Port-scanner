import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
COMMON_PORTS = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
    110, 111, 119, 123, 135, 139, 143, 161, 162, 179,
    194, 389, 443, 445, 465, 514, 515, 587, 631, 636,
    993, 995, 1080, 1433, 1521, 1723, 2049, 2082, 2083, 2086,
    2087, 2095, 2096, 2483, 2484, 3128, 3306, 3389, 3690, 4369,
    4899, 5432, 5900, 6000, 6660, 6661, 6662, 6663, 6664, 6665,
    6666, 6667, 6668, 6669, 7000, 7070, 8000, 8008, 8080, 8081,
    8443, 8888, 9000, 9001, 9090, 10000, 32768, 49152, 49153, 49154,
    49155, 49156, 49157, 49158, 49159, 49160, 49161, 49162, 49163, 49164
]

def scan_port(host, port, timeout=1.0, grab_banner=False):
    """Scan a single port. Optionally grab banner. Returns (port, status, banner)."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        
        banner = None
        if result == 0:  
            status = "OPEN"
            if grab_banner:
                try:
                    sock.settimeout(1.0)
                    sock.send(b"HEAD / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host).encode())
                    banner = sock.recv(1024).decode(errors="replace").strip()
                    if not banner:
                        banner = None
                except Exception:
                    banner = None
        else:
            status = "CLOSED"
        
        sock.close()
        return (port, status, banner)
    except socket.gaierror:
        return (port, "ERROR: Invalid hostname", None)
    except socket.error:
        return (port, "ERROR: Connection failed", None)
    except Exception as e:
        return (port, f"ERROR: {e}", None)

def scan_ports(host, ports, max_workers=50, timeout=1.0, grab_banner=False):
    """Scan multiple ports concurrently."""
    results = []
    
    print(f"\nScanning {host} for {len(ports)} ports...\n")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_port, host, port, timeout, grab_banner): port 
                   for port in ports}
    
        completed = 0
        for future in as_completed(futures):
            port, status, banner = future.result()
            if status == "OPEN":
                banner_text = f" | Banner: {banner[:60]}" if banner else ""
                print(f"Port {port:5d}: {status}{banner_text}")
            results.append((port, status, banner))
            completed += 1
            
        
            progress = (completed / len(ports)) * 100
            if completed % 10 == 0 or status == "OPEN":
                sys.stderr.write(f'\rProgress: {completed}/{len(ports)} ({progress:.0f}%)')
                sys.stderr.flush()
    
    sys.stderr.write('\r' + ' ' * 50 + '\r') 
    
   
    results.sort(key=lambda x: x[0])
    
    print("\n✅ Scan Complete!\n")
    print("Summary:")
    open_ports = [p for p, s, b in results if s == "OPEN"]
    print(f"  Open ports: {open_ports if open_ports else 'None'}")
    print(f"  Total scanned: {len(results)}\n")
    
    return results

def main():
    try:
        host = input("Enter target host (IP or domain): ").strip()
        
        
        grab_banner_input = input("Grab banners from open ports? (y/n) [default: n]: ").strip().lower()
        grab_banner = grab_banner_input == 'y'
        
        print("\nChoose scan type:")
        print("1. Single Port")
        print("2. Port Range")
        print("3. Fast Scan (Top 100 Ports)")
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == "1":
            port = int(input("Enter port number: "))
            scan_ports(host, [port], grab_banner=grab_banner)
        
        elif choice == "2":
            port_range = input("Enter port range (e.g., 20-100): ").strip()
            try:
                start, end = map(int, port_range.split("-"))
                ports = range(start, end + 1)
                scan_ports(host, ports, grab_banner=grab_banner)
            except ValueError:
                print("❌ Invalid range format. Use: start-end")
        
        elif choice == "3":
            scan_ports(host, COMMON_PORTS, grab_banner=grab_banner)
        
        else:
            print("❌ Invalid choice.")
            return
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Scan interrupted by user.")
        sys.exit(0)
    except ValueError as e:
        print(f"❌ Invalid input: {e}")

if __name__ == "__main__":
    main()
