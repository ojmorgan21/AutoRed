# modules/vuln_scan.py
from rich import print

# Starter vulnerability database
VULN_DB = {
    "ssh": {"CVE-2018-15473": {"description": "Username enumeration vulnerability", "severity": "Medium"}},
    "ftp": {"CVE-1999-0491": {"description": "Anonymous FTP login allowed", "severity": "High"}},
    "telnet": {"CVE-1999-0516": {"description": "Telnet weak authentication", "severity": "High"}},
    "http": {"CVE-2017-5638": {"description": "Apache Struts RCE", "severity": "Critical"}},
}

def analyze_vulnerabilities(scan_results):
    """
    Takes scan results from recon and maps them to known vulnerabilities.
    Returns a structured list with port, service, vulnerability, severity.
    """
    report = []

    for item in scan_results:
        service = item["service"]
        port = item["port"]
        if service in VULN_DB:
            for cve, vuln_info in VULN_DB[service].items():
                report.append({
                    "port": port,
                    "service": service,
                    "vuln": f"{cve} - {vuln_info['description']}",
                    "severity": vuln_info["severity"]
                })
        else:
            report.append({
                "port": port,
                "service": service,
                "vuln": "No known CVE mapped",
                "severity": "Low"
            })
    return report

def print_vuln_report(report):
    print("\n[bold red]Vulnerability Analysis Report[/bold red]\n")
    for item in report:
        color = "red" if item["severity"] in ["High", "Critical"] else "yellow" if item["severity"] == "Medium" else "green"
        print(f"[{color}]Port {item['port']} | Service: {item['service']} | Vulnerability: {item['vuln']} | Severity: {item['severity']}[/{color}]")
