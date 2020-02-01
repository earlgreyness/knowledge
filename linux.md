# Bash

## How to run command directly, but not its alias

You should prefix the command with the backslash symbol `\`. For instance:

    \ls

## Why do some python scripts begin with #!/usr/bin/env python?

If you have several versions of Python installed, `/usr/bin/env` will ensure the interpreter used is the first one on your environment's `$PATH`.

# Disk usage

Best tool so far is `ncdu`. Run it from any directory and see detailed usage info by subdirectories.

# Downloading, uploading files

## scp

**Download** file from server:

    scp username@remote:/file/to/send /where/to/put

**Upload** file to server:

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

# SSH

## Forbid password ssh autorization

(good security practice as it eliminates brute force possibility)

Edit sshd daemon config:

    /etc/ssh/sshd_config
    # To disable tunneled clear text passwords, change to no here!
    PasswordAuthentication no

Restart sshd daemon:

    sudo systemctl restart sshd.service

## Prevent ssh client from disconnecting

To fix constant `Broken pipe` errors, add these lines:

    Host *
    ServerAliveInterval 30

to file `~/.ssh/config`. Usually the file needs to be created first. It is the ssh client config.

This settings forces ssh client to ping ssh server every 30 seconds. By default there are no pings at all.

## Copy key

This command effectively copies `~/.ssh/id_rsa.pub` to remote `.ssh/authorized_keys`.

    ssh-copy-id m4u@10.10.0.105

## SSH tunnel

This command proxies socket `10.2.0.5:5411` as if we are actually on `m4u@10.10.0.105`.
The socket will be available at `localhost:9999`.

    ssh -nNT -L 9999:10.2.0.5:5411 m4u@10.10.0.105
