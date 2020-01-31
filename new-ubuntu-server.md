# New VPS. Ubuntu 18.04 64bit

    sudo apt-get update
    sudo apt-get upgrade


## Hostname

https://askubuntu.com/questions/87665/how-do-i-change-the-hostname-without-a-restart


## GCC

    sudo apt-get install build-essential


## Locales

    sudo locale-gen en_US.UTF-8
    sudo locale-gen ru_RU.UTF-8
    sudo dpkg-reconfigure locales
    
## Timezone

Set correct timezone systemwide:

    $ sudo timedatectl set-timezone Europe/Moscow
    $ timedatectl
    
Source: https://linuxize.com/post/how-to-set-or-change-timezone-on-ubuntu-18-04/

## Python

    sudo apt-get install -y libpq-dev python3-pip python3-venv


## Open ports 80 and 443

Open ports 80 and 443 for incoming TCP connections:

    sudo apt-get install iptables-persistent
    sudo iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
    sudo iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
    sudo iptables-save > /etc/iptables/rules.v4


## Users

Create necessary users:

    sudo adduser ads


## User services (systemd)

### Enable persistent journalctl Storage

https://serverfault.com/questions/806469/how-to-allow-a-user-to-use-journalctl-to-see-user-specific-systemd-service-logs
https://www.freedesktop.org/software/systemd/man/journald.conf.html
https://lists.freedesktop.org/archives/systemd-devel/2016-October/037554.html

Edit journalctl config:

    $ sudo nano /etc/systemd/journald.conf

Add line

    Storage=persistent

Restart:
    
    $ sudo systemctl daemon-reload
    $ sudo systemctl restart systemd-journald.service

### Auto-start and lingering

As root, give the user permission to run services when they're not logged in:
To enable start right after boot, regardless of user session:

    sudo loginctl enable-linger username

### Location of unit files

    ~/.config/systemd/user/

To enable unit (make it start automatically):

    systemctl --user enable myunit.service
    systemctl --user start myunit.service
    systemctl --user status myunit.service

To restart:

    systemctl --user restart myunit.service

if the unit file itself was changed, this is how to restart:

    systemctl --user daemon-reload
    systemctl --user restart myunit.service


### Reading the journal

    journalctl --user -u myunit.service -o cat -fn1000

Python buffers sys.stdout by default. If stdout is connected to tty console, it flushes on `\n` symbols. Otherwise, when stdout is connected to PIPE (which is what happens when you use systemd user units), it flushes unpredictably. Use loggers or do this (StreamHandler flushes each record), or set environment variable for the whole python interpreter. 12 factor apps recommend non-buffered output, which gives us only the last option.

    export PYTHONUNBUFFERED=1

    print('Hello World!', flush=True)


## Edit `/etc/sysctl.conf` for max performance

For Redis:

    vm.overcommit_memory = 1

For uWSGI:

    # Increase number of incoming connections
    net.core.somaxconn = 4096

Then restart sysctl by:

    sudo sysctl -p /etc/sysctl.conf
