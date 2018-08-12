# New VPS. Ubuntu 18.04 64bit

    sudo apt-get update
    sudo apt-get upgrade


Change hostname:

https://askubuntu.com/questions/87665/how-do-i-change-the-hostname-without-a-restart


GCC:

    sudo apt-get install build-essential


Locales:

    sudo locale-gen en_US.UTF-8
    sudo locale-gen ru_RU.UTF-8
    sudo dpkg-reconfigure locales

Software:

    sudo apt-get install sox libsox-fmt-mp3
    sudo apt-get install postgresql postgresql-contrib libpq-dev
    sudo apt-get install redis-server
    sudo apt-get install nginx
    sudo apt-get install htop ncdu mc

Python:

    sudo apt-get install python3-dev
    sudo apt-get install python3-pip
    sudo apt-get install python3-venv
    sudo apt install python3-widgetsnbextension
    sudo apt install python3-testresources
    sudo python3 -m pip install --upgrade pip setuptools wheel
    sudo python3 -m pip install uwsgi


Open ports 80 and 443 for incoming TCP connections:

    sudo apt-get install iptables-persistent
    sudo iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
    sudo iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
    sudo iptables-save > /etc/iptables/rules.v4


Create necessary users:

    sudo adduser ads


## Edit `/etc/sysctl.conf` for max performance:

For Redis:

    vm.overcommit_memory = 1

For uWSGI:

    # Increase number of incoming connections
    net.core.somaxconn = 4096

Then restart sysctl by:

    sudo sysctl -p /etc/sysctl.conf


Don't forget to add uWSGI users to `www-data` group:

    sudo usermod -a -G ads www-data
