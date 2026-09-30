from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
out = root / "results" / "processed"
out.mkdir(parents=True, exist_ok=True)

cpu = pd.read_csv(out / "cpu_scalability.csv")
comparable = cpu[cpu["prime_limit"] == 20000].copy()
comparable["scaling_vs_1_thread"] = comparable["events_per_second"] / comparable.loc[comparable["threads"] == 1, "events_per_second"].iloc[0]
comparable["increase_vs_1_thread_percent"] = (comparable["scaling_vs_1_thread"] - 1) * 100
comparable.to_csv(out / "cpu_scalability_calculations.csv", index=False)

startup = pd.read_csv(out / "startup_times.csv")
summary = pd.DataFrame([{
    "mean_seconds": startup["real_seconds"].mean(),
    "median_seconds": startup["real_seconds"].median(),
    "min_seconds": startup["real_seconds"].min(),
    "max_seconds": startup["real_seconds"].max(),
    "std_seconds": startup["real_seconds"].std(ddof=1),
}])
summary.to_csv(out / "startup_statistics.csv", index=False)
print(summary.to_string(index=False))
