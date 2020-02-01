## Acquire SSL-certificate

**Important:** ports 80 and 443 must be open to external world (see [linux.md](linux.md)).

Create working config in `/etc/nginx/sites-available/` only for port 80. nginx must listen to 80 and 443 ports.
Certificates and SSL-commands are missing for now.

    listen 80;
    server_name courier.dostavka.me;

Complete instructions: https://certbot.eff.org/#ubuntuxenial-nginx

    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:certbot/certbot
    sudo apt-get update
    sudo apt-get install python-certbot-nginx

Your nginx server directive must listen to both 80 and 443 ports in order for the following command to work.
Run this command and choose interactively what domains you want to set up SSL for:

    sudo certbot --nginx

Agree to redirection.

## Test your configuration

https://www.ssllabs.com/ssltest/analyze.html?d=courier.dostavka.me
