# Metasploit

- Rules:
- Allow in ALL machines
    ```
    multi/handler
    msfvenom (excluding meterpreter payload),
    pattern_create 
    pattern_offset 
    ```
- Allow in SINGLE machines
  ```
    meterpreter
    auxiliary
    post
    exploit
    scan
  ```