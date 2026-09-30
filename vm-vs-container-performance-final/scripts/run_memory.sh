#!/bin/bash
set -e
mkdir -p results/raw/memory
sysbench memory --memory-block-size=1M --memory-total-size=10G --threads=4 run > results/raw/memory/memory.txt
