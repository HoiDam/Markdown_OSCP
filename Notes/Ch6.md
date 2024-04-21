# Passive Information Gathering
## 1. Whois Enum
- ``` whois {hostname} -h {ip} ```
- Gather servers name, email
## 2. Google hacking
- Just google loll
## 3. Netcraft
- Site report check info
- Checking what app running on top
## 4. Open-Source Code
- Tool: Gitrob and Gitleaks
## 5. Shodan
- Grab iot devices
## 6. Security Headers & SSL/TLS
- Scan headers tool: https://securityheaders.com/ 

# Active Information Gathering
## 1. DNS Enum

- ``` host {domain name} ```
- after -t can search different params 

  ``` host -t mx {domain name} ```
  
- search multi domains:

  for ip in $(cat list.txt); do host $ip.megacorpone.com; done

- Tool: dnsrecon 
    
    Search details under a param

    ``` dnsrecon -d {domain name} -t std ```
- Tool: dnsenum

    Brute force enum all possible sub domain

- Windows command

    ``` nslookup -type=TXT {sub domain + domain name} {ip} ```

## 2. TCP/UDP Port Scanning
- ``` nc -nv -u -z -w 1 {ip} {port}-{port} ```

## 3. Nmap
- Using IPtable chain to log traffic packets/bytes if needed ( in case big data )
- Params:
``` 
-sS Stealth (not completing ACK | but not stealth in modern anymore since can log by FW)
-sT Full TCP scan
-sU UDP scan
-sN network sweeping ips
-oG output log
-O OS fingerprint 
-A OS & service enum
```
- can use more than 1 scan mode to build full picture clearly
- Windows handling (TCP):
```
Test-NetConnection -Port {port} {ip}

1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("{ip}", $_)) "TCP port $_ is open"} 2>$null