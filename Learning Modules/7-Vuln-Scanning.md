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
![alt text](1_g2AGcwf6RRQoLG2Z4cakDw.webp)
## Update db with new script
- Paste the new script to nmap/scripts
``` sudo nmap --script-updatedb ```

## Search nmap list 
``` locate *.nse ```

## Use
- ``` sudo nmap -T5 -sCVS --min-rate 10000 -p 443 --script vuln -vvv {ip} ```

- ``` nmap -sCVS --script=smb-vuln-* {ip} -vvv ```


