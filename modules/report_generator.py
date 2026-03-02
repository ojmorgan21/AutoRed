from jinja2 import Template

def generate_html_report(target, vuln_report, summary, output_file="reports/scan_report.html"):
    # Load the HTML template
    with open("reports/report_template.html") as f:
        template = Template(f.read())

    # Render the template with the scan data
    html_content = template.render(target=target, vuln_report=vuln_report, summary=summary)

    # Save the rendered HTML
    with open(output_file, "w") as f:
        f.write(html_content)

    print(f"\n[bold blue]HTML report saved to {output_file}[/bold blue]")
