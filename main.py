# main.py
from modules.recon import run_recon, suggest_next_steps
from modules.vuln_scan import analyze_vulnerabilities, print_vuln_report
from modules.ai_analysis import summarize_vulnerabilities
from modules.report_generator import generate_html_report
from rich import print

def main():
    print("[bold blue]Welcome to AutoRed - Semi-Autonomous Pentesting Agent[/bold blue]\n")
    
    target = input("Enter target IP: ")

    # 1️⃣ Run reconnaissance
    results = run_recon(target)
    print("\n[bold green]Open Ports Discovered:[/bold green]")
    for item in results:
        print(f"Port: {item['port']} | Service: {item['service']}")

    # 2️⃣ Semi-autonomous suggestions
    print("\n[bold magenta]Recommended Next Steps:[/bold magenta]")
    suggest_next_steps(results)

    # 3️⃣ Vulnerability Analysis
    vuln_report = analyze_vulnerabilities(results)
    print_vuln_report(vuln_report)

    # 4️⃣ AI Analysis Summary
    summary = summarize_vulnerabilities(vuln_report)

    # 5️⃣ Generate HTML Report
    generate_html_report(target, vuln_report, summary)

    # 6️⃣ Save plain text report
    text_report_file = "reports/scan_report.txt"
    with open(text_report_file, "w") as f:
        for item in vuln_report:
            f.write(f"Port {item['port']} | Service: {item['service']} | Vulnerability: {item['vuln']} | Severity: {item['severity']}\n")

    print(f"\n[bold green]Plain text report saved to {text_report_file}[/bold green]")

if __name__ == "__main__":
    main()
