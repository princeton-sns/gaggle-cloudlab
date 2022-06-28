#!/bin/bash

sudo apt update && sudo apt upgrade -y
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install -y nodejs
cd /local && mkdir gaggle && cd gaggle && sudo chmod 774 .
git clone --branch remotes/origin/web-bench/latency git@github.com:princeton-sns/noise.git
cd noise/libnoise-server/ && npm install
cd ../bench/web-bench/server
tmux new
