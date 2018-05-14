# nginx, php5-fpm

    sudo apt-get install nginx
    sudo apt-get install php5-fpm

Unix socket file location.

    /var/run/php5-fpm.sock

Enabling sites.

    sudo ln -s /etc/nginx/sites-available/mirzakonov /etc/nginx/sites-enabled/

Check config syntax.

    nginx -t


Don't forget to add uWSGI users to `www-data` group:

    sudo usermod -a -G ads www-data

