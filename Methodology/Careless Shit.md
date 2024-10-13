# Writing all my careless shit here
1. LFI remember ../../../../../../../../../../../../ 
2. always enum all hidden files with 
   1. ls -la 
   2. dir /a <------- [Windows cmd]
   3. dir -force <-------- [Windows powershell]
   4. gci -force
3. Always possible find all file type ``` html,php,aspx ```
4. Read the exploit description & comments!!
5. Dont forget the exploit/ways you do in initial foothold -> maybe useful for rooting too!
6. Watch password in mimikatz dump CAREFULLY!!! 
7. Oscp cheat sheet: Windows Files & Linux Files. Try Read them all!!
8. Sometimes dont need be so tech. keep it simple with sweeping passwords!
9. Make username and password list. Spray all possible assholes (services)
10. CHECK TYPO !
11. All uncommon string can be sub directory -,- e.g. you found weeb maybe can try 192.168.55.66/weeb  
12. Try more rev shell command and remember will have outbound port blocking! (think which port may be used even can curl =/= port can use)


# Kill port command
- dont ask why i put here LMAO
1. ```sudo ss -lptn 'sport = :8080'```
2. ``` kill {pid} ```