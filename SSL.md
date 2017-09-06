## Acquire SSL-certificate

Ports 80 and 443 must be open to external world (see above).


    sudo rm /etc/nginx/sites-enabled/default
    sudo systemctl reload nginx


Create config in `/etc/nginx/sites-available/`. Your `server` directive must contain at least this:

    listen 80;
    listen [::]:80;
    listen 443 ssl;
    listen [::]:443 ssl;
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

Add command `certbot renew` to `/etc/crontab`. Must be run every 90 days.

    30 2 * * 1 certbot renew >> /var/log/le-renew.log


## Make nginx config more secure


    sudo mkdir -p /etc/nginx/ssl
    sudo openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048



## Test your configuration

https://www.ssllabs.com/ssltest/analyze.html?d=courier.dostavka.me

