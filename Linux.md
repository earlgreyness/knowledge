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


## Optional. Get rid of "command-not-found has crashed" problem:

    export LANGUAGE=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8  # doesn't always work ...
    locale-gen en_US.UTF-8
    sudo dpkg-reconfigure locales

    sudo apt-get install update-manager-core
    sudo do-release-upgrade


# Disk usage

Best tool so far is `ncdu`. Run it from any directory and see detailed usage info by subdirectories.



# Download file from server

    scp username@remote:/file/to/send /where/to/put


# Upload file to server

    scp /file/to/send username@remote:/where/to/put



# GNU screen

    ssh user@somewhere
    screen
    ...
    ssh user@somewhere
    screen -ls
    screen -r
    exit

Switching:

    ctrl + a + n

New window:

    ctrl + a + c

Detach:

    ctrl + a + d

Exit:

    ctrl + a + x



# Create user

    adduser kirill


# RAM usage

    free -m

# Streams redirection

To run `command` on `in.txt` and save its output in `out.txt` and its stderr in `err.txt` you should run:

    command < in.txt > out.txt 2> err.txt


## Difference between `>` and `>>`

The `>>` appends to a file or creates the file if it doesn't exist.

The `>` overwrites the file if it exists or creates it if it doesn't exist.


## Example

```bash
$ which ssh-copy-id
/usr/bin/ssh-copy-id

$ cat < `which ssh-copy-id`
(Contents of the file /usr/bin/ssh-copy-id)
```


# Ubuntu 16.04 and NVIDIA GeForce GTX 550 Ti

To add latest open source drivers to apt, issue these commands:

    sudo apt-add-repository ppa:graphics-drivers/ppa
    sudo apt-get update

Go to *Applications/Additional Drivers* and enable the latest NVIDIA **open source** driver.

To get rid of vsync issues, run this command:

    nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"

If you want to apply this permanently, do the following:

    sudo nvidia-xconfig
    sudo nano /etc/X11/xorg.conf

Working configuration:

    Section "Device"
        Identifier     "Device0"
        Driver         "nvidia"
        VendorName     "NVIDIA Corporation"
        Option         "RegistryDwords" "PerfLevelSrc=0x3322; PowerMizerDefaultAC=0x1"
        Option         "TripleBuffer" "True"
        Option         "TearFree" "True"
    EndSection

    Section "Screen"
        Identifier     "Screen0"
        Device         "Device0"
        Monitor        "Monitor0"
        DefaultDepth    24
        SubSection     "Display"
            Depth       24
        EndSubSection
        # Option "metamodes" "nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"
    EndSection

