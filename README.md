# **README**

## **STIG-CKLB-EDIT**

Python3 script to automate editing DISA STIG .cklb checklist control status and comments.

## **Introduction**

My goal is to create a fully automated STIG process using the DISA SCC SCAP, evaluate-stig and this script to ease the burden on technicians who constantly have to create checklists.

## **Usage**

To use STIG-CKLB-EDIT, follow these steps:

1. Run `python3 ./stig-cklb-edit.py /path/to/cklb/file /path/to/vulnerability/edits/yaml/file`
2. The script will utilize the inputs from your yaml file to edit an existing checklist and save it.
3. The yaml file needs to be structured like:
```
vulnerabilities:
  - Vuln_ID: "V-257777"
    Status: "not_a_finding"
    Comment: "CHIKUNS"
  - Vuln_ID: "V-258241"
    Status: "not_a_finding"
    Comment: "CHIKUNS said so."
  - Vuln_ID: "V-258227"
    Status: "not_a_finding"
    Comment: "CHIKUNS told me too."
  - Vuln_ID: "V-258225"
    Status: "not_a_finding"
    Comment: "CHIKUNS HATES ME."
```

