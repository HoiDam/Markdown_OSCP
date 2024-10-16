# Writing all my careless shit here
1. LFI remember ../../../../../../../../../../../../ 
2. always enum all hidden files with 
   1. ls -la 
   2. dir /a <------- [Windows cmd]
   3. dir -force <-------- [Windows powershell]
   4. gci -force
3. Read the exploit description & comments!!
4. Dont forget the exploit/ways you do in initial foothold -> maybe useful for rooting too!
5. Watch password in mimikatz dump CAREFULLY!!! 
6. [Oscp cheat sheet](https://github.com/0xsyr0/OSCP): Windows Files & Linux Files. Try Read them all!!
7. Sometimes dont need be so tech. keep it simple with sweeping passwords!
8. Make username and password list. Spray all possible assholes (services)
9. CHECK TYPO !
10. All uncommon string can be sub directory -,- e.g. you found weeb maybe can try 192.168.55.66/weeb  
11. Try more rev shell command and remember will have outbound port blocking! (think which port may be used even can curl =/= port can use)
12. Maybe can search password on the webapp you pwned (Go look app folder directory or GUI)
13. Press every button on the web.

# Kill port command
- dont ask why i put here LMAO
1. ```sudo ss -lptn 'sport = :8080'```
2. ``` kill {pid} ```