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
```
## 4. SMB Enum
- Scan for SMB services

  ``` nmap ```
- identifying NetBIOS information
  
  ``` nbtscan -r {ip} ```

- smb discovery script(nmap) works on SMBv1 only

- Windows SMB enum
  
  Replace dc01 with the name or IP address of the server you want to view shared resources on

  ``` net view \\dc01 /all ```

- SMB Enum tool:
  
  ``` enum4linux-ng -A 192.168.171.187 ``` List all info of SMB

  ``` smbmap -R {share} -H {ip}``` list all files 

## 5. SMTP Enum
- nc(linux) / telnet(windows) to communicate with SMTP server
- ``` VRFY ``` verify users existence
- If return 252 = yes, 550 = no
- ``` smtp-user-enum -t 192.168.158.63 -U /usr/share/wordlists/dirb/big.txt -M VRFY ```

## 6. SNMP Enum (If no interesting thing outside then play this)
- SNMP Mangement information base -> netw management
- MIB Tree info: https://www.ibm.com/support/knowledgecenter/ssw_aix_71/commprogramming/mib.html
1. Enum which opened service first ``` sudo nmap -sU -A --open -p 161  {ip}``` 
2. try this also ``` sudo nmap -sU  --script *snmp* {ip} ```
- ``` onesixtyone ``` also can do similar enum
- ``` snmpwalk -c {community name} {ip} {mib code} ``` to search info from mib e.g. running process, user acc
- ``` -Oa ``` can translate hex to ascii for snmpwalk 

## 7. Connect Windows w/ rdp
- sometimes no need domain (for education account?? e.g. offsec lab)
``` xfreerdp /v:192.168.220.196 /u:offsec /p:lab /cert-ignore  ```
``` rdesktop -u offsec -p lab -d {domain} 192.168.239.74 ```

## 8. Brute Force idea
- find user list
- if have first name and last name try concat them 
    e.g. First name: Anne Last name: Flora
    username = anne.Flora
- Try password with season + year 
    e.g. Summer2023

## File enum
1. xxd (reading file in hex dump) ``` xxd interesting.file ```