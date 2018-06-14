# Install PostgreSQL 10.4 on Ubuntu 16.04


Using this instruction: https://www.postgresql.org/download/linux/ubuntu/.

We are assuming that standard for Ubuntu 16.04 Postgres 9.5 is already set up and running.

Stop all services that keep open Postgresql connections.

## (Optional) Uninstall other versions of postgres

To make life simple, remove all other versions of Postgres. Obviously not required, but again, makes life simple.

    dpkg -l | grep postgres

returned for me:

    ii  postgresql                                  9.5+173                                                     all          object-relational SQL database (supported version)
    ii  postgresql-9.5                              9.5.8-0ubuntu0.16.04.1                                      amd64        object-relational SQL database, version 9.5 server
    ii  postgresql-client-9.5                       9.5.8-0ubuntu0.16.04.1                                      amd64        front-end programs for PostgreSQL 9.5
    ii  postgresql-client-common                    173                                                         all          manager for multiple PostgreSQL client versions
    ii  postgresql-common                           173                                                         all          PostgreSQL database-cluster manager
    ii  postgresql-contrib-9.5                      9.5.8-0ubuntu0.16.04.1

... therefore I ran:

    sudo apt-get --purge remove postgresql postgresql-9.5 postgresql-client-9.5 postgresql-client-common  postgresql-common postgresql-contrib-9.5

## Add PostgreSQL apt repository

Create the file `/etc/apt/sources.list.d/pgdg.list` and add a line for the repository

    deb http://apt.postgresql.org/pub/repos/apt/ YOUR_UBUNTU_VERSION_HERE-pgdg main

In our case `YOUR_UBUNTU_VERSION_HERE` is `xenial`.

Import the repository signing key, and update the package lists

    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo apt-get update


## Install PostgreSQL

    sudo apt-get install postgresql-10


## Check successfullness

    sudo su - postgres
    psql
    select version();
    \l

Then create your databases and users and restore dumps back to the database.

No additional cleanup is required.



# General commands

Setup:

    sudo apt-get install postgresql postgresql-contrib libpq-dev

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

Create file `/etc/postgresql/9.5/main/environment` with this content:

    PGCLIENTENCODING=utf8

Configure `/etc/postgresql/9.5/main/postgres.conf`:

    max_connections = 1000
    ssl = false

Then:

    sudo systemctl restart postgresql

Home directory for automatically created `postgres` UNIX-user and all the data is also here:

    /var/lib/postgresql


# Dumps and Restores

Use `pg_dump`. Login as the same user as your database role. And then:

    pg_dump dbName --create --clean > outfile

Then locally:

    sudo su postgres psql < outfile

Alternativelly:

    pg_dump --dbname="postgresql://glue:****@localhost:5432/glue" > outfile

## Full example

Create dump:

    pg_dump --dbname="postgresql://glue:****@localhost:5432/glue" --create --clean | gzip -9 > dump.sql.gz

Restore from dump:

    gunzip < dump.sql.gz | sudo -u postgres psql

