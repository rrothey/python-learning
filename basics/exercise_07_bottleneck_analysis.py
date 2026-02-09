import pandas as pd
df = pd.read_csv("cycle_times.csv")
bottleneck = df.groupby("station")["cycle_time"].mean().idxmax()
print("Bottleneck station:", bottleneck)