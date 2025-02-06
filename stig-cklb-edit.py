import argparse
import json
import yaml

def load_cklb(file_path):
    """Load the .cklb JSON data from a file."""
    with open(file_path, 'r+', encoding='utf-8') as f:
        cklb_data = json.load(f)
    return cklb_data, file_path

def update_vulnerabilities(cklb_data, yaml_file):
    """Update vulnerabilities' status and comments based on the YAML file."""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

        for entry in data.get("vulnerabilities", []):
            vuln_id = entry.get("Vuln_ID")
            status = entry.get("Status")
            comment = entry.get("Comment")

            for vuln in cklb_data.get("stigs", [])[0].get("rules", []):
                if vuln.get("group_id") == vuln_id:
                    if status:
                        vuln["status"] = status
                    if comment:
                        vuln["comments"] = comment
    return cklb_data

def save_cklb(cklb_data, file_path):
    """Save the modified .cklb JSON data back to the same file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(cklb_data, file, indent=4)

def main():
    # Setting up argument parsing
    parser = argparse.ArgumentParser(description="Update STIG .cklb file based on vulnerabilities YAML file.")
    parser.add_argument("cklb_file", help="Path to the .cklb file")
    parser.add_argument("yaml_file", help="Path to the YAML file with vulnerability updates")

    args = parser.parse_args()

    # Load the cklb data from the file
    cklb_data, file_path = load_cklb(args.cklb_file)

    # Update the cklb data with the vulnerability information from the yaml file
    updated_cklb = update_vulnerabilities(cklb_data, args.yaml_file)

    # Save the updated cklb data back to the file
    save_cklb(updated_cklb, file_path)

    print("CKLB file successfully updated!")

if __name__ == "__main__":
    main()
