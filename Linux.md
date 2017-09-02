# New VPS. Ubuntu 16.04 64bit

    sudo apt-get update
    sudo apt-get upgrade


GCC:

    sudo apt-get install build-essential

Locales:

    sudo locale-gen en_US.UTF-8
    sudo locale-gen ru_RU.UTF-8
    sudo dpkg-reconfigure locales

Python:

    sudo apt-get install python3-dev
    sudo apt-get install python3-pip
    sudo python3 -m pip install --upgrade pip


Open port 80 for incoming TCP connections:

    sudo apt-get install iptables-persistent
    sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
    sudo iptables-save > /etc/iptables/rules.v4



## Optional. Get rid of "command-not-found has crashed" problem:

    export LANGUAGE=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8  # doesn't always work ...
    locale-gen en_US.UTF-8
    sudo dpkg-reconfigure locales

    sudo apt-get install update-manager-core
    sudo do-release-upgrade



# GNU screen

    ssh user@somewhere
    screen
    ...
    ssh user@somewhere
    screen -ls
    screen -r
    exit

Switching:

    ctrl + a + n

New window:

    ctrl + a + c

Detach:

    ctrl + a + d

Exit:

    ctrl + a + x



# Create user

    adduser kirill


# RAM usage

    free -m

# Streams redirection

To run `command` on `in.txt` and save its output in `out.txt` and its stderr in `err.txt` you should run:

    command < in.txt > out.txt 2> err.txt


## Example
```bash
    $ which ssh-copy-id
    /usr/bin/ssh-copy-id

    $ cat < `which ssh-copy-id`
    Contents of the program...
```


# Ubuntu 16.04 and NVIDIA GeForce GTX 550 Ti

To add latest open source drivers to apt, issue these commands:

    sudo apt-add-repository ppa:graphics-drivers/ppa
    sudo apt-get update

Go to *Applications/Additional Drivers* and enable the latest NVIDIA **open source** driver.

To get rid of vsync issues, run this command:

    nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"

If you want to apply this permanently, do the following:

    sudo nvidia-xconfig
    sudo nano /etc/X11/xorg.conf

Working configuration:

    Section "Device"
        Identifier     "Device0"
        Driver         "nvidia"
        VendorName     "NVIDIA Corporation"
        Option         "RegistryDwords" "PerfLevelSrc=0x3322; PowerMizerDefaultAC=0x1"
        Option         "TripleBuffer" "True"
        Option         "TearFree" "True"
    EndSection

    Section "Screen"
        Identifier     "Screen0"
        Device         "Device0"
        Monitor        "Monitor0"
        DefaultDepth    24
        SubSection     "Display"
            Depth       24
        EndSubSection
        # Option "metamodes" "nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"
    EndSection


# SSH

## SSH without password

    cd ~
    ssh-keygen -t rsa
    ssh user@example.com mkdir -p .ssh
    cat ~/.ssh/id_rsa.pub | ssh user@example.com 'cat >> .ssh/authorized_keys'
    ls ~

Issue the command `ls ~/.ssh` and study contained files.

    ~/.ssh/id_rsa
    ~/.ssh/id_rsa.pub
    ~/.ssh/known_hosts

## Copy key

This command effectively copies `~/.ssh/id_rsa.pub` to remote `.ssh/authorized_keys`.

    ssh-copy-id m4u@10.10.0.105

## SSH tunnel

This command proxies socket `10.2.0.5:5411` as if we are actually on `m4u@10.10.0.105`.
The socket will be available at `localhost:9999`.

    ssh -nNT -L 9999:10.2.0.5:5411 m4u@10.10.0.105



# Init systems

## supervisor

    supervisorctl restart [service]

## Ubuntu 14.04 uses Upstart

Services are located at

    /etc/init/*.conf

They are triggered by

    sudo service php5-fpm [status|start|restart|stop]

## Ubuntu 16.04 uses systemd

    ...




# nginx, php5-fpm

    sudo apt-get install nginx
    sudo apt-get install php5-fpm

Unix socket file location.

    /var/run/php5-fpm.sock

Enabling sites.

    sudo ln -s /etc/nginx/sites-available/mirzakonov /etc/nginx/sites-enabled/

Check config syntax.

    nginx -t




# MySQL

## Creating database and user

    CREATE USER 'sa'@'localhost' IDENTIFIED BY 'password';
    CREATE DATABASE sa_blog
      DEFAULT CHARACTER SET utf8mb4
      DEFAULT COLLATE utf8mb4_unicode_ci;
    GRANT ALL ON sa_blog.* TO 'sa'@'localhost';
    FLUSH PRIVILEGES;

## wp-config.php

    /** Кодировка базы данных для создания таблиц. */
    define('DB_CHARSET', 'utf8mb4');

    /** Схема сопоставления. Не меняйте, если не уверены. */
    define('DB_COLLATE', 'utf8mb4_unicode_ci');

## Dumps

    mysqldump -u username -ppassword --comments --add-drop-table sa_blog > dump.sql

## Other

MySQL Database management software: https://www.adminer.org.



# PostgreSQL

Setup:

    sudo apt-get install postgresql
    sudo apt-get install postgresql-contrib
    sudo apt-get install libpq-dev
    sudo pip3 install psycopg2

Commands:

    CREATE USER "speaker" WITH PASSWORD 'the_password';
    CREATE DATABASE "speaker-db" WITH encoding='utf8'
                                      template="template0"
                                      LC_COLLATE='ru_RU.UTF-8'
                                      LC_CTYPE='ru_RU.UTF-8';
    GRANT ALL PRIVILEGES ON DATABASE "speaker-db" to "speaker";

Enter the shell:

    sudo -i -u postgres
    export LC_ALL=ru_RU.UTF-8
    psql [database_name]
    \l
    \d
    \c database_name

Create file `/etc/postgresql/9.3/main/environment` with this content:

    PGCLIENTENCODING=utf8

Configure `/etc/postgresql/9.3/main/postgres.conf`:

    max_connections = 1000
    ssl = false
    client_encoding = utf8

Home directory for automatically created `postgres` UNIX-user:

    /var/lib/postgresql
