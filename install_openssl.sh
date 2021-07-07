#!/bin/bash

set -ex

wget https://www.openssl.org/source/old/1.1.0/openssl-1.1.0g.tar.gz
tar xzvf openssl-1.1.0g.tar.gz
cd openssl-1.1.0g
./config
make
sudo make install

openssl version -a
