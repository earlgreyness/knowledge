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

