## Acquire SSL-certificate

**Important:** ports 80 and 443 must be open to external world (see [Linux.md](Linux.md)).

These two commands are probably redundant:

    sudo rm /etc/nginx/sites-enabled/default
    sudo systemctl reload nginx


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


Result:

    Congratulations! Your certificate and chain have been saved at:
    /etc/letsencrypt/live/courier.dostavka.me/fullchain.pem
    Your key file has been saved at:
    /etc/letsencrypt/live/courier.dostavka.me/privkey.pem
    Your cert will expire on 2017-12-05. To obtain a new or tweaked
    version of this certificate in the future, simply run certbot again
    with the "certonly" option. To non-interactively renew *all* of
    your certificates, run "certbot renew"



## Set up automatic cert renewal

Add command `certbot renew` to `/etc/crontab`. Must be run at most every 90 days.

Run at 03:49 on Mondays:

    49 3 * * 1 certbot renew >> /var/log/certbot-renew.log


## Important!

After installing certbot, there are two systemd units created:

    /lib/systemd/system/certbot.service
    /lib/systemd/system/certbot.timer

They are responsible for automated certificates renewal twice daily. Timer unit sets crontab rule,
and the service unit actually fires `certbot -q renew`. Flag `-q` means `--quiet` -- no stdout.

You can disable these units since we've already set up automatic renewal:

    systemctl disable certbot.service
    systemctl disable certbot.timer
    systemctl stop certbot.timer


## Make nginx config more secure


    sudo mkdir -p /etc/nginx/ssl
    sudo openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048


## Complete nginx config example

[example-ssl.nginx](example-ssl.nginx)


## Test your configuration

https://www.ssllabs.com/ssltest/analyze.html?d=courier.dostavka.me

