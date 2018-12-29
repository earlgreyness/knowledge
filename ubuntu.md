How to restore Windows entry to GRUB after installing Ubuntu:

    sudo update-grub


# Shell (Bash)

## How to run command directly, but not its alias

You should prefix the command with the backslash symbol `\`. For instance:

    \ls


## Why do some python scripts begin with #!/usr/bin/env python?

If you have several versions of Python installed, `/usr/bin/env` will ensure the interpreter used is the first one on your environment's `$PATH`.



# Disk usage

Best tool so far is `ncdu`. Run it from any directory and see detailed usage info by subdirectories.


# Downloading, uploading files

## scp

Download file from server:

    scp username@remote:/file/to/send /where/to/put


Upload file to server:

    scp /file/to/send username@remote:/where/to/put


## rsync

Archive directory `archive/`

    tar -cv archive | gzip > archive.tar.gz

Upload file to server, limiting bandwidth to 1000 kB/s:

    rsync --bwlimit=1000 --progress -avz archive.tar.gz root@example.com:/home/

Decompress archive on server to current directory:

    gunzip < archive.tar.gz | tar -xv


# GNU screen

    ssh user@somewhere
    screen
    ...
    ssh user@somewhere
    screen -ls
    screen -r
    exit

Detach:

    Ctrl+A, Ctrl+D

Enable mouse scroll in screen:

    echo 'termcapinfo xterm* ti@:te@' >> ~/.screenrc


# Users, Groups

Create user:

    adduser kirill

Add existing user to group:

    usermod -a -G groupName userName

Delete user (with home directory):

    userdel -r userName


Delete user from group

    deluser userName groupName

Delete group

    groupdel kirill


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

