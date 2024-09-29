# 1 
- frankfurt
- common name = oscp.example.com
## Nmap scan
```
Host is up (0.043s latency).
Not shown: 63416 closed tcp ports (reset), 2103 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 3.0.3
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
|_ssl-date: TLS randomness does not represent time
22/tcp   open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7e:62:fd:92:52:6f:64:b1:34:48:8d:1e:52:f1:74:c6 (RSA)
|   256 1b:f7:0c:c7:1b:05:12:a9:c5:c5:78:b7:2a:54:d2:83 (ECDSA)
|_  256 ee:d4:a1:1a:07:b4:9f:d9:e5:2d:f6:b8:8d:dd:bf:d7 (ED25519)
25/tcp   open  smtp     Exim smtpd 4.90_1
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
| smtp-commands: oscp.exam Hello nmap.scanme.org [192.168.251.233], SIZE 52428800, 8BITMIME, PIPELINING, AUTH PLAIN LOGIN, CHUNKING, STARTTLS, HELP
|_ Commands supported: AUTH STARTTLS HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP
|_ssl-date: 2024-09-29T03:22:11+00:00; +1m23s from scanner time.
53/tcp   open  domain   ISC BIND 9.11.3-1ubuntu1.18 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.11.3-1ubuntu1.18-Ubuntu
80/tcp   open  http     nginx
|_http-title: oscp.exam &mdash; Coming Soon
| http-methods: 
|_  Potentially risky methods: TRACE
110/tcp  open  pop3     Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: RESP-CODES SASL(PLAIN LOGIN) CAPA STLS UIDL TOP USER PIPELINING AUTH-RESP-CODE
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
143/tcp  open  imap     Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
|_imap-capabilities: OK LITERAL+ listed IDLE AUTH=PLAIN capabilities STARTTLS IMAP4rev1 ID post-login Pre-login ENABLE SASL-IR have AUTH=LOGINA0001 LOGIN-REFERRALS more
|_ssl-date: TLS randomness does not represent time
465/tcp  open  ssl/smtp Exim smtpd 4.90_1
|_ssl-date: 2024-09-29T03:20:23+00:00; -24s from scanner time.
| smtp-commands: oscp.exam Hello nmap.scanme.org [192.168.251.233], SIZE 52428800, 8BITMIME, PIPELINING, AUTH PLAIN LOGIN, CHUNKING, HELP
|_ Commands supported: AUTH HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
587/tcp  open  smtp     Exim smtpd 4.90_1
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
|_ssl-date: 2024-09-29T03:21:12+00:00; +24s from scanner time.
| smtp-commands: oscp.exam Hello nmap.scanme.org [192.168.251.233], SIZE 52428800, 8BITMIME, PIPELINING, AUTH PLAIN LOGIN, CHUNKING, STARTTLS, HELP
|_ Commands supported: AUTH STARTTLS HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP
993/tcp  open  ssl/imap Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
|_imap-capabilities: OK more LITERAL+ listed post-login IDLE Pre-login AUTH=PLAIN SASL-IR have capabilities AUTH=LOGINA0001 IMAP4rev1 LOGIN-REFERRALS ENABLE ID
|_ssl-date: TLS randomness does not represent time
995/tcp  open  ssl/pop3 Dovecot pop3d
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: UIDL TOP SASL(PLAIN LOGIN) CAPA USER RESP-CODES PIPELINING AUTH-RESP-CODE
2525/tcp open  smtp     Exim smtpd 4.90_1
| smtp-commands: oscp.exam Hello nmap.scanme.org [192.168.251.233], SIZE 52428800, 8BITMIME, PIPELINING, AUTH PLAIN LOGIN, CHUNKING, STARTTLS, HELP
|_ Commands supported: AUTH STARTTLS HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP
|_ssl-date: 2024-09-29T03:20:34+00:00; -14s from scanner time.
| ssl-cert: Subject: commonName=oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
| Not valid before: 2022-11-08T08:16:51
|_Not valid after:  2023-11-08T08:16:51
3306/tcp open  mysql    MySQL 5.7.40-0ubuntu0.18.04.1
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=MySQL_Server_5.7.40_Auto_Generated_Server_Certificate
| Not valid before: 2022-11-08T08:15:37
|_Not valid after:  2032-11-05T08:15:37
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.40-0ubuntu0.18.04.1
|   Thread ID: 7
|   Capabilities flags: 65535
|   Some Capabilities: IgnoreSigpipes, InteractiveClient, Speaks41ProtocolOld, SupportsTransactions, Speaks41ProtocolNew, LongPassword, ConnectWithDatabase, FoundRows, SupportsCompression, ODBCClient, SwitchToSSLAfterHandshake, Support41Auth, DontAllowDatabaseTableColumn, LongColumnFlag, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: xM\x10iX!9N\x016g\x0C)m\x0FY4D\x04^
|_  Auth Plugin Name: mysql_native_password
8080/tcp open  http     Apache httpd 2.4.29 ((Ubuntu) mod_fcgid/2.3.9 OpenSSL/1.1.1)
|_http-server-header: Apache/2.4.29 (Ubuntu) mod_fcgid/2.3.9 OpenSSL/1.1.1
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: oscp.exam &mdash; Coming Soon
8083/tcp open  http     nginx
|_http-title: Did not follow redirect to https://192.168.233.156:8083/
8443/tcp open  http     Apache httpd 2.4.29 ((Ubuntu) mod_fcgid/2.3.9 OpenSSL/1.1.1)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.29 (Ubuntu) mod_fcgid/2.3.9 OpenSSL/1.1.1
Service Info: Host: oscp.exam; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 17s, deviation: 48s, median: -14s
```
## Service Emumeration

### ftp
- vsftpd 3.0.3
- no anonymous login
### ssh 
- no cred yet
- OpenSSH 7.6p1 Ubuntu 4ubuntu0.7
### smtp 
- oscp.example.com/organizationName=Vesta Control Panel/stateOrProvinceName=California/countryName=US
### dns
- n/a
### 80:http
- roundcube
- ```/webmail```
### pop3 
- dovecot
### imap 
- dovecot
### 161:snmp
- jack@oscp
- password : 3PUKsX98BMupBiCf

### 465:ssl/smtp 
- exim smtpd 4.90_1
### 587:smtp
- exim smtpd 4.90_1
### 993:imap
- dovecot
### 995:ssl/pop3
- dovecot
### 2525:smtp
- exim smtpd 4.90_1
- 4.91 - Local Privilege Escalation
### 3306:mysql
- 5.7.40 mysql (?)
### 8080:http
- roundcube
- ```/webmail```
### 8083:https
- vestacp
### 8443:http
- roundcube
- ```/webmail```


## Exploit
1. try to login 8083 as Jack:3PUKsX98BMupBiCf
2. success and find RCE about vesta CP : https://ssd-disclosure.com/ssd-advisory-vestacp-multiple-vulnerabilities/
3. run the exploit
## Post Exploitation
- N/A
## Privilege Esculation
- N/A (only need upgrade the shell since its a webshell)
## Proofs
![alt text](image-1.png)

# 2
## Nmap scan
```

```
## Service Emumeration
### ?
## Exploit
## Post Exploitation
## Privilege Esculation
## Proofs

# 3
## Nmap scan
```

```
## Service Emumeration
### ?
## Exploit
## Post Exploitation
## Privilege Esculation
## Proofs