# 0x0E. Web stack debugging #1

---

> Web debugging tasks on fixing errors on why the web is not working as it should

## TASKS

**0. Nginx likes port 80**

I Was to find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80.

Then, write a Bash script with the minimum number of commands to automate your fix.

Requirements:

- Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs

- Write a Bash script that configures a server to the above requirements

`0-nginx_likes_port_80` edits the configuration file for the server to listen at port 80
