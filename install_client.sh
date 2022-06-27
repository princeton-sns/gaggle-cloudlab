#!/bin/bash
git clone git@github.com:princeton-sns/noise.git && cd noise
git checkout remotes/origin/web-bench/latency
cd libnoise-client/ && npm install && cd ..
cd bench/web-bench/client && npm install
