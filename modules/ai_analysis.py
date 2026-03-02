from rich import print

def summarize_vulnerabilities(vuln_report):
    """
    Takes the vulnerability report and generates an AI-like analysis summary.
    """
    summary = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for item in vuln_report:
        severity = item["severity"]
        if severity in summary:
            summary[severity] += 1

    print("\n[bold blue]AI Analysis Summary[/bold blue]\n")
    for sev in ["Critical", "High", "Medium", "Low"]:
        print(f"[bold]{sev}:[/bold] {summary[sev]} issues")

    # Simple recommendations
    if summary["Critical"] > 0:
        print("\n[red]Immediate action required on critical vulnerabilities![/red]")
    elif summary["High"] > 0:
        print("[yellow]High severity vulnerabilities should be addressed soon.[/yellow]")
    else:
        print("[green]System appears low-risk based on detected services.[/green]")

    return summary
