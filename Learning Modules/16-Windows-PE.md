# Enum
## Info useful
- Usrname , hostname
- Group memberships of current user
- Existing users and groups
- OS,version ,architecture
- Network Info
- Installed app
- Running process

## Basic enum
- ``` whoami /groups ```  display all groups our current user is a member
- ``` Get-LocalUser ```  obtain a list of all local users 
- ``` Get-LocalGroup ``` existing groups in local
- ``` Get-LocalGroupMember {Group_name} ``` list users under a group
- ``` systeminfo ``` care 32 or 64 bits
- ``` netstat -ano ``` search service
- ``` Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname ``` Get installed app 32 bits
- ``` Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname ``` Get installed app 64 bits
- ``` Get-Process ```
- get path of a process: ``` Get-Process | Select-Object Name,Path | Select-String "NonStandardProcess" ```
- Check if have remote access (rdp) ``` net user xxx``` and see local group memberships
    have = *Remote Management Use Users*

## Hidden info
- Searching attackable files in system ``` Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue ```
- Can search if have password ``` Get-ChildItem -Path C:\xampp\apache -Include *.txt ,*.ini -File -Recurse -ErrorAction SilentlyContinue ```
- Can search user desktop ``` C:\Users\{user_name}\Desktop ``` <- probably here lol
- 

## Auto tool 
- Winpeas (may be info not correct)