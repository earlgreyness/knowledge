Install php and apache module for php:

    sudo apt-get install php
    sudo apt-get install libapache2-mod-php

Install php libraries:

    sudo apt-get install php-mcrypt
    sudo apt-get install php-mysql
    sudo apt-get install php-curl
    sudo apt-get install php-imap

Restart apache for libraries to activate:

    sudo systemctl restart apache2

Ensure libraries are activated:

    sudo php -m | grep imap

