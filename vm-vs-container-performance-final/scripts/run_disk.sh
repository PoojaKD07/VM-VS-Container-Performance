#!/bin/bash
set -e
mkdir -p ~/fio-test results/raw/disk
fio --name=seq-write --filename=~/fio-test/testfile --size=2G --bs=1M --rw=write --direct=1 --iodepth=16 --runtime=30 --time_based > results/raw/disk/seq-write.txt
fio --name=seq-read --filename=~/fio-test/testfile --size=2G --bs=1M --rw=read --direct=1 --iodepth=16 --runtime=30 --time_based > results/raw/disk/seq-read.txt
fio --name=random-read --filename=~/fio-test/testfile --size=2G --bs=4k --rw=randread --direct=1 --iodepth=16 --runtime=30 --time_based > results/raw/disk/random-read.txt
fio --name=random-write --filename=~/fio-test/testfile --size=2G --bs=4k --rw=randwrite --direct=1 --iodepth=16 --runtime=30 --time_based > results/raw/disk/random-write.txt
