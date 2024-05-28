# Enum
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
- ```ps aux``` show all process 
- ``` ip a ``` list all network card & info in this machine
- ``` route ``` | ``` routel ``` show network routing tables (easy fuck itself localhost services to priv esc)
- ``` ss -anp ``` list all connection
- ``` cat /etc/iptables/rules.v4 ``` need root to see iptables (firewall rules)
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