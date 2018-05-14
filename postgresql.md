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

Home directory for automatically created `postgres` UNIX-user:

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

