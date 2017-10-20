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


