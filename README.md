# Open folder in Sublime Text 3

Open `~/.bashrc` in your favorite text editor.

    [nano|gedit|mcedit|subl] ~/.bashrc

Add the following line somewhere (for instance, in aliases section).

    alias subl3='subl -n -a .'

Now you can open current directory in Sublime just by entering the command `subl3` in terminal.

# SSH tunnel

This command proxies socket `10.2.0.5:5411` as if we are actually on `m4u@10.10.0.105`.
The socket will be available at `localhost:9999`.

    ssh -nNT -L 9999:10.2.0.5:5411 m4u@10.10.0.105

# Ubuntu 14.04 uses Upstart

Services are located at

    /etc/init/*.conf

They are triggered by

    sudo service php5-fpm [status|start|restart|stop]

# Ubuntu 16.04 uses systemd

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


# SSH without password.

    cd ~
    ssh-keygen -t rsa
    ssh root@jurist-rus.ru mkdir -p .ssh
    cat ~/.ssh/id_rsa.pub | ssh root@jurist-rus.ru 'cat >> .ssh/authorized_keys'
    ls ~

Issue the command `ls ~/.ssh` and study contained files.

    ~/.ssh/id_rsa
    ~/.ssh/id_rsa.pub
    ~/.ssh/known_hosts


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
    psql
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


# Git

Create new branch and switch to it immediately:

    git checkout -b BRANCH_NAME

The first time pushing that branch:

    git push [-u|--set-upstream] origin BRANCH_NAME

Resets the index and working tree. Any changes to tracked files in the working tree since <commit> are discarded.

    git reset --hard HEAD

# Django

This is equivalent to `GROUP BY` in raw SQL.

```python
AggregatedOrders.objects
                .filter(date__in=dates, restaurant_id=restaurant_id)
                .values('date')
                .annotate(count=Sum(F('count_total') - F('count_deleted')))
                .order_by('count')
```

# Tools

* Genymotion (https://www.genimotion.com) for testing Android on desktop.

Genymotion requires Oracle VirtualBox (https://www.virtualbox.org/wiki/Linux_Downloads)

After that we can run `*.apk` files on it -- like Apps from Google Market

My account on genimotion: `earlgreyness`.

# Linux

RAM usage in Ubuntu:

    free -m

