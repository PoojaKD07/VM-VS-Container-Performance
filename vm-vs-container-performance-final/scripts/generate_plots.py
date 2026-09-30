from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
processed = root / "results" / "processed"
figures = root / "results" / "figures"
figures.mkdir(parents=True, exist_ok=True)

cpu = pd.read_csv(processed / "cpu_scalability.csv")
plt.figure(figsize=(8,5))
plt.plot(cpu["threads"], cpu["events_per_second"], marker="o")
plt.xlabel("Number of Threads")
plt.ylabel("Events per Second")
plt.title("CPU Performance vs Number of Threads")
plt.grid(True)
plt.tight_layout()
plt.savefig(figures / "cpu_scalability.png", dpi=300)
plt.close()

memory = pd.read_csv(processed / "memory_observed.csv")
plt.figure(figsize=(7,5))
plt.bar(memory["workload"], memory["throughput_mib_per_sec"])
plt.ylabel("MiB/s")
plt.title("Observed Memory Throughput")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(figures / "memory_observed.png", dpi=300)
plt.close()

network = pd.read_csv(processed / "network_observed.csv")
plt.figure(figsize=(8,5))
plt.bar(network["test"], network["throughput_gbit_per_sec"])
plt.ylabel("Gbit/s")
plt.title("Observed Network Throughput")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(figures / "network_observed.png", dpi=300)
plt.close()

api = pd.read_csv(processed / "api_benchmark_observed.csv")
plt.figure(figsize=(7,5))
plt.bar(api["endpoint"], api["requests_per_second"])
plt.ylabel("Requests/s")
plt.title("Observed FastAPI Throughput")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(figures / "api_requests_per_second.png", dpi=300)
plt.close()

startup = pd.read_csv(processed / "startup_times.csv")
plt.figure(figsize=(7,5))
plt.plot(startup["run"], startup["real_seconds"], marker="o")
plt.xlabel("Run")
plt.ylabel("Real Time (s)")
plt.title("Container Startup Time")
plt.grid(True)
plt.tight_layout()
plt.savefig(figures / "startup_time.png", dpi=300)
plt.close()
