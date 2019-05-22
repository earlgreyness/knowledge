# Install Python 3.6.7 on Ubuntu 19.04 (where default Python is 3.7.3)

Install dependencies:

    sudo apt-get install -y build-essential libbz2-dev libssl-dev libreadline-dev \
                            libffi-dev libsqlite3-dev tk-dev

    # optional scientific package headers (for Numpy, Matplotlib, SciPy, etc.)
    sudo apt-get install -y libpng-dev libfreetype6-dev  

Install Python 3.6.7 from source:

    cd /usr/src
    sudo wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz
    
    sudo tar xzf Python-3.6.7.tgz

    cd Python-3.6.7
    sudo ./configure --enable-optimizations
    sudo make altinstall

    python3.6 --version

Links:

https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get
