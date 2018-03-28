uWSGI master process takes requests directly from nginx. The top amount of them is limited
by Linux kernel parameter

    net.core.somaxconn

Increase it by adding the following line

    net.core.somaxconn=4096

to `sudo nano /etc/sysctl.conf`.

To apply this immediately, issue

    echo 4096 > /proc/sys/net/core/somaxconn


Also there is a `listen` directive for uWSGI config, it must be also set as `4096`.
