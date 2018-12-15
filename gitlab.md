# Installing self-managed Gitlab Communiti Edition

## Installing Gitlab

Instruction: https://about.gitlab.com/install/#ubuntu

We are installing Omnibus package (recommended) on Ubuntu 18.04 LTS.

Obtain barebones Ubuntu server. Don't touch it in any way (don't even open ports).

Installing dependencies:

    sudo apt-get update
    sudo apt-get install -y curl openssh-server ca-certificates

Installing Gitlab:

    curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
    sudo EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee

## Installing additional components

Instruction: https://docs.gitlab.com/omnibus/README.html#installation-and-configuration-using-omnibus-package

### Installing HTTPS

Instruction: https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https. Choose Let's Encrypt.

### Configuring Email notifications

Just install `sendmail` properly:

    sudo apt-get install sendmail

## Install server-side commit hooks

Instruction: https://docs.gitlab.com/ee/administration/custom_hooks.html
