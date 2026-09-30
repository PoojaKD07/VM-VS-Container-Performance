#!/bin/bash
set -e
mkdir -p results/raw/cpu/vm
for threads in 1 2 4 8; do
  sysbench cpu --cpu-max-prime=20000 --threads=$threads --time=30 run > results/raw/cpu/vm/threads-${threads}.txt
done
