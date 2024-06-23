# How to assemble all learned shit

## 1. Enum Public Network
    1. Nmap (port? services)
    2. searchsploit ? cve ? eploit-db?
    3. enum website? services?

## 2.  Attack Public machine
    1. Initial foothold: abusing public vulns/ sql injection? etc.
    2. Steal ssh/ rdp credential of the machine  
    3. See if have connection to internal network
    4. If no , try Prividege esculation by enum (linpeas/ winpeas)
    5. See old version of the machine e.g. files/ logs etc
## 3. Gain access to internal network 
    1. Reorganize all credentials | example:
        ```
            daniela:tequieromucho (SSH private key passphrase)
            wordpress:DanielKeyboard3311 (WordPress database connection settings)
            john:dqsTwTpZPn#nL (fetch_current.sh)

            Other identified users:
            marcus
        ```
    2. Try possible entry point
    3. Phishing is another way if no possible attack vector 
        1. Office phishing
        2. MS Library phishing
## 4. Enum Internal Network
    1. Bloodhound
    2. Awareness on the attack path
    3. pivoting & port fw
    4. If windows, see if can RDP first~

## 5. Maybe attack internal services?
    1. gain access to that host which hosting that service e.g. kerberoasting a password and pass to it

## 6. Gain access to Domain Controller
    1. Find Cached credential by various way
    2. Lateral movement!