# Basic AUTH

    location / {
        root "/home/worker/public";
        try_files $uri$args $uri$args/ /index.html;
        auth_basic "Restricted";
        auth_basic_user_file /home/worker/.htpasswd;
    }

Follow the instructions: https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/

1. Verify that `apache2-utils` is installed.

    sudo apt-get install apache2-utils

2. Create a password file and a first user. Run the `htpasswd` utility with the `-c` flag (to create a new file), the file pathname as the first argument, and the username as the second argument:

    $ sudo htpasswd -c /etc/apache2/.htpasswd user1

Press Enter and type the password for **user1** at the prompts.

3. Create additional user-password pairs. Omit the `-c` flag because the file already exists:

    $ sudo htpasswd /etc/apache2/.htpasswd user2

4. You can confirm that the file contains paired usernames and encrypted passwords:

    $ cat /etc/apache2/.htpasswd
    user1:$apr1$/woC1jnP$KAh0SsVn5qeSMjTtn0E9Q0
    user2:$apr1$QdR8fNLT$vbCEEzDj7LyqCMyNpSoBh/
    user3:$apr1$Mr5A0e.U$0j39Hp5FfxRkneklXaMrr/


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

