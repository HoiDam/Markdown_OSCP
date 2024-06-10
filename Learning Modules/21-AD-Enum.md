# AD
- ``` xfreerdp /u:stephanie /d:corp.com /v:192.168.50.75 ``` req domain name if AD activated
## Manual Enum
### Legacy Tools
- w/ CMD / PWSH
- ``` net user {user name} /domain ``` get user info | get all without providing
- ``` net group "{group name}" /domain ``` get user list in xx group | get all without providing name

### .NET & Pwsh modules/classes
- Get ldap path (since ldap can support other than AD)
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

- Enum by ldap ``` $direntry = New-Object System.DirectoryServices.DirectoryEntry($LDAP) ```
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
  