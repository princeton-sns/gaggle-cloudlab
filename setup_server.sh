#!/bin/bash
sudo apt update && sudo apt upgrade -y
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install -y nodejs
cd /local && mkdir gaggle && cd gaggle && sudo chmod 774 .
cp /local/repository/install_server.sh .
