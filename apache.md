# Apache setup

    sudo apt-get --purge remove apache2
    apt-get install apache2
    NO! SEE OTHER FILE!
    # apt-get install libapache2-mod-wsgi-py3
    sudo a2enmod headers
    sudo a2enmod wsgi

# Apache directory is located at /etc/apache2
# Files "apache2.conf", "envvars", "magic", "ports.conf" should not be changed

# at /etc/apache2/sites-available and /etc/apache2/sites-enabled
# files must have .conf extension
# So:
    etc
      apache2
        sites-available
          000-default.conf  # exists by default
          default-ssl.conf  # exists by default
          training-vps.ru.conf  # have to provide
        sites-enabled
          000-default.conf  # link, exists by default
          training-vps.ru.conf  # link, created by a2ensite (see below)

# this will create a necessary link at /etc/apache2/sites-enabled
    a2ensite training-vps.ru

    service apache2 restart


# user www-data in group www-data (see training-vps.ru.conf file)
# must be given permissions to own folder /var/www/training-vps.ru/ and all its files and subfolders recursively
# to do that, make /var/www current directory
# then:

    sudo chown -R www-data:www-data /var/www
    sudo chmod -R g+rw /var/www

# this command will make www-data owner of the folder
# this will enable www-data to create/delete files/folders in training-vps.ru (working with sqlite3 databases, writing logs etc)


# how to allow access only from several domains:
    <Directory //var/www/training-vps.ru/>
        WSGIProcessGroup flask
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Deny from all
        Allow from 94.103.232.214
        Header set Pragma "no-cache"
    </Directory>

# how to include access-control-allow-origin header:
    <Directory //var/www/training-vps.ru/>
        ...
        Header set Access-Control-Allow-Origin "*"
    </Directory>

# to unsure that changes are correct:
    apachectl -t

# How to check which MPM apache is currently running:
    apachectl -V | grep -i mpm

# How to list available MPM Modules (make sure mpm_prefork is listed):
    ls /etc/apache2/mods-available/mpm*

# How to disable event:
    a2dismod mpm_event

# How to enable prefork:
    a2enmod mpm_prefork

# Apache restart:
    service apache2 restart

# Apache logs location:
    /var/log/apache2/access.log


