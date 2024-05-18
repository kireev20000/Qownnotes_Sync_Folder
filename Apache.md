Apache
======
```
docker run -d --name ApacheServ -p 8080:80 -v B:/_WorkLab/passp_region/backend:/var/www/passpregion/ httpd:latest


```

sudo service apache2 start
sudo service apache2 restart
sudo service apache2 stop

apachectl -S

apache2 -l

имя папки
sudo chown -R $USER apache2


The default Apache error log file is at one of the following locations: /var/log/apache2/error. log (Ubuntu and Debian)
The main configuration details for your Apache server are held in the /etc/apache2/apache2. conf file.


[WSL2-Windows Linux Subsystem: A guide to install a Local Web Server Ubuntu-20.04 Apache,PHP8 y MySQL8 - DEV Community](https://dev.to/aitorsol/wsl2-windows-linux-subsystem-a-guide-to-install-a-local-web-server-ubuntu-20-04-apache-php8-y-mysql8-3bbk)

[How to Install Apache in Docker](https://phoenixnap.com/kb/docker-apache)

[How to Use the Apache httpd Docker Official Image | Docker](https://www.docker.com/blog/how-to-use-the-apache-httpd-docker-official-image/)