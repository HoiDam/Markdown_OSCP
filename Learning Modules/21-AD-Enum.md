# AD
- ``` xfreerdp /u:stephanie /d:corp.com /v:192.168.50.75 ``` req domain name if AD activated
- target domain admin
## Manual Enum
### Legacy Tools
- w/ CMD / PWSH
- ``` net user {user name} /domain ``` get user info | get all without providing
- ``` net group "{group name}" /domain ``` get user list in xx group | get all without providing name

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

### Auto Enum 
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

## Useful query
- Show all computers/users ``` MATCH (m:Computer/User) RETURN m ```
- Show all active sessions ``` MATCH p = (c:Computer)-[:HasSession]->(m:User) RETURN p ```

# Window shit
1. change user: ``` runas /user:{domain_name}\{user_name} "cmd" ```
2. change someone password: ``` net user {username} {new password} /domain ``` 