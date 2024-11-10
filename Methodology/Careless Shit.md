# Writing all my careless shit here
1. LFI remember ../../../../../../../../../../../../ 
2. always enum all hidden files with 
   1. ls -la 
   2. dir /a <------- [Windows cmd]
   3. dir -force <-------- [Windows powershell]
   4. gci -force
   5. tree /F {dir} <-- windows
3. Read the exploit description & comments!!
4. Dont forget the exploit/ways you do in initial foothold -> maybe useful for rooting too!
5. Watch password in mimikatz dump CAREFULLY!!! 
6. Sometimes dont need be so tech. keep it simple with sweeping passwords!
7. Make username and password list. Spray all possible assholes (services)
8. CHECK TYPO !
9.  All uncommon string can be sub directory -,- e.g. you found weeb maybe can try 192.168.55.66/weeb  
10. Try more rev shell command and remember will have outbound port blocking! (think which port may be used even can curl =/= port can use)
11. Maybe can search password on the webapp you pwned (Go look app folder directory or GUI)
12. Press every button on the web.
13. Check Sbin for GTFO also!
14. Privlege Esculation maybe using some exploit you discarded in foothold
15. Recheck the config file as other users ( may differs from exploit read )
16. For Impacket modules, domain name is use full domain name (Not netbios) e.g. corp.facebook.com 
17. netexec also try ``` -k ``` if guess ntlm not working, -> use kerberos
18. Use exiftool when see documents to check authors

# Kill port command
- dont ask why i put here LMAO
1. ```sudo ss -lptn 'sport = :8080'```
2. ``` kill {pid} ```