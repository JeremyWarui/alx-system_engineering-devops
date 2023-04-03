# LOAD BALANCER

---

> Build a configuration of the web server. Replicate the first server to the second server. Set up HAproxy load balancer to manage the web servers

## TASKS

**0. Double the number of webservers**

[0-custom_http_response_header](./0-custom_http_response-header): Bash script that installs and configures Nginx on a server with a custom HTTP Response header.

    * The name of the HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.

**1. Install your load balancer**

Install and configure HAproxy on your lb-01 server.
[1-install_load_balancer](./1-install_load_balancer): Bash script that installs and configures HAproxy version 1.5 on a server.

    * Enables management via the init script.
    * Requests are distributed using a round-robin algorithm.
