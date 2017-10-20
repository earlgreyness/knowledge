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
