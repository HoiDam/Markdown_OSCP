# .149 Kiero
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 5c:5f:f1:bb:02:f9:14:7c:8e:38:32:2b:f4:bc:d0:8c (RSA)
|   256 18:e2:47:e1:c8:40:a1:d0:2c:a5:87:97:bd:01:12:27 (ECDSA)
|_  256 26:2d:98:d9:47:6d:22:5d:4a:14:7a:24:5c:98:a2:1d (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```
## Foothold
1. found kiero reset password in snmp
2. try login kiero:kiero in ftp...
3. grab id_rsa & id_rsa_2 (found uncrackable...) & id_rsa.pub
4. saw john user there and try -i id_rsa.pub
5. no luck and try id_rsa for john and ok...
6. ``` ssh -i id_rsa john@192.168.229.149  ```

## Root
1. no other exploitable
2. try exploit suggester & gcc seems on machine
3. using [CVE-2022-0847] DirtyPipe
4. ``` exploit-1.c ``` & ``` ./exploit-2 /home/john/RESET_PASSWD ``` also works


# .150 Berlin
```
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 ad:ac:80:0a:5f:87:44:ea:ba:7f:95:ca:1e:90:78:0d (ECDSA)
|_  256 b3:ae:d1:25:24:c2:ab:4f:f9:40:c5:f0:0b:12:87:bb (ED25519)
8080/tcp open  http-proxy
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 
|     Content-Type: application/json;charset=UTF-8
|     Date: Sun, 15 Sep 2024 02:40:28 GMT
|     Connection: close
|     {"timestamp":"2024-09-15T02:40:28.495+0000","status":404,"error":"Not Found","message":"No message available","path":"/nice%20ports%2C/Tri%6Eity.txt%2ebak"}
|   GetRequest: 
|     HTTP/1.1 200 
|     Content-Type: text/plain;charset=UTF-8
|     Content-Length: 19
|     Date: Sun, 15 Sep 2024 02:40:28 GMT
|     Connection: close
|     {"api-status":"up"}
|   HTTPOptions: 
|     HTTP/1.1 200 
|     Allow: GET,HEAD,OPTIONS
|     Content-Length: 0
|     Date: Sun, 15 Sep 2024 02:40:28 GMT
|     Connection: close
|   RTSPRequest: 
|     HTTP/1.1 505 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 830
|     Date: Sun, 15 Sep 2024 02:40:28 GMT
|     <!doctype html><html lang="en"><head><title>HTTP Status 505 
|     HTTP Version Not Supported</title><style type="text/css">h1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} h2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} h3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} body {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} b {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} p {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;} a {color:black;} a.name {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1
|   Socks5: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 800
|     Date: Sun, 15 Sep 2024 02:40:28 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|_    Request</title><style type="text/css">h1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} h2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} h3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} body {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} b {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} p {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;} a {color:black;} a.name {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body
|_http-favicon: Spring Java Framework
|_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
|_http-open-proxy: Proxy might be redirecting requests
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.94SVN%I=7%D=9/14%Time=66E64924%P=x86_64-pc-linux-gnu%r
SF:(GetRequest,98,"HTTP/1\.1\x20200\x20\r\nContent-Type:\x20text/plain;cha
SF:rset=UTF-8\r\nContent-Length:\x2019\r\nDate:\x20Sun,\x2015\x20Sep\x2020
SF:24\x2002:40:28\x20GMT\r\nConnection:\x20close\r\n\r\n{\"api-status\":\"
SF:up\"}")%r(HTTPOptions,75,"HTTP/1\.1\x20200\x20\r\nAllow:\x20GET,HEAD,OP
SF:TIONS\r\nContent-Length:\x200\r\nDate:\x20Sun,\x2015\x20Sep\x202024\x20
SF:02:40:28\x20GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,3C6,"HT
SF:TP/1\.1\x20505\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nConte
SF:nt-Language:\x20en\r\nContent-Length:\x20830\r\nDate:\x20Sun,\x2015\x20
SF:Sep\x202024\x2002:40:28\x20GMT\r\n\r\n<!doctype\x20html><html\x20lang=\
SF:"en\"><head><title>HTTP\x20Status\x20505\x20\xe2\x80\x93\x20HTTP\x20Ver
SF:sion\x20Not\x20Supported</title><style\x20type=\"text/css\">h1\x20{font
SF:-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;fo
SF:nt-size:22px;}\x20h2\x20{font-family:Tahoma,Arial,sans-serif;color:whit
SF:e;background-color:#525D76;font-size:16px;}\x20h3\x20{font-family:Tahom
SF:a,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;
SF:}\x20body\x20{font-family:Tahoma,Arial,sans-serif;color:black;backgroun
SF:d-color:white;}\x20b\x20{font-family:Tahoma,Arial,sans-serif;color:whit
SF:e;background-color:#525D76;}\x20p\x20{font-family:Tahoma,Arial,sans-ser
SF:if;background:white;color:black;font-size:12px;}\x20a\x20{color:black;}
SF:\x20a\.name\x20{color:black;}\x20\.line\x20{height:1px;background-color
SF::#525D76;border:none;}</style></head><body><h1")%r(FourOhFourRequest,11
SF:3,"HTTP/1\.1\x20404\x20\r\nContent-Type:\x20application/json;charset=UT
SF:F-8\r\nDate:\x20Sun,\x2015\x20Sep\x202024\x2002:40:28\x20GMT\r\nConnect
SF:ion:\x20close\r\n\r\n{\"timestamp\":\"2024-09-15T02:40:28\.495\+0000\",
SF:\"status\":404,\"error\":\"Not\x20Found\",\"message\":\"No\x20message\x
SF:20available\",\"path\":\"/nice%20ports%2C/Tri%6Eity\.txt%2ebak\"}")%r(S
SF:ocks5,3BB,"HTTP/1\.1\x20400\x20\r\nContent-Type:\x20text/html;charset=u
SF:tf-8\r\nContent-Language:\x20en\r\nContent-Length:\x20800\r\nDate:\x20S
SF:un,\x2015\x20Sep\x202024\x2002:40:28\x20GMT\r\nConnection:\x20close\r\n
SF:\r\n<!doctype\x20html><html\x20lang=\"en\"><head><title>HTTP\x20Status\
SF:x20400\x20\xe2\x80\x93\x20Bad\x20Request</title><style\x20type=\"text/c
SF:ss\">h1\x20{font-family:Tahoma,Arial,sans-serif;color:white;background-
SF:color:#525D76;font-size:22px;}\x20h2\x20{font-family:Tahoma,Arial,sans-
SF:serif;color:white;background-color:#525D76;font-size:16px;}\x20h3\x20{f
SF:ont-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76
SF:;font-size:14px;}\x20body\x20{font-family:Tahoma,Arial,sans-serif;color
SF::black;background-color:white;}\x20b\x20{font-family:Tahoma,Arial,sans-
SF:serif;color:white;background-color:#525D76;}\x20p\x20{font-family:Tahom
SF:a,Arial,sans-serif;background:white;color:black;font-size:12px;}\x20a\x
SF:20{color:black;}\x20a\.name\x20{color:black;}\x20\.line\x20{height:1px;
SF:background-color:#525D76;border:none;}</style></head><body");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# .151 Gust
```
PORT     STATE SERVICE          VERSION
80/tcp   open  http             Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows
3389/tcp open  ms-wbt-server    Microsoft Terminal Services
|_ssl-date: 2024-09-15T02:43:16+00:00; -8s from scanner time.
| ssl-cert: Subject: commonName=OSCP
| Not valid before: 2024-09-14T02:36:02
|_Not valid after:  2025-03-16T02:36:02
8021/tcp open  freeswitch-event FreeSWITCH mod_event_socket
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -8s
```

## Foothold
1. freeswitch exploit rce
   
## root
1. have impersonate priv
2. godpotato