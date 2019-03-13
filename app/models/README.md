# Setting up MySQL in c9 #

1.  You need to install the phpmyadmin client in c9. 
    ```shell
    phpmyadmin-ctl install
```
2. Create new database called tunnel_vision
3. Create User called tunnel_vision with the password given
4. run 
   ```shell
   python create_db.py
   ```

Everytime you start your c9 environment you need to start the mysql server
```shell
mysql-ctl start
```