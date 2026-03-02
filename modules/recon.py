import nmap

def run_recon(target):
    print(f"[+] Starting reconnaissance on {target}...")

    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sV')  # service/version scan

    results = []

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                results.append({
                    "port": port,
                    "service": service
                })

    return results

def suggest_next_steps(scan_results):
    print("\n[bold yellow]Suggested Actions:[/bold yellow]\n")
    for item in scan_results:
        port = item['port']
        service = item['service']

        if service in ["ssh", "ftp", "telnet"]:
            print(f"[green]Try brute-force or credential checks on {service} (port {port})[/green]")
        elif service in ["http", "https"]:
            print(f"[cyan]Enumerate web directories or vulnerabilities on {service} (port {port})[/cyan]")
        else:
            print(f"[magenta]Port {port} with service {service} – further analysis optional[/magenta]")
