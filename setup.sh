#!/bin/bash
sudo apt update && sudo apt upgrade -y 2> err1 1> out1
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash - 2> err2 1> out2
sudo apt install -y nodejs 2> err3 1> out3
cd /local && mkdir gaggle && cd gaggle && sudo chmod 774 . 2> err4 1> out4
cp /local/repository/install_server.sh . 2> err5 1> out5
cp /local/repository/install_client.sh . 2> err6 1> out6
