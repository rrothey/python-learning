import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cycle_times.csv")
df['cycle_time'].plot(kind='hist', bins=10)
plt.title("Cycle Time Distribution")
plt.xlabel("Seconds")
plt.show()