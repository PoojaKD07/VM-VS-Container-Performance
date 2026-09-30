#!/bin/bash
set -e
docker run --rm --cpus=4 --memory=8g vm-container-benchmark sysbench cpu --cpu-max-prime=20000 --threads=4 --time=30 run
docker run --rm vm-container-benchmark sysbench memory --memory-block-size=1M --memory-total-size=10G --threads=4 run
