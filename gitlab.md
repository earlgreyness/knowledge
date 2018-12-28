# Installing self-managed Gitlab Community Edition

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

Pay close attention to installation stdout, it will probably ask you to manually configure sendmail config files.

You should also update `/etc/hosts` file, making its first line look like this:

    127.0.0.1   localhost gitlab.speechanalytics.ru

## Configure time zone

Instruction:

https://docs.gitlab.com/ee/workflow/timezone.html

Add the following line to config file `/etc/gitlab/gitlab.rb`:

    gitlab_rails['time_zone'] = 'Europe/Moscow'

## Install server-side commit hooks

Instruction: https://docs.gitlab.com/ee/administration/custom_hooks.html
