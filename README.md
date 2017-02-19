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

