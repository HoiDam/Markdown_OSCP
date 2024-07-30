# VM 1
- dc01.medtech.com
```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-07-30 11:57:00Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: medtech.com0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: medtech.com0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
50479/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
50484/tcp open  msrpc         Microsoft Windows RPC
50495/tcp open  msrpc         Microsoft Windows RPC
50508/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-07-30T11:57:53
|_  start_date: N/A
|_nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:f4:a5 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: -9s


```

# VM 2
- files02.medtech.com
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
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
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-07-30T12:04:01
|_  start_date: N/A
|_clock-skew: -10s
|_nbstat: NetBIOS name: FILES02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:df:a7 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

```
## Foothold & Root
1. checked with crackmapexec its pwned!
   ```
        crackmapexec smb 172.16.184.13 -u "joe" -p "Flowers1" -d medtech.com --shares
   ```
2. Run psexec in kali
    ``` 
        impacket-psexec medtech.com/joe:Flowers1@172.16.184.11
    ```

# VM 6
- dev04.medtech.com
```
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=DEV04.medtech.com
| Not valid before: 2024-04-07T19:17:42
|_Not valid after:  2024-10-07T19:17:42
|_ssl-date: 2024-07-30T12:01:19+00:00; -10s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: MEDTECH
|   NetBIOS_Domain_Name: MEDTECH
|   NetBIOS_Computer_Name: DEV04
|   DNS_Domain_Name: medtech.com
|   DNS_Computer_Name: DEV04.medtech.com
|   DNS_Tree_Name: medtech.com
|   Product_Version: 10.0.20348
|_  System_Time: 2024-07-30T11:59:17+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49667/tcp open  unknown
49668/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
```

# VM 7
- prod01.medtech.com
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
```

# VM 8
- ?
```
    22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
    | ssh-hostkey: 
    |   3072 eb:0e:77:7c:69:f2:4a:a5:65:2a:1c:ec:ec:6e:79:19 (RSA)
    |_  256 74:51:ee:1e:8f:61:d6:0f:c5:11:52:2e:f9:ef:ac:29 (ECDSA)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# VM 9
- client01.medtech.com
```
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: MEDTECH
|   NetBIOS_Domain_Name: MEDTECH
|   NetBIOS_Computer_Name: CLIENT01
|   DNS_Domain_Name: medtech.com
|   DNS_Computer_Name: CLIENT01.medtech.com
|   DNS_Tree_Name: medtech.com
|   Product_Version: 10.0.22000
|_  System_Time: 2024-07-30T14:21:27+00:00
| ssl-cert: Subject: commonName=CLIENT01.medtech.com
| Not valid before: 2024-04-07T20:14:17
|_Not valid after:  2024-10-07T20:14:17
|_ssl-date: 2024-07-30T14:22:07+00:00; -10s from scanner time.
5040/tcp  open  unknown
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-07-30T14:21:27
|_  start_date: N/A
|_clock-skew: mean: -10s, deviation: 0s, median: -10s
|_nbstat: NetBIOS name: CLIENT01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:92:cd (VMware)
```

# VM 10
- client02.medtech.com
```
?

```

```
SMB         172.16.184.83   445    CLIENT02         [*] Windows 10.0 Build 22000 x64 (name:CLIENT02) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.184.83   445    CLIENT02         [+] medtech.com\joe:Flowers1 
SMB         172.16.184.83   445    CLIENT02         [+] Enumerated shares
SMB         172.16.184.83   445    CLIENT02         Share           Permissions     Remark
SMB         172.16.184.83   445    CLIENT02         -----           -----------     ------
SMB         172.16.184.83   445    CLIENT02         ADMIN$                          Remote Admin
SMB         172.16.184.83   445    CLIENT02         C               READ            
SMB         172.16.184.83   445    CLIENT02         C$                              Default share
SMB         172.16.184.83   445    CLIENT02         IPC$            READ            Remote IPC
SMB         172.16.184.83   445    CLIENT02         Windows         READ            
                                                                                        
```

