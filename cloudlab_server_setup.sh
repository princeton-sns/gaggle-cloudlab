#!/bin/bash
sudo apt update && sudo apt upgrade -y
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install -y nodejs
cd .. && git clone git@github.com:princeton-sns/noise.git && cd noise
git checkout remotes/origin/web-bench/latency
cd libnoise-server/ && npm install && cd ..
cd bench/web-bench/server
node index.js
