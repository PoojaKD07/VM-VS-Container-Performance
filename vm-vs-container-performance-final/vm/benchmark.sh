#!/bin/bash
set -e
sysbench cpu --cpu-max-prime=20000 --threads=4 --time=30 run
sysbench memory --memory-block-size=1M --memory-total-size=10G --threads=4 run
