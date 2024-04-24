# Nessus
## Not allowed to use LOL

# Nmap
## Allow Use~
## NSE Vulnerability Scripts Scanning
- Browse script   
``` cd /usr/share/nmap/scripts/
cat script.db  | grep "\"vuln\""
```

- Scan for exploitable
```
sudo nmap -sV -p 443 --script "vuln" 192.168.50.124
```

## Work with NSE vuln

