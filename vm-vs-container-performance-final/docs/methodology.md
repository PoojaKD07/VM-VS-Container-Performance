# Methodology

The project uses the same benchmark workloads for VM and Docker environments. The lab manual specifies Sysbench for CPU and memory, fio for disk I/O, iperf3 for network throughput, FastAPI with Apache Benchmark for application performance, and repeated startup measurements for startup time.

CPU scalability uses 1, 2, 4 and 8 threads. The controlled CPU workload is `--cpu-max-prime=20000 --time=30`.

Memory uses a 1 MiB block, 10 GiB total workload and four threads.

Disk uses sequential and random read/write workloads with fio, 2 GiB test size, direct I/O, queue depth 16 and 30-second runtime.

Network uses iperf3 for 30 seconds with one stream and four parallel streams.

FastAPI is benchmarked using `/health` and `/compute` with Apache Benchmark. Startup uses `time docker run` with repeated runs.
