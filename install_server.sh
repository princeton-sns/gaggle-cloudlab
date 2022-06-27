#!/bin/bash
git clone git@github.com:princeton-sns/noise.git && cd noise
git checkout remotes/origin/web-bench/latency
cd libnoise-server/ && npm install && cd ..
cd bench/web-bench/server
tmux new
