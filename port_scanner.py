import socket
import sys

socket.setdefaulttimeout(0.5)

def get_service_name(port):
    """Pokušava dobiti naziv servisa za dani port."""
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"

def scan_port(ip, port):
    """Vraća True ako je port otvoren."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def scan_range(host, start_port, end_port):
    """Skenira raspon portova i vraća listu otvorenih."""
    # Provjera ispravnosti raspona
    if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
        print("[!] Portovi moraju biti između 1 i 65535")
        sys.exit(1)
    if start_port > end_port:
        print("[!] Početni port mora biti manji od završnog")
        sys.exit(1)

    # Razrješavanje hostnamea
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[!] Ne mogu razriješiti hostname: {host}")
        sys.exit(1)

    print(f"\nSkeniranje: {host} ({ip}), portovi {start_port}-{end_port}")
    print("-" * 45)

    open_ports = []

    for port in range(start_port, end_port + 1):
        # Ispisujemo napredak u istom redu
        print(f"  Testiram port {port}...", end="\r")

        if scan_port(ip, port):
            service = get_service_name(port)
            open_ports.append((port, service))
            print(f"  [+] Port {port} ({service}) - OTVOREN        ")

    return open_ports

def print_results(host, open_ports):
    """Lijepo ispisuje rezultate."""
    print(f"\nOtvoreni portovi na {host}:")
    if open_ports:
        for port, service in open_ports:
            print(f"  - {port} ({service.upper()})")
    else:
        print("  Nema otvorenih portova u zadanom rasponu.")

# ─── ZADATAK 3: višestruki hostovi ───────────────────────────────────────────

def scan_multiple_hosts(hosts, start_port, end_port):
    """Skenira iste portove na više hostova i prikazuje tablicu."""
    results = {}

    for host in hosts:
        print(f"\n{'='*45}")
        open_ports = scan_range(host, start_port, end_port)
        print_results(host, open_ports)
        results[host] = open_ports

    # Tablica rezultata
    print(f"\n\n{'='*45}")
    print("SAŽETAK — svi hostovi")
    print(f"{'='*45}")
    print(f"{'Host':<25} {'Otvoreni portovi'}")
    print("-" * 45)
    for host, ports in results.items():
        port_list = ", ".join(str(p) for p, s in ports) if ports else "—"
        print(f"{host:<25} {port_list}")
    print(f"{'='*45}")

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 45)
    print("       TCP PORT SKENER")
    print("=" * 45)
    print("\nOdaberi mod:")
    print("  1 - Jedan host, raspon portova")
    print("  2 - Više hostova (Zadatak 3)")
    
    choice = input("\nUnesi izbor (1 ili 2): ").strip()

    start_port = int(input("Početni port: ").strip())
    end_port   = int(input("Završni port: ").strip())

    if choice == "1":
        host = input("Unesi host (IP ili hostname): ").strip()
        open_ports = scan_range(host, start_port, end_port)
        print_results(host, open_ports)

    elif choice == "2":
        print("Unesi hostove jedan po jedan, prazna linija za kraj:")
        hosts = []
        while True:
            h = input("  Host: ").strip()
            if not h:
                break
            hosts.append(h)
        if not hosts:
            print("[!] Nisi unio/la nijedan host.")
            sys.exit(1)
        scan_multiple_hosts(hosts, start_port, end_port)

    else:
        print("[!] Neispravan izbor.")
        sys.exit(1)

if __name__ == "__main__":
    main()