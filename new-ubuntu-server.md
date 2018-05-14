# New VPS. Ubuntu 16.04 64bit

    sudo apt-get update
    sudo apt-get upgrade


GCC:

    sudo apt-get install build-essential

tcl language for redis test suite:

    sudo apt-get install tcl

Locales:

    sudo locale-gen en_US.UTF-8
    sudo locale-gen ru_RU.UTF-8
    sudo dpkg-reconfigure locales

Python:

    sudo apt-get install python3-dev
    sudo apt-get install python3-pip
    sudo apt-get install python3-venv
    sudo python3 -m pip install --upgrade pip
    sudo python3 -m pip install --upgrade setuptools

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
