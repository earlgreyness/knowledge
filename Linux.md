RAM usage:

    free -m

# Streams redirection

To run `command` on `in.txt` and save its output in `out.txt` and its stderr in `err.txt` you should run:

    command < in.txt > out.txt 2> err.txt


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


# SSH

## SSH without password

    cd ~
    ssh-keygen -t rsa
    ssh user@example.com mkdir -p .ssh
    cat ~/.ssh/id_rsa.pub | ssh user@example.com 'cat >> .ssh/authorized_keys'
    ls ~

Issue the command `ls ~/.ssh` and study contained files.

    ~/.ssh/id_rsa
    ~/.ssh/id_rsa.pub
    ~/.ssh/known_hosts

## Copy key

This command effectively copies `~/.ssh/id_rsa.pub` to remote `.ssh/authorized_keys`.

    ssh-copy-id m4u@10.10.0.105

## SSH tunnel

This command proxies socket `10.2.0.5:5411` as if we are actually on `m4u@10.10.0.105`.
The socket will be available at `localhost:9999`.

    ssh -nNT -L 9999:10.2.0.5:5411 m4u@10.10.0.105



# Init systems

## supervisor

    supervisorctl restart [service]

## Ubuntu 14.04 uses Upstart

Services are located at

    /etc/init/*.conf

They are triggered by

    sudo service php5-fpm [status|start|restart|stop]

## Ubuntu 16.04 uses systemd

    ...