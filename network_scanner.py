import socket
import ipaddress

# Function to check if a port is open
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # short timeout
        result = sock.connect_ex((ip, port))  # 0 = success
        sock.close()
        return result == 0
    except:
        return False

# Main scanner function
def network_scanner(network, ports_to_scan):
    print(f"Scanning network: {network}")
    net = ipaddress.ip_network(network, strict=False)
    
    for ip in net.hosts():  # loop through all possible hosts
        ip = str(ip)
        try:
            socket.gethostbyaddr(ip)
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        
        open_ports = []
        for port in ports_to_scan:
            if scan_port(ip, port):
                open_ports.append(port)
        
        if open_ports:
            print(f"{ip:15} | {hostname:20} | Open ports: {open_ports}")

