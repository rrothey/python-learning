cycle_times = [12, 14, 11, 13, 15, 12, 14, 16, 13, 12]

total = 0
for t in cycle_times:
    total += t

average = total / len(cycle_times)
print("Average Cycle Time:", average)
# Expected output: Average Cycle Time: 13.2