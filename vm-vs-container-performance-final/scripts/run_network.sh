#!/bin/bash
set -e
mkdir -p results/raw/network
iperf3 -c "$1" -t 30 > results/raw/network/iperf3-single.txt
iperf3 -c "$1" -t 30 -P 4 > results/raw/network/iperf3-parallel.txt
